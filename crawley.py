# TODO: EMPTY THE CRAWLED AND QUEUED FILES AFTER EVERY SUCCESSFUL SEARCH/CRAWL
from endpoint import endpoint
import argparse, os, json
from flask import Flask, request
from random import randint
import requests, time, socket
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = str(randint(1000, 10000))

# Testing argument parsing

# parser = argparse.ArgumentParser(description='Enter a web project and the site to crawl')
# parser.add_argument('-P', '--project', required='True', default='youtube',
#                     help='name of project directory')
# parser.add_argument('-W', '--website', required='True', default='youtube.com',
#                     help='website url ignoring the domain prefix')
# parser.add_argument('-H', '--http', required='True', default='https://www.',
#                     help='domain prefix')
# args = parser.parse_args()


# Until a new request is sent to it, the crawler continues to crawl the internet saaaaa :)
# A non-stopping crawler
# @app.route('/api/start_crawler', methods=['GET', 'POST'])
# def start_crawler():
#     if request.method == 'POST':
#         content = request.get_json(force=True, silent=True)
#         theurl = str(content['url'])
#         # open the crawled and queued files and delete the already crawled files
#         crawledFilePath = os.path.join('geo_gis', 'crawled.txt')
#         with open(crawledFilePath, 'w'):
#             pass
#
#         # open the crawled and queued files and delete the already crawled files
#         queuedFilePath = os.path.join('geo_gis', 'queue.txt')
#         with open(queuedFilePath, 'w'):
#             pass
#
#         beginCrawl = endpoint(project_name='geo_gis', site=theurl)
#         beginCrawl.create_workers()
#         beginCrawl.crawl()
#
#         return None


# @app.route('/api/fetch_data', methods=['GET'])
# def fetch_data():
#
#     # open the crawled.txt, read the content into a list line-wise, and until the length is greater
#     # than a particular random seed, loop
#
#     crawledData = os.path.join('geo_gis', 'crawled.txt')
#     results = []
#     size_checker = 0
#     # time.sleep(10)
#     while size_checker < 10:
#         with open(crawledData, 'rt') as f:
#             for line in f:
#                 results.append(line.replace('\n', ''))
#         size_checker += len(results)
#         print('Size checker: {}'.format(size_checker))
#     message = {
#         'data': results
#     }
#
#     return json.dumps(message)


# endpoint linking to the frontend
@app.route('/api/url', methods=['GET', 'POST'])
def url():
    if request.method == 'POST':
        content = request.get_json(force=True, silent=True)
        theurl = str(content['url'])
        sites = endpoint(project_name='geo_gis', homepage=theurl)
        sites.create_workers()
        sites.crawl()
        thefile = os.path.join('geo_gis', 'crawled.txt')
        results = list()
        with open(thefile, 'rt') as f:
            for line in f:
                results.append(line.replace('\n', ''))
        message = {
            'data' : results
        }
        return json.dumps(message)
    
# command line endpoint test
@app.route('/api/crawler-test/<string:output_dir>')
def test(output_dir):
    # test url startpoint
    url = "https://news.ycombinator.com"
    sites = endpoint(project_name=output_dir, homepage=url)
    sites.create_workers()
    sites.crawl()
    saved_files = os.path.join(dir, 'crawled.txt')
    results = list()
    with open(saved_files, 'rt') as f:
        for line in f:
            results.append(line.replace('\n', ''))
    message = {
        'results': results
    }

    return json.dumps(message)

# receives a list of all the urls and for each and every one of them, returns the ip information back
# as a json key -> value (list) form
@app.route('/api/get_url_info', methods=['GET', 'POST'])
def get_url_info():
    content = request.get_json(force=True, silent=True)
    url_list = content['url_list']
    ip_list = []
    url_info = []
    # get the ip of each and every one of them into a list
    for url in url_list:
        # get the main domain of the website from the "https://example.com/other/examples" format,
        # get the IP address of that website and append the ip address to the ip_list list
        ip_list.append(socket.gethostbyname(url))
        # ip_list.append(socket.gethostbyname(url.split('/')[2]))
    # get the information of the url and append it to the url_info list
    for ip in ip_list:
        url_info.append(requests.get('http://ipinfo.io/'+ip).json())
    # store the list in json format and return
    message = {
        'url_info' : url_info
    }

    return json.dumps(message)



if __name__=="__main__":
    app.run(port=8100)

# execute
# ep = endpoint(project_name=args.project, site=args.website, prefix=args.http)
# ep.create_workers()
# ep.crawl()

