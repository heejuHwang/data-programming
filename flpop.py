import pandas as pd
from bs4 import BeautifulSoup
import requests


startnumber=1
endnumber=1000
limit = 2000

Infor = {}
yearlist=[]
quatlist=[]
codelist = []
codenamelist = []
genderlist=[]
agrdelist = []
tmzonelist = []
daylist = []
flpop_list = []


def listing(soup):
    rows = soup.findAll('row')
    for row in rows:
        year = row.find('stdr_yy_cd')
        y = year.text
        yearlist.extend([y] *504)
        quat = row.find('stdr_qu_cd')
        q = quat.text
        quatlist.extend([q]*504)
        codenumber = row.find('trdar_cd')
        cn = codenumber.text
        codelist.extend([cn]*504)
        codename = row.find('trdar_cd_nm')
        cnm = codename.text
        codenamelist.extend([cnm]*504)
        for a in ['10', '20', '30', '40', '50','60_above']:
            for d in ['mon','tue','wed','thu','fri','sat','sun']:
                for t in ['1','2','3','4','5','6']:
                    globals()['m{age}_{day}_{tm}'.format(age = a,day=d, tm=t)] = row.find(('mag_{age}_{day}tm_{tm}_flpop_co').format(age=a, day=d, tm=t))
                    genderlist.append('m')
                    if a=='60_above':
                        agrdelist.extend(['above60']*2)
                    else:
                        agrdelist.extend([a+'s']*2)

                    if t=='1':
                        tmzonelist.extend(['00to06']*2)
                    elif t=='2':
                        tmzonelist.extend(['06to11']*2)
                    elif t=='3':
                        tmzonelist.extend(['11to14']*2)
                    elif t=='4':
                        tmzonelist.extend(['14to17']*2)
                    elif t=='5':
                        tmzonelist.extend(['17to21']*2)
                    elif t=='6':
                        tmzonelist.extend(['21to24']*2)
                    daylist.extend([d]*2)
                    flpop_list.append(globals()['m{age}_{day}_{tm}'.format(age = a,day=d, tm=t)].text)
                    globals()['f{age}_{day}_{tm}'.format(age = a,day=d, tm=t)] = row.find(('fag_{age}_{day}tm_{tm}_flpop_co').format(age=a, day=d, tm=t))
                    genderlist.append('f')
                    flpop_list.append(globals()['f{age}_{day}_{tm}'.format(age = a,day=d, tm=t)].text)



while endnumber<=limit:
    url='http://openapi.seoul.go.kr:8088/4a685a454f68686a31303167706c6871/xml/VwsmTrdarFlpopQq/'+str(startnumber)+'/'+str(endnumber)+'/'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    l = soup.find('list_total_count').text
    limit = int(l)

    listing(soup)

    startnumber+=1000
    endnumber+=1000


url='http://openapi.seoul.go.kr:8088/4a685a454f68686a31303167706c6871/xml/VwsmTrdarFlpopQq/'+str(startnumber)+'/'+str(limit)+'/'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

listing(soup)


Infor['year'] = yearlist
Infor['quater'] = quatlist
Infor['code'] = codelist
Infor['name'] = codenamelist
Infor['gender'] = genderlist
Infor['agrde'] = agrdelist
Infor['tmzon'] = tmzonelist
Infor['day'] = daylist
Infor['flpop'] = flpop_list



df = pd.DataFrame(Infor)
df.to_csv("flpop_small.csv", header=True)