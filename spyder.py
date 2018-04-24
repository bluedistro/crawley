# TODO: Domain Movement Restrictions is performed in this script

from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class spider:

    # class variables shared among all instances
    project_name = ''
    base_url = ''
    domain_name = ''
    queued_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        spider.project_name = project_name
        spider.base_url = base_url
        spider.domain_name = domain_name
        spider.queued_file = spider.project_name+'/queue.txt'
        spider.crawled_file = spider.project_name+'/crawled.txt'
        self.boot()
        self.crawl_page('spider 1', spider.base_url)

    @staticmethod
    def boot():
        create_project_directory(spider.project_name)
        create_data_files(spider.project_name, spider.base_url)
        spider.queued = file_to_set(spider.queued_file)
        spider.crawled = file_to_set(spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queued: ' + str(len(spider.queue))  + ' | Crawled: ' + str(len(spider.crawled)))
            spider.add_links_to_queue(spider.gather_links(page_url))
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print('Error: cannot crawl page | check internet connection')
            print(str(e))
            return set()

        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in spider.queue:
                continue
            if url in spider.crawled:
                continue
            # TODO: Uncomment these lines to restrict the movement its movement within the domain
            # if spider.domain_name not in url:
            #     continue
            spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(spider.queue, spider.queued_file)
        set_to_file(spider.crawled, spider.crawled_file)



