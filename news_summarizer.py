from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc

def get_news_content(topic):
  
    driver = uc.Chrome()


    driver.get('https://www.google.com')


    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(topic)
    search_box.send_keys(Keys.RETURN)  


    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "tbm=nws")]')))

    news_tab = driver.find_element(By.XPATH, '//a[contains(@href, "tbm=nws")]')
    news_tab.click()

    
    contents = []

   
    for i in range(5):
     
        try:
            article = driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[10]/div/div/div[2]/div[2]/div/div/div/div/div[{i+1}]/div/div/a')
            article_url = article.get_attribute('href')
            print(f"\nOpening article {i + 1}: {article_url}")
            driver.get(article_url)
        except:
            pass

            

        try:
     
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        except:
            pass

        try:
          
            content = driver.find_element(By.TAG_NAME, 'body').text  
            contents.append(content)
         
        except Exception as e:
            print(f"Could not extract content from article {i + 1}: {str(e)}")


        driver.back()  

        time.sleep(10)  

  
    driver.quit()
    return contents




if __name__ == "__main__":
    import pickle

    topic = input("Enter the topic to search for news: ")
    contents =get_news_content(topic)
    with open("scraped_articles.pkl", "wb")  as f:
        pickle.dump(contents, f)
    dict ={}
    for i in range(1, 6):
        dict[f"a{i}"] =contents[i-1]

    from dotenv import load_dotenv
    load_dotenv()
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain.schema.runnable import RunnableLambda, RunnableSequence, RunnableParallel

    llm =ChatOpenAI(model ="gpt-4o")
    pt =ChatPromptTemplate.from_messages (
        [
            ("system", "You are AI Text Cleaner and Summarizer"),
            ("human", "Clean and Summarize {text}")
        ]
    )


    b1 =RunnableLambda(lambda x: pt.invoke(x["a1"])) | llm | (lambda x: x.content)
    b2 =RunnableLambda(lambda x: pt.invoke(x["a2"])) | llm | (lambda x: x.content)
    b3 =RunnableLambda(lambda x: pt.invoke(x["a3"])) | llm | (lambda x: x.content)
    b4 =RunnableLambda(lambda x: pt.invoke(x["a4"])) | llm | (lambda x: x.content)
    b5 =RunnableLambda(lambda x: pt.invoke(x["a5"])) | llm | (lambda x: x.content)
    pt =ChatPromptTemplate.from_template("You are given a dictionary containing the content of five different news articles. Each article is stored with keys `b1`, `b2`, `b3`, `b4`, and `b5`, where the value of each key is the text of an individual article. Please summarize all five articles while retaining all key details, facts, and main points. Ensure that no important information is left out from any of the articles. The articles as follows {x}"
    ) 

    chain =(lambda x: x) | RunnableParallel(branches ={"b1":b1, "b2":b2, "b3":b3, "b4":b4, "b5":b5}) |( lambda x: str(x["branches"])) | pt | llm | (lambda x: x.content)

    with open("summary.txt", "w") as f:
        f.write(chain.invoke(dict))