from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        '''

        :param base_url: the initial url of the site to crawl
        :param page_url: the url of the current page of the site
        '''
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        '''

        :param tag: the html tags present on the web page
        :param attrs: the attributes available in the tag
        :return: returns the links crawled from the page
        '''
        if tag == 'a':
            for attribute, value in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links
