from urllib.parse import urlparse


# get domain name(example.com)
def get_domain_name(url):
    '''

    :param url: url of the domain to crawl
    :return:
    '''
    try:
        results = get_subdomain_name(url).split('.')
        cleaned_results = results[-2]+ '.' +results[-1]
        return cleaned_results
    except:
        return ''

# get subdomain name (name.example.com)
def get_subdomain_name(url):

    '''

    :param url: url of the domain to crawl
    :return:
    '''
    try:
        return urlparse(url).netloc
    except:
        return ''
