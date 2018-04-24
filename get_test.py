# from random import randint
# from flask import Flask, request
#
# app = Flask(__name__)
# app.secret_key = str(randint(1000, 10000))
#
#
# @app.route('/get_test', methods=['GET', 'POST'])
# def get_test():
#     if request.method == 'POST':
#         content = request.get_json(force=True, silent=True)
#         result = str(content)
#         url = str(content.values())
#         print url
#         return result
#     elif request.method == 'GET':
#         return 'we will work on that'
#
#     return 'okay'
#


# if __name__ == '__main__':
#     app.run(port=8100)

# import os
#
# results = []
# file = os.path.join('geo_gis', 'crawled.txt')
# with open(file, 'rt') as f:
#     for line in f:
#         results.append(line.replace('\n', ''))
# print(results)


import socket, requests, json
url = 'https://news.ycombinator.com/from?site=aboutamazon.com'
url_2 = 'https://news.ycombinator.com/item?id=16894731'
url_3 = 'http://eskateboard.huu.la'
url_list = [url, url_2, url_3]
ip_list = []
url_info = []
# get the ip of each and every one of them into a list
for url in url_list:
    # get the main domain of the website from the "https://example.com/other/examples" format,
    # get the IP address of that website and append the ip address to the ip_list list
    ip_list.append(socket.gethostbyname(url.split('/')[2]))
# get the information of the url and append it to the url_info list
for ip in ip_list:
    url_info.append(requests.get('http://ipinfo.io/' + ip).json())
# store the list in json format and return
message = {
    'message' : url_info
}
print(json.dumps(message))

