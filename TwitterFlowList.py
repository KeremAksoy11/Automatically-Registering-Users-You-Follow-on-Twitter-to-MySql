from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import locale
from urllib3.packages.six import _import_module
locale.setlocale(locale.LC_ALL, 'turkish')
from bs4 import BeautifulSoup
import requests
import os
import csv
import pymysql.cursors
import pandas as pd
from bs4 import BeautifulSoup
import pyautogui



connection = pymysql.connect(host='', user='root',password='',database='sakila',cursorclass=pymysql.cursors.DictCursor)
mycursor = connection.cursor()


driver = webdriver.Chrome()
driver.maximize_window()
url = "https://twitter.com/login?lang=tr"
driver.get(url)
time.sleep(2)

kullaniciad1 = ""
password1 = ""

kullaniciad = driver.find_element_by_name("session[username_or_email]")
kullaniciad.send_keys(kullaniciad1)
time.sleep(1)

sifre = driver.find_element_by_name("session[password]")
sifre.send_keys(password1)
time.sleep(1)

giris = driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(8) > div > div")
giris.click()
time.sleep(1)

profil = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[5]/div/div[2]/span")
profil.click()
time.sleep(1)

takipci = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a/span[2]/span")
takipci.click()
time.sleep(1)

ekran_goruntusu = pyautogui.screenshot()
dosya_adi = "anlık.jpg"
ekran_goruntusu.save(dosya_adi)

scroll = 0
sayac = 0 
pause = 0.5


last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height 
    FlowList = driver.find_elements_by_css_selector(".css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")
    for i in FlowList:   
        takip =  ("https://twitter.com/" + i.text)
        print(takip)
        sql = "INSERT INTO benitakipedenler (takipcilerim) VALUES (%s)"
        val = (takip)
        mycursor.execute(sql, val)
        
        
connection.commit()
driver.quit()
print("Başarıyla Tamamlandı.")



            

