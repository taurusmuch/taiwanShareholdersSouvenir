import requests;
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import datetime
import json

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
base_url='https://stock.wespai.com/'
startYear = 105
today = datetime.date.today()
endYear = today.year - 1911
result_data = {}
for i in range(startYear, endYear+1):

    page = base_url + 'stock' + str(i)
    res = requests.get(page, headers=headers)
    page = res.text

    doc = pq(page)
    lis = doc('tr')
    for tr in lis.items():
        #代號
        code = tr.find('td').eq(1).text()
        #公司
        company = tr.find('td').eq(2).text()
        #禮物
        present = tr.find('td').eq(5).text()
        if code != '':
            if code in result_data:
                # present_data = result_data[code]['present']
                # present_data.append(present)
                result_data[code]['present'][i] = present
            else:
                result_data[code] = {'company':company, 'present':{i:present}}

json = json.dumps(result_data)
print(json)

