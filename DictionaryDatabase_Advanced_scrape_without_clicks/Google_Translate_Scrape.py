from datetime import date, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from custom_function import alphabate
import threading
import requests
import json
import time

data = requests.get(
    "https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json").text
data = json.loads(data)

ChromeDriver = "./chromedriver.exe"
url = "https://translate.google.co.in/?sl=en&tl=hi"

ser = Service(ChromeDriver)
op = webdriver.ChromeOptions()
# op.add_argument("--headless")
op.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=ser, options=op)

driver.get(url)

textarea = ''
hindi = ''


def getbox():
    global textarea
    global hindi
    try:
        time.sleep(1)
        textarea = driver.find_element(
            By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
        hindi = driver.find_element(
            By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]')
    except:
        getbox()


PreviousData = ""
error = False
notdefine = 0


def getTranslation():
    global PreviousData
    global notdefine
    for x in data:
        try:
            time.sleep(.5)
            textarea.clear()
            textarea.send_keys(x)
            same = True
            i = 0
            while error:
                pass
            while same:
                time.sleep(.5)
                htext = hindi.text.split("\n")[0]
                if len(htext) > 0:
                    if not alphabate(htext):
                        if htext != PreviousData:
                            PreviousData = htext
                            same = False
                            print(x, htext)
                    i += 1
                    if i > 10:
                        same = False
                        print(x, "not defined")
                        notdefine += 1
                        if notdefine > 1:
                            print("wait")
                            time.sleep(50)
                            notdefine = 0
        except:
            print(x, "not defined except")
            getbox()
            time.sleep(10)


def getError():
    global error
    while True:
        print('Error', end=' ')
        try:
            TryAgain = driver.find_element(
                By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[5]/div[2]/button')
            if TryAgain.is_displayed():
                print('Found')
                error = True
                time.sleep(10)
                print("clicked")
                TryAgain.click()
                error = False
            else:
                print("Not Found 1")

        except:
            print('Not Found 2')
        time.sleep(10)


t1 = threading.Thread(target=getTranslation)
t2 = threading.Thread(target=getError)
t1.start()
t2.start()
t1.join()
t2.join()
driver.quit()
