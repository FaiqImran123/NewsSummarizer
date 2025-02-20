# NewsSummarizer
### Project Name: **NewsSummarizer  📑📰**

### README File for **NewsSummarizer**

---

# NewsSummarizer 📑📰

**NewsSummarizer** is a Python-based application that scrapes news articles from Google News, cleans and summarizes them using OpenAI's GPT-4 model, and saves the summarized content for further use. The project combines **web scraping**, **data processing**, and **summarization** into an easy-to-use tool.

## Features ✨

- **Web Scraping**: Scrape news articles based on any user-defined topic using **Selenium** and **undetected-chromedriver**.
- **Article Summarization**: Summarizes each of the scraped news articles while retaining all key details, facts, and points.
- **Save Results**: The summarized content is saved to a `.txt` file and also serialized in a `.pkl` file for persistence.

## Requirements 📦

Before running the project, you need to install the following Python packages:

1. **Selenium**: For scraping news articles.
2. **Undetected-Chromedriver**: To avoid detection by Google.
3. **Langchain**: For interaction with the GPT model.
4. **Pickle**: For saving the scraped content.
5. **dotenv**: For handling environment variables.

To install the dependencies, run the following command:

```bash
pip install selenium undetected-chromedriver langchain langchain_openai webdriver-manager python-dotenv
```

## How It Works 🔧

1. **Step 1**: **Scraping News Articles** 📰  
   - The user inputs a search topic.
   - The script opens Google and searches for news related to the topic.
   - The first 5 news articles are scraped, and their content is stored in a list.

2. **Step 2**: **Summarizing Articles** ✂️  
   - Each article is sent to the GPT-4 model via **Langchain** for summarization.
   - The model summarizes the content while keeping all important details intact.

3. **Step 3**: **Saving Summaries** 💾  
   - The summarized content of all five articles is saved into a `.txt` file (`summary.txt`).
   - The scraped content is also serialized into a `.pkl` file (`scraped_articles.pkl`), which is useful for data persistence.

## How to Use 🚀

1. Clone the repository:

```bash
git clone https://github.com/yourusername/NewsSummarizer.git
cd NewsSummarizer
```

2. Run the script:

```bash
python news_summarizer.py
```

3. Enter the **topic** when prompted. For example:
   ```text
   Enter the topic to search for news: Technology
   ```

4. Once the articles are scraped and summarized, the summary will be written into a `summary.txt` file.

## Example Output 📑

Here's a sample of what the output might look like:

### **summary.txt**
```text
Title: AI Revolution in 2023
Content: This article discusses the rapid advancements in artificial intelligence in 2023. Key developments include...
...

Title: New Technology Trends to Watch
Content: The article covers the latest trends in technology for the coming year. Focus areas include the rise of machine learning...
...

... (More summarized articles)
```

### **scraped_articles.pkl**
This file contains the raw text data of all 5 articles in a serialized format, which you can load back for analysis or re-summarization.

## Project Structure 🗂

```
NewsSummarizer/
├── news_summarizer.py   # Main scraping and summarization script
├── summary.txt         # Output file containing the summarized articles
├── scraped_articles.pkl  # Serialized file with the raw scraped articles
├── .env                # Contains your OpenAI API key and other env variables
└── README.md           # This file
```

## Environment Variables 🌱

To use the OpenAI GPT-4 model, you'll need to create an `.env` file with the following content:

```
OPENAI_API_KEY=your-openai-api-key
```

Replace `your-openai-api-key` with your actual OpenAI API key.

## Contributing 🤝

We welcome contributions! If you'd like to help improve the project, please feel free to fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.



### Enjoy summarizing news with NewsSummarizer! 📰✨
