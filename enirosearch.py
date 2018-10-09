import requests
from bs4 import BeautifulSoup
import mysql.connector
requests.packages.urllib3.disable_warnings()
cnx = mysql.connector.connect(
    user='mysqluser', database='mysqldatabase', password='mysqlpass',  host='mysqlip')
cursor = cnx.cursor()
totalcount = 0


def addstoreinfo(data_store):
    add_store = ("INSERT IGNORE INTO finalstoreinfo "
             "(name,website,phone,orgnumber,street,postcode,postarea,price,cord)"
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    
    cursor.execute(add_store, data_store)

def addpriceinfo(data_store):
    add_store = ("INSERT IGNORE INTO prices "
             "(id,klippning)"
             "VALUES (%s, %s)")
    
    cursor.execute(add_store, data_store)

def getsurlfromjson(jsontoget):

    hemsidor = []
    
    
    for advert in jsontoget['adverts']:
        # print(advert)
        totalcount =+ 1
        
        hemsida = advert['homepage']
        asd = str(hemsida)
        if asd != 'None':
            # print(advert['companyInfo']['companyName'])
            hemsidor.append(asd)
        else:
            asd = 'https://blankslate.io/'
            hemsidor.append(asd)

    return hemsidor
def getnamefromjson(jsontoget):
    namn = []

    for advert in jsontoget['adverts']:
        # print(advert)
        namne = advert['companyInfo']['companyName']
        asd = str(namne)
        if asd != 'None':

            namn.append(asd)
        else:
            asd = 'https://blankslate.io/'
            namn.append(asd)

    return namn
def getorgnumberfromjson(jsontoget):
    namn = []

    for advert in jsontoget['adverts']:
        # print(advert)
        namne = advert['companyInfo']['orgNumber']
        asd = str(namne)
        if asd != 'None':

            namn.append(asd)
        else:
            asd = 'https://blankslate.io/'
            namn.append(asd)

    return namn
def getphonefromjson(jsontoget):
    namn = []

    for advert in jsontoget['adverts']:
        # print(advert)
        namne = advert['phoneNumbers']
        asd = str(namne)
        if asd != 'None':

            namn.append(asd)
        else:
            asd = 'https://blankslate.io/'
            namn.append(asd)

    return namn
def getstreetfromjson(jsontoget):
    namn = []

    for advert in jsontoget['adverts']:
        # print(advert)
        namne = advert['address']['streetName']
        asd = str(namne)
        if asd != 'None':

            namn.append(asd)
        else:
            asd = 'https://blankslate.io/'
            namn.append(asd)

    return namn
def getpostalcodefromjson(jsontoget):
    namn = []

    for advert in jsontoget['adverts']:
        # print(advert)
        namne = advert['address']['postCode']
        asd = str(namne)
        if asd != 'None':

            namn.append(asd)
        else:
            asd = 'https://blankslate.io/'
            namn.append(asd)

    return namn
def getareafromjson(jsontoget):
    namn = []

    for advert in jsontoget['adverts']:
        # print(advert)
        namne = advert['address']['postArea']
        asd = str(namne)
        if asd != 'None':

            namn.append(asd)
        else:
            asd = 'https://blankslate.io/'
            namn.append(asd)

    return namn
def getphonefromjson(jsontoget):
    namn = []

    for advert in jsontoget['adverts']:
        # print(advert)
        namne = advert['phoneNumbers']
        asd = str(namne)
        if asd != 'None':

            namn.append(asd)
        else:
            asd = 'https://blankslate.io/'
            namn.append(asd)

    return namn
def getcordfromjson(jsontoget):
    namn = []

    for advert in jsontoget['adverts']:
        # print(advert)
        namne = advert['location']['coordinates']
        asd = str(namne)
        if asd != 'None':

            namn.append(asd)
        else:
            asd = 'https://blankslate.io/'
            namn.append(asd)

    return namn
def loopsapiget(page):

    multi = page*25
    mutli2 = page+1
    start = 1 * multi
    end = 25 * mutli2
    if start == 0:
        start = 1

    a = str(start)
    b = str(end)

    res = requests.get(
        'https://api.eniro.com/cs/search/basic?profile=stenstensten&key=eniroapikey&country=se&version=1.1.3&search_word=fris%C3%B6r&geo_area=medelpad&from_list='+a+'&to_list='+b
        )
    (true, false, null) = (True, False, None)
    json = eval(res.text)
    enirourls = getsurlfromjson(json)
  
  


    forloopvar = 0
    # here the eniroapi goes to websites and gather storedata
    for link in enirourls:
        
        url_link = eniroproxietourl(str(link))

        url_stuff = urltolinkarray(str(url_link))
        print(url_link)
        
        for asdasdd in url_stuff:
            print(cursor.lastrowid)
            urltotext(str(url_stuff[asdasdd]),json,forloopvar)
        forloopvar = forloopvar +1



    return json
def pagestorender(pages):
    for x in range(pages):
        a = loopsapiget(x)
def eniroproxietourl(enirourl):
    # res= requests.get('http://api.eniro.com/proxy/homepage/uANwPf5aVK2QIcBQafSBkgv6qwgIm2zXgibaR_Npfo78YJ08iCkbkPfCWOj3bdmwTOph139rvZM=')
    res = requests.get(enirourl)

    soup = BeautifulSoup(res.text, 'html.parser')

    poop = str(soup.find_all('meta'))
    website = ''
    i = 0
    var1 = 22
    var2 = ''
    find_http = poop.find('www')

    while var1 != 100:

        var2 = poop[var1]
        var1 = var1 + 1
        if(var2 != '"'):
            website = website + str(var2)
        if(var2 == '"'):
            var1 = 100

    if(find_http == -1):
        website = '0'

    return website
def urltolinkarray(urltotextify):
    urls = {}
    counter = 0
    res = ''
    try:
        res = requests.get(urltotextify, verify=False)

    except:
        res = requests.get('https://blankslate.io/', verify=False)

    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.find_all('a'):
        adddd = str(link.get('href'))
        find_http = adddd.find('http')
        if(find_http == -1):
            adddd = 'https://blankslate.io/'

        urls[counter] = adddd
        counter = counter+1

    return urls
def textifystring(text):
    text = text.lower()
    newtext = ''
    validLetters = "abcdefghijklmnopqrstuvwxyzåäö1234567890 :-"
    for char in text:
        if char in validLetters:
            newtext += char

    return newtext
def numberifystring(text):
    newtext = ''
    validLetters = "1234567890"
    for char in text:
        if char in validLetters:
            newtext += char
    return newtext
# returns all text of a html
# and searches for all tags and number after
def urltotext(urltotextify,json,forloopvar):
    
    urls = ''
    res = ''
    try:
        res = requests.get(urltotextify, verify=False)
    except:
        res = requests.get('https://blankslate.io/', verify=False)

    soup = BeautifulSoup(res.text, 'html.parser')

    for para in soup.find_all('p'):
        urls = urls + str(para)
    for para in soup.find_all('li'):
        urls = urls + str(para)

    urls = textifystring(urls)

    def pricekeywordfind(string):
        keywords = ['kr', ':-']
        keywords2 = ['klipp']

        for key in keywords:
            a = 0
            b = False

            while b == False:
                number = ''
                c = string.find(str(key), int(a+1))
                a = c

                if c == -1:
                    b = True
                else:
                    d = c - 6
                    if d < 0:
                        d = 0

                    while c > d:

                        if string[d] == '1':
                            number = number + '1'
                        if string[d] == '2':
                            number = number + '2'

                        if string[d] == '3':
                            number = number + '3'

                        if string[d] == '4':
                            number = number + '4'

                        if string[d] == '5':
                            number = number + '5'

                        if string[d] == '6':
                            number = number + '6'

                        if string[d] == '7':

                            number = number + '7'

                        if string[d] == '8':
                            number = number + '8'

                        if string[d] == '9':
                            number = number + '9'

                        if string[d] == '0':
                            number = number + '0'

                        d = d + 1
                    number2 = numberifystring(number)
                    #print(' ending and price',c,number)
                    asdd = -1
                    asdd2 = len(number2)
                    if asdd2 > 0:
                        asdd = int(number2)

                    if asdd > 0:

                        da = c - 40
                        if da < 0:
                            da = 0
                        if c < 0:
                            c = 0
                        db = c
                        for key2 in keywords2:

                            dc = string.find(key2, da, c)
                            print(dc, number)
                            if dc != -1:
                                dsad = getsurlfromjson(json)[forloopvar]
                                dsad = eniroproxietourl(dsad)
                                data1_store = (getnamefromjson(json)[forloopvar],dsad, getphonefromjson(json)[forloopvar], getorgnumberfromjson(json)[forloopvar], getstreetfromjson(json)[forloopvar],
                                getpostalcodefromjson(json)[forloopvar], getareafromjson(json)[forloopvar],asdd,getcordfromjson(json)[forloopvar])
                                print(data1_store)
                                addstoreinfo(data1_store)

    pricekeywordfind(urls)
    #pricekeywordfind('  klippning 1000kr')
    # print(urls)
    # keywordtxtfind(str(urls))
    return urls
# print(keywordtxtfind(asd))
# urltofunc(eniroproxietourl('http://api.eniro.com/proxy/homepage/uANwPf5aVK2QIcBQafSBkgv6qwgIm2zXgibaR_Npfo78YJ08iCkbkPfCWOj3bdmwTOph139rvZM='))
# eniroproxietourl('http://api.eniro.com/proxy/homepage/uANwPf5aVK2QIcBQafSBkgv6qwgIm2zXgibaR_Npfo78YJ08iCkbkPfCWOj3bdmwTOph139rvZM=')
pagestorender(1000)
# urltotext('https://www.harlinjen.nu/prislista/')
#addstoreinfo(data1_store)

    

cnx.commit()
cursor.close()
cnx.close()
print('done')
# methods
#urll = 'http://www.air90suk.info/'
#res = requests.get(urll,verify=False)
