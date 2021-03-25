from datetime import datetime
from datetime import timedelta
import time
from datetime import datetime
from pprint import pprint
import requests
from requests.models import Response

def get_stack():
    now = datetime.now()
    two_days = timedelta(2)
    before_yesterday = now - two_days
    now = str(time.mktime(now.timetuple()))
    now = now[0:10]
    before_yesterday = str(time.mktime(before_yesterday.timetuple()))
    before_yesterday = before_yesterday[0:10]
    url = 'https://api.stackexchange.com/2.2/search'
    params = {'fromdate': before_yesterday, 'todate': now, 'tagged': 'python', 'site': 'stackoverflow'}
    resp = requests.get(url, params=params).json()
    pprint(resp)

get_stack()