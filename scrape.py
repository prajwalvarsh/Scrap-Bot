import selenium.webdriver as webdriver
import time
import streamlit as st
from bs4 import BeautifulSoup


def scrape_site():
    print("Launching Firefox....")

    driver = None
    try:
        driver = webdriver.Firefox()
        # browser = webdriver.Firefox(firefox_binary=binary,executable_path='./geckodriver.exe')
    except Exception as e:
        print("Driver Error {e}")
    return driver

def getDriver(site, driver):
    html = None
    print("Launching getDriver ....")
    try:
        driver.get(site)
        print("Page loaded...")
        html = driver.page_source
        # time.sleep(10)
        # print(f"An error an occurred: ")
        return html
    except:
        # Code that runs if that specific exception occurs
        # print(f"An error occurred:")
        return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
    
    
    
# # class MySpider(scrapy.Spider):
# #     name = 'myspider'
    
# #     def __init__(self, url=None, *args, **kwargs):
# #         super(MySpider, self).__init__(*args, **kwargs)
# #         self.start_urls = [url]
    
# #     def parse(self, response):
# #         page_content = response.body.decode('utf-8')  # Get HTML of the page
# #         self.html_content = page_content

# # def run_scrapy_spider(site):
# #     process = CrawlerProcess(get_project_settings())
    
# #     # Create a spider instance with the provided URL
# #     spider = MySpider(site)
# #     process.crawl(spider)
    
# #     # Start the crawling process
# #     process.start()
    
# #     return spider.html_content

# # st.title("Scrape Bot")
# # url = st.text_input("Enter URL: ")

# # if st.button("scrape URL"):
# #     st.write("Scraping URL")
# #     # result = scrape_site()
# #     # driverResult = getDriver(url)
# #     driverResult =  run_scrapy_spider(url)
# #     print(driverResult)

# class MySpider(scrapy.Spider):
#     name = 'myspider'
    
#     def __init__(self, url=None, *args, **kwargs):
#         super(MySpider, self).__init__(*args, **kwargs)
#         self.start_urls = [url]
#         self.html_content = None

#     def parse(self, response):
#         page_content = response.body.decode('utf-8')  # Get HTML of the page
#         self.html_content = page_content

# # Function to run the Scrapy spider and return the HTML data
# def run_scrapy_spider(url):
#     settings = get_project_settings()
#     process = CrawlerProcess(settings)

#     # Store the spider's output in a dictionary
#     output = {}
    
#     def catch_item(signal, sender, item, response, spider):
#         output['html'] = spider.html_content

#     # Connect a signal to capture the scraped data once done
#     dispatcher.connect(catch_item, signal=signals.item_scraped)
    
#     # Run the spider and pass the URL
#     process.crawl(MySpider, url=url)
#     process.start()  # the script will block here until the spider finishes

#     return output.get('html')

# # Streamlit app
# st.title("Web Scraper using Scrapy and Streamlit")

# # Input: User provides a URL
# url = st.text_input("Enter the URL to scrape")

# if st.button("Scrape"):
#     if url:
#         # Call the function to run the Scrapy spider
#         with st.spinner("Scraping in progress..."):
#             try:
#                 html_data = run_scrapy_spider(url)
#                 if html_data:
#                     st.code(html_data, language='html')  # Display the HTML content
#                 else:
#                     st.warning("Failed to retrieve the HTML content.")
#             except Exception as e:
#                 st.error(f"Error occurred: {e}")
#     else:
#         st.warning("Please enter a valid URL.")

# import streamlit as st
# import scrapy
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy.crawler import CrawlerRunner
# from twisted.internet import reactor
# from scrapy import signals
# import json
# from scrapy.http import HtmlResponse

# # Define the Scrapy spider
# class HtmlSpider(scrapy.Spider):
#     name = "html_spider"
#     start_urls = []

#     def __init__(self, urls=None, *args, **kwargs):
#         super(HtmlSpider, self).__init__(*args, **kwargs)
#         if urls:
#             self.start_urls = urls.split(',')

#     def parse(self, response):
#         yield {'url': response.url, 'html': response.text}

# # Function to run Scrapy
# def run_scrapy(urls):
#     process = CrawlerProcess(get_project_settings())
#     results = []
#     # results = process.crawler.stats.get_value('finish_reason')

#     # runner = CrawlerRunner(get_project_settings())
#     # d = runner.crawl(HtmlSpider, urls=urls)
#     # d.addBoth(lambda _: reactor.stop())
#     # reactor.run()
#     crawler = process.create_crawler()
#     spider = crawler.spiders.create(spname, **opts.spargs)
#     results = crawler.crawl(spider)
#     process.start()
#     return results

# # Streamlit UI
# def main():
#     st.title("Webpage Crawler")

#     urls = st.text_input("Enter URLs (comma-separated)", "")

#     if st.button("Crawl"):
#         if urls:
#             with st.spinner("Crawling..."):
#                 results = run_scrapy(urls)
#                 st.write("Crawled Data:")
#                 for result in results:
#                     st.write(result['url'])
#                     st.write(result['html'])
#         else:
#             st.warning("Please enter some URLs")

# if __name__ == "__main__":
#     main()

