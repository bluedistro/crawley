from general import *
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import re

class info_retriever:

    # init class
    def __init__(self, project_name=None, info_file_name=None):
        '''

        :param project_name: dir which contains the crawled/yet to be crawled info of the interested site
        :param info_file_name: preferred name to save the retrieved info
        '''

        self.project_name = project_name
        self.info_file_name = info_file_name
        self.read_links = set()

    # read all the links crawled from the page
    def get_all_links(self):
        crawled_file = 'crawled.txt'
        try:
            path = os.path.join(self.project_name, crawled_file)
        except Exception as e:
            print(str(e))

        with open(path, 'r') as links:
            for link in links:
                self.read_links.add(link.replace('\n', ''))
        return self.read_links


    # break link down to analyze keywords in the link (using regex), find interested urls based on keywords
    # and returns the url
    def analyze_link(self, target_words = []):

        '''

        :param target_words: the words of interest to arrive increase prob of getting into the desired page faster
        :return: urls with words of interest
        '''
        matched_urls = set()
        urls = self.get_all_links()
        for url in urls:
            url_words = re.compile(r'[\:/?=\-&]+', re.UNICODE).split(url)
            for t_word in target_words:
                for u_word in url_words:
                    if t_word.lower() == u_word.lower():
                        matched_urls.add(url)
        if len(matched_urls) == 0:
            return ('No related urls were found. Please try with different keywords')

        return matched_urls


    # open the webpage of the interested link and search through html tags to retrieve needed information
    def fetch_info(self, target_words = []):
        '''

        :param target_words: the words of interest to arrive increase prob of getting into the desired page faster
        :return:
        '''
        web_pages_url = self.analyze_link(target_words=target_words)
        for web_page_url in web_pages_url:
            html_doc = ''
            try:
                response = urlopen(web_page_url)
                if 'text/html' in response.getheader('Content-Type'):
                    html_bytes = response.read()
                    html_doc = html_bytes.decode('utf-8')
            except Exception as e:
                print(str(e))
            soup = BeautifulSoup(html_doc, 'html.parser')

            print(soup.get_text())

            import time
            time.sleep(10)

    # write all important information to a file created file and saved in the same project directory
    def save_info(self):
        pass



ir = info_retriever(project_name='reddit')
analinks = ir.analyze_link(target_words=['jackpot', 'million'])
print(analinks)

# fetch_infomation = ir.fetch_info()
# print(fetch_infomation)