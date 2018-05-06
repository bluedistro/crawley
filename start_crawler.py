from endpoint import endpoint


# spontaneously start the crawler to crawl for ever
try:
    sites = endpoint(project_name='geo_gis', site='http://www.opengeospatial.org/')
    sites.create_workers()
    sites.crawl()
except Exception as e:
    print(str(e))