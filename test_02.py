# http://www.umiacs.umd.edu/~jbg/docs/nips2009-rtl.pdf


from cryptopanic import CRYPTOPANIC_API_AUTH_TOKEN
import requests

URL_BASE = 'https://cryptopanic.com'
URL_ADD = '/api/posts/?auth_token='+CRYPTOPANIC_API_AUTH_TOKEN+'&currencies=EOS&filter=trending'

for number in range(3):
	URL_PAGE_NUMBER='&page='+str(number+1)
	URL = URL_BASE+URL_ADD+URL_PAGE_NUMBER
	r = requests.get(URL)
	# print(r.json())
	print
	content = r.json()['results']
	for index, item in enumerate(content):
		print(index, item['title'])
