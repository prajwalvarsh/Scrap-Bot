Scrap-Bot is a Python-based web scraping tool enhanced with Natural Language Processing (NLP) and a user-friendly interface.
It utilizes Selenium for dynamic web content scraping, Streamlit for a visual front-end, and LangChain with the Ollama model for processing workflows.
The tool uses Requests and BeautifulSoup for static web data extraction, while Pandas structures the scraped data for further analysis or storage.

Python 3.x
Requests: For HTTP requests to fetch webpage content.

Selenium: For scraping dynamic web content.

Streamlit: Provides an interactive UI for running and visualizing the scraper.

BeautifulSoup (bs4): For HTML parsing and web data extraction.

Pandas: For structuring and manipulating the scraped data.

Logging: To track and maintain logs of scraping activities.

Regex: For pattern matching and data extraction.

Ollama Model: A language model used for NLP tasks like text summarization and content generation.

LangChain: For creating a chain of NLP tasks to automate complex scraping workflows.
    
pip install -r requirements.txt (for installing the dependencies) 

Start the Streamlit app, use the following command: streamlit run app.py
