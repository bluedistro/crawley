from endpoint import endpoint

# execute
ep = endpoint(project_name='reddit', homepage='https://www.reddit.com/')
ep.create_workers()
ep.crawl()