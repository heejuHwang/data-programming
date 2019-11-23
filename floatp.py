import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

startnumber=1
endnumber=1000
limit = 2000

CommerceInfor = {}
yearlist=[]
quatlist=[]
codelist = []
codenamelist = []
totalnumberlist = []
maletotallist = []
femaletotallist = []
agrade_10list = []
agrade_20list = []
agrade_30list = []
agrade_40list = []
agrade_50list = []
above_60list = []
mon_list = []
tues_list = []
wed_list =[]
thur_list = []
fri_list = []
sat_list = []
sun_list = []

def listing(soup, sn, en):
    year = soup.findAll('stdr_yy_cd')
    quat = soup.findAll('stdr_qu_cd')
    codenumber = soup.findAll('trdar_cd')
    codename = soup.findAll('trdar_cd_nm')
    totalnumber = soup.findAll('tot_flpop_co')
    maletotal = soup.findAll('ml_flpop_co')
    femaletotal = soup.findAll('fml_flpop_co')
    agrade_10 = soup.findAll('agrde_10_flpop_co')
    agrade_20 = soup.findAll('agrde_20_flpop_co')
    agrade_30 = soup.findAll('agrde_30_flpop_co')
    agrade_40 = soup.findAll('agrde_40_flpop_co')
    agrade_50 = soup.findAll('agrde_50_flpop_co')
    above_60 = soup.findAll('agrde_60_above_flpop_co')
    mon = soup.findAll('mon_flpop_co')
    tues = soup.findAll('tues_flpop_co')
    wed = soup.findAll('wed_flpop_co')
    thur = soup.findAll('thur_flpop_co')
    fri = soup.findAll('fri_flpop_co')
    sat = soup.findAll('sat_flpop_co')
    sun = soup.findAll('sun_flpop_co')

    for code in year:
        yearlist.append(code.text)
    for code in quat:
        quatlist.append(code.text)
    for code in codenumber:
        codelist.append(code.text)
    for code in codename:
        codenamelist.append(code.text)
    for code in totalnumber:
        totalnumberlist.append(code.text)
    for code in maletotal:
        maletotallist.append(code.text)
    for code in femaletotal:
        femaletotallist.append(code.text)
    for code in agrade_10:
        agrade_10list.append(code.text)
    for code in agrade_20:
        agrade_20list.append(code.text)
    for code in agrade_30:
        agrade_30list.append(code.text)
    for code in agrade_40:
        agrade_40list.append(code.text)
    for code in agrade_50:
        agrade_50list.append(code.text)
    for code in above_60:
        above_60list.append(code.text)
    for code in mon:
        mon_list.append(code.text)
    for code in tues:
        tues_list.append(code.text)
    for code in wed:
       wed_list.append(code.text)
    for code in thur:
        thur_list.append(code.text)
    for code in fri:
        fri_list.append(code.text)
    for code in sat:
        sat_list.append(code.text)
    for code in sun:
        sun_list.append(code.text)


while endnumber<=1000:
    url='http://openapi.seoul.go.kr:8088/(ServiceKey)/xml/VwsmTrdarFlpopQq/'+str(startnumber)+'/'+str(endnumber)+'/'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    l = soup.find('list_total_count').text
    limit = int(l)
    print(limit)

    listing(soup, startnumber, endnumber)
    time.sleep(5)

    startnumber+=1000
    endnumber+=1000

url='http://openapi.seoul.go.kr:8088/(ServiceKey)/xml/VwsmTrdarFlpopQq/'+str(startnumber)+'/'+str(limit)+'/'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
listing(soup, startnumber, endnumber)




CommerceInfor['Year'] = yearlist
CommerceInfor['Quater'] = quatlist
CommerceInfor['Code'] = codelist
CommerceInfor['Name'] = codenamelist
CommerceInfor['Total Number'] = totalnumberlist
CommerceInfor['Male Total Number'] = maletotallist
CommerceInfor['Female Total Number'] = femaletotallist
CommerceInfor['Age 10s Number'] = agrade_10list
CommerceInfor['Age 20s Number'] = agrade_20list
CommerceInfor['Age 30s Number'] = agrade_30list
CommerceInfor['Age 40s Number'] = agrade_40list
CommerceInfor['Age 50s Number'] = agrade_50list
CommerceInfor['Age above 60s Number'] = above_60list
CommerceInfor['Monday'] = mon_list
CommerceInfor['Tuesday'] = tues_list
CommerceInfor['Wednesday'] = wed_list
CommerceInfor['Thursday'] = thur_list
CommerceInfor['Friday'] = fri_list
CommerceInfor['Saturday'] = sat_list
CommerceInfor['Sunday'] = sun_list


df = pd.DataFrame(CommerceInfor)
df.to_csv("flpop.csv", header=True)