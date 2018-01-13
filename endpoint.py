import threading
from queue import Queue
from spyder import spider
from domain import *
from general import *


class endpoint:

    def __init__(self, project_name='hackernews', homepage='https://news.ycombinator.com', thread_num=8):
        '''

        :param project_name: dir name of the site to crawl
        :param homepage: the homepage url of the site to be crawled
        :param thread_num: number of threads to undertake the job
        '''

        self.PROJECT_NAME = project_name
        self.HOMEPAGE = homepage
        self.DOMAIN_NAME = get_domain_name(self.HOMEPAGE)
        self.QUEUE_FILE = self.PROJECT_NAME+'/queue.txt'
        self.CRAWLED_FILE = self.PROJECT_NAME+'/crawled.txt'
        self.NUMBER_OF_THREADS = thread_num
        self.queue = Queue()
        spider(self.PROJECT_NAME,self. HOMEPAGE, self.DOMAIN_NAME)

    # do the next job in the queue
    def work(self):
        while True:
            url = self.queue.get()
            spider.crawl_page(threading.current_thread().name, url)
            self.queue.task_done()

    # create worker threads-> dies when main exits
    def create_workers(self):
        for _ in range(self.NUMBER_OF_THREADS):
            t = threading.Thread(target=self.work)
            t.daemon = True
            t.start()

    #each queued link is a new job
    def create_jobs(self):
        for link in file_to_set(self.QUEUE_FILE):
            self.queue.put(link)
        self.queue.join()
        self.crawl()

    # look in todo list for items
    def crawl(self):
        queued_links = file_to_set(self.QUEUE_FILE)
        if len(queued_links) > 0:
            print('Available number of links: {}'.format(str(len(queued_links))))
            self.create_jobs()
