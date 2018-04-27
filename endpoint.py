import threading
from queue import Queue
from spyder import spider
from domain import *
from general import *


class endpoint:

    def __init__(self, project_name='geo_gis', prefix='http://www.', site=None, thread_num=12):
        '''

        :param project_name: dir name of the site to crawl
        :param homepage: the homepage url of the site to be crawled
        :param thread_num: number of threads to undertake the job
        '''

        self.PROJECT_NAME = project_name
        self.HOMEPAGE = site
        # self.HOMEPAGE = prefix+site
        self.DOMAIN_NAME = get_domain_name(self.HOMEPAGE)
        self.QUEUE_FILE = self.PROJECT_NAME+'/queue.txt'
        self.CRAWLED_FILE = self.PROJECT_NAME+'/crawled.txt'
        self.NUMBER_OF_THREADS = thread_num
        self.queue = Queue()
        print('DOMAIN NAME')
        print(self.DOMAIN_NAME)
        print('HOME PAGE')
        print(self.HOMEPAGE)
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
        crawled_links = file_to_set(self.CRAWLED_FILE)
        if len(queued_links) > 0 and len(crawled_links) < 100:
            print('Available number of links: {}'.format(str(len(queued_links))))
            self.create_jobs()
        else:
            return None

    # def crawl(self):
    #     queued_links = file_to_set(self.QUEUE_FILE)
    #     thefile = open(self.CRAWLED_FILE, 'r')
    #     result = set()
    #     thefile.seek(0, 2)
    #     while True:
    #         line = thefile.readline()
    #         result.add(line.replace('\n', ''))
    #         if len(result) < 50 and len(queued_links) > 0:
    #             print('Available number of links: {}'.format(str(len(queued_links))))
    #             self.create_jobs()
    #         else:
    #             print('End')
    #             return None



    # def limit_check(self):
    #     crawled_links = file_to_set(self.CRAWLED_FILE)
    #     if len(crawled_links) < 300:
    #         self.crawl()
    #     else:
    #         return
