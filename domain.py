from urllib.parse import urlparse


# get domain name(example.com)
def get_domain_name(url):
    '''

    :param url: url of the domain to crawl
    :return:
    '''
    try:

        results = get_subdomain_name(url).split('.')
        # TODO: Uncomment the lines commented below and above and
        # TODO: comment those uncommented to avoid pre-domain names example --
        # TODO: the (name) in => name.example.com
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
