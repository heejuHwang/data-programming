import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

startnumber=1
endnumber=1000
limit = 2000

Infor = {}
yearlist=[]
quatlist=[]
codelist = []
codenamelist = []
genderlist = []
agrdelist = []
repop_list = []

def listing(soup, sn, en):
    rows = soup.findAll('row')
    for row in rows:
        year = row.find('stdr_yy_cd')
        y = year.text
        quat = row.find('stdr_qu_cd')
        q = quat.text
        codenumber = row.find('trdar_cd')
        cn = codenumber.text
        codename = row.find('trdar_cd_nm')
        cnm = codename.text

        m_agrde_10 = row.find('mag_10_repop_co')
        m_agrde_20 = row.find('mag_20_repop_co')
        m_agrde_30 = row.find('mag_30_repop_co')
        m_agrde_40 = row.find('mag_40_repop_co')
        m_agrde_50 = row.find('mag_50_repop_co')
        m_above_60 = row.find('mag_60_above_repop_co')
        f_agrde_10 = row.find('fag_10_repop_co')
        f_agrde_20 = row.find('fag_20_repop_co')
        f_agrde_30 = row.find('fag_30_repop_co')
        f_agrde_40 = row.find('fag_40_repop_co')
        f_agrde_50 = row.find('fag_50_repop_co')
        f_above_60 = row.find('fag_60_above_repop_co')

        for i in range(12):
            yearlist.append(y)
            quatlist.append(q)
            codelist.append(cn)
            codenamelist.append(cnm)     
        for i in range(6):
            genderlist.append('m')
        for i in range(6):
            genderlist.append('f')        

        agrdelist.append('10s')
        repop_list.append(m_agrde_10.text)
            
        agrdelist.append('20s')
        repop_list.append(m_agrde_20.text)
            
        agrdelist.append('30s')
        repop_list.append(m_agrde_30.text)
            
        agrdelist.append('40s')
        repop_list.append(m_agrde_40.text)

        agrdelist.append('50s')
        repop_list.append(m_agrde_50.text)

        agrdelist.append('above60')
        repop_list.append(m_above_60.text)

        agrdelist.append('10s')
        repop_list.append(f_agrde_10.text)

        agrdelist.append('20s')
        repop_list.append(f_agrde_20.text)

        agrdelist.append('30s')
        repop_list.append(f_agrde_30.text)
            
        agrdelist.append('40s')
        repop_list.append(f_agrde_40.text)

        agrdelist.append('50s')
        repop_list.append(f_agrde_50.text)
            
        agrdelist.append('above60')
        repop_list.append(f_above_60.text)


while endnumber<=limit:
    url='http://openapi.seoul.go.kr:8088/4a685a454f68686a31303167706c6871/xml/VwsmTrdarRepopQq/'+str(startnumber)+'/'+str(endnumber)+'/'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    l = soup.find('list_total_count').text
    limit = int(l)

    listing(soup, startnumber, endnumber)
    time.sleep(2)

    startnumber+=1000
    endnumber+=1000

url='http://openapi.seoul.go.kr:8088/4a685a454f68686a31303167706c6871/xml/VwsmTrdarRepopQq/'+str(startnumber)+'/'+str(limit)+'/'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
listing(soup, startnumber, endnumber)




Infor['year'] = yearlist
Infor['quater'] = quatlist
Infor['code'] = codelist
Infor['name'] = codenamelist
Infor['gender'] = genderlist
Infor['agrde'] = agrdelist
Infor['repop'] = repop_list




df = pd.DataFrame(Infor)
df.to_csv("repop.csv", header=True)