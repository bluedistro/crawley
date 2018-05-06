from nltk.corpus import stopwords
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

class engine:

    def __init__(self, search_words=None):
        self.search_words = search_words

    # get the words types individually
    def split_search_words(self, search_words=None):
        words_list = search_words.split(' ')
        # remove stop words
        filtered_words = [word.lower() for word in words_list if word not in stopwords.words('english')]
        return filtered_words

    # search indexed urls for links containing either or all words in filtered_words
    def search_indexed_urls(self, search_words=None):
        filtered_words = self.split_search_words(search_words=search_words)
        # open the file containing crawled urls
        index_urls = os.path.join('geo_gis', 'crawled.txt')
        results = []
        with open(index_urls, 'rt') as f:
            for line in f:

                # trying out the keyword checker
                try:
                    response = urlopen(line)
                    if 'text/html' in response.getheader('Content-Type'):
                        html_bytes = response.read()
                        html_string = html_bytes.decode('utf-8')
                        soup = BeautifulSoup(html_string)
                        text = soup.get_text().lower()
                        # searching_for = ['symbology encoding', 'styled layer descriptor']
                        for word in filtered_words:
                            if word in text:
                                print('Keyword {} found in url {}'.format(word, line))
                                results.append(line.replace('\n', ''))
                            else:
                                continue
                except Exception as e:
                    print('Engine search error!!!')
                    print(str(e))
        return results
                # end of trying out