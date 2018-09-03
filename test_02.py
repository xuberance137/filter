# http://www.umiacs.umd.edu/~jbg/docs/nips2009-rtl.pdf


from tokens import CRYPTOPANIC_API_AUTH_TOKEN
import requests
from pprint import pprint

URL_BASE = 'https://cryptopanic.com'
URL_ADD = '/api/posts/?auth_token='+CRYPTOPANIC_API_AUTH_TOKEN+'&currencies=ETH&filter=trending'

print
print 

for number in range(2):
	URL_PAGE_NUMBER='&page='+str(number+1)
	URL = URL_BASE+URL_ADD+URL_PAGE_NUMBER
	r = requests.get(URL)
	pprint(r.json())
	
	print
	content = r.json()['results']
	for index, item in enumerate(content):
		print(index, item['title'])
