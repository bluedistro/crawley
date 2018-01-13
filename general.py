import os

def create_project_directory(directory):
    '''

    :param directory: make a directory for the links from the page to be crawled
    :return:
    '''
    if not os.path.exists(directory):
        print('creating project: {}'.format(directory))
        os.makedirs(directory)
    else:
        print('Project exists!')

# for each crawling done, there is the queued and the crawled files only

# create queued and crawled files (if not created)
# base_url is the homepage
def create_data_files(project_name, base_url):
    '''

    :param project_name: name of the project
    :param base_url: home url of the site to be crawled
    :return:
    '''
    queue_ext = 'queue.txt'
    queue = os.path.join(project_name, queue_ext)
    crawled_ext = 'crawled.txt'
    crawled = os.path.join(project_name, crawled_ext)

    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# create a new file
def write_file(path, data):
    '''

    :param path: path to the location where the file will be written
    :param data: data to be written to the file
    :return:
    '''
    f = open(path, 'w')
    f.write(data)
    f.close()

# Add data onto existing file
def append_to_file(path, data):
    '''

    :param path: path to the location where the file will be written
    :param data: data to be written to the file
    :return:
    '''
    with open(path, 'a') as file:
        file.write(data + '\n')


# delete contents of a file
def delete_file_contents(path):
    '''

    :param path:  replace the file with a newly created file of the same name ( .equals() delete aint it?,
     but faster)
    :return:
    '''
    with open(path, 'w'):
        pass

# Read a file and convert to set
def file_to_set(file_name):
    '''

    :param file_name: the file to be read from
    :return:
    '''
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# convert set items to file as new lines
def set_to_file(links, file_name):
    '''

    :param links: links to be sent from the set data type to the file
    :param file_name: the file in which the data will be stored
    :return:
    '''
    delete_file_contents(file_name)
    for link in sorted(links):
        append_to_file(file_name, link)

