'''

Usage: %run test_04.py -s '07012018' -e '09012018' -c 100

'''

from tokens import SNOWFLAKE_USERNAME, SNOWFLAKE_PASSWORD, SNOWFLAKE_URL_BASE
import requests
from requests.auth import HTTPBasicAuth
import time
from pprint import pprint
from datetime import datetime
import tzlocal  # $ pip install tzlocal
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import argparse
import seaborn as sns

parser=argparse.ArgumentParser()

parser.add_argument('--start', '-s', default='06012018', type=str, help='Start Time')
parser.add_argument('--end', '-e', default='09012018', type=str, help='End Time')
parser.add_argument('--count', '-c', default=50, type=int, help='Number of steps')

args=parser.parse_args()

start = args.start
end = args.end
steps = args.count

start_time  = time.mktime(datetime.strptime(start, "%m%d%Y").timetuple())
end_time  = time.mktime(datetime.strptime(end, "%m%d%Y").timetuple())

#URL_BASE = 'http://127.0.0.1'
URL_ADD1 = '/api/price/'+str(int(start_time))+'/'+str(int(end_time))+'/'+str(steps)+'/ETHUSD.json'
URL_ADD2 = '/api/price/'+str(int(start_time))+'/'+str(int(end_time))+'/'+str(steps)+'/BTCUSD.json'
print(URL_ADD1, URL_ADD2)

r1 = requests.get(SNOWFLAKE_URL_BASE+URL_ADD1, auth=HTTPBasicAuth(SNOWFLAKE_USERNAME, SNOWFLAKE_PASSWORD))
pprint(r1.json())

r2 = requests.get(SNOWFLAKE_URL_BASE+URL_ADD2, auth=HTTPBasicAuth(SNOWFLAKE_USERNAME, SNOWFLAKE_PASSWORD))
pprint(r2.json())

timeval = []
ETHval = []
BTCval = []
for item in r1.json():
	unix_timestamp = float(item['date'])
	local_timezone = tzlocal.get_localzone() # get pytz timezone
	local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
	print(local_time, item['price'])
	timeval.append(local_time)
	ETHval.append(item['price'])

for item in r2.json():
	unix_timestamp = float(item['date'])
	local_timezone = tzlocal.get_localzone() # get pytz timezone
	local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
	print(local_time, item['price'])
	BTCval.append(item['price'])

plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
plt.plot(timeval, np.array(ETHval)/ETHval[0], label='ETH scale')
plt.plot(timeval, np.array(BTCval)/BTCval[0], 'r', label='BTC scale')
plt.plot(timeval, np.divide(np.array(BTCval)/BTCval[0], np.array(ETHval)/ETHval[0]), 'g', label='BTC/ETH scale')
plt.gcf().autofmt_xdate()
plt.xticks(rotation=90)
plt.xlabel('DateTime')
plt.ylabel('Ratio')
plt.legend(loc='upper left')
plt.show()







