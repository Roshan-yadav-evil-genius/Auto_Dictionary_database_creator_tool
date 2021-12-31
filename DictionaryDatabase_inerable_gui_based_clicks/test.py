import sqlite3
from translate3 import Translator
from bs4 import BeautifulSoup
import requests


conn = sqlite3.connect('Dictionary.db')
c = conn.cursor()
c.execute('SELECT `key`, valueHin FROM Dictionary')
data = c.fetchall()
error = "WARNING: YOU USED ALL AVAILABLE FREE TRANSLATIONS FOR TODAY. NEXT AVAILABLE IN  14 HOURS 54 MINUTES 39 SECONDSVISIT HTTPS://MYMEMORY.TRANSLATED.NET/DOC/USAGELIMITS.PHP TO TRANSLATE MORE"
proxylist = []


def getProxies():
    url = "https://free-proxy-list.net/"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for x in soup.find("tbody").findAll("tr"):
        details = x.findAll("td")
        host, port, https = details[0].text, details[1].text, details[6].text
        if https == "yes":
            ipAdd = host+":"+port
            proxylist.append(ipAdd)


getProxies()


def hindi(english):
    for ipAdd in proxylist:
        try:
            translator = Translator(to_lang="Hindi", proxy=ipAdd)
            hindi = translator.translate(f"{x[0]}")
            if error in hindi:
                getProxies()
            print(hindi)
        except:
            pass


for x in data:
    if x[1] == None or x[1] == 'None':
        hindi(x[0])
