# import socket, pygeoip
#
# ip = (socket.gethostbyname('www.google.com'))
# GEOIP = pygeoip.GeoIP("GeoIP.dat", pygeoip.MEMORY_CACHE)
# print GEOIP.country_name_by_addr(ip)

import argparse
parser = argparse.ArgumentParser(description='Helping you...')
parser.add_argument('-N','--name',required='True', default='Kingsley',
                    help='Input name')
parser.add_argument('-A', '--age', default='15',
                    help='Input age')
parser.add_argument('-C', '--course', default='CPEN')
args = parser.parse_args()
print(args.name)

