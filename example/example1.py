import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

from urllib import parse

options = Options()
options.headless = False
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://hisnet.handong.edu/login/login.php")

browser.find_element_by_name('id').send_keys('loveetls')
browser.implicitly_wait(3)
browser.find_element_by_name('password').send_keys('sit32004')
browser.implicitly_wait(3)
browser.find_element_by_name('login').submit()
browser.implicitly_wait(3)

# 게시판 글 읽기
time.sleep(5)
browser.find_element_by_xpath('//*[@id="td_box32"]').click()
notice = browser.find_element_by_xpath('//*[@id="tr_box_32"]/table/tbody')
time.sleep(5)
print(notice.text)

time.sleep(5)
browser.find_element_by_xpath('//*[@id="td_box34"]').click()
#//*[@id="tr_box_34"]/table/tbody
'''
browser.implicitly_wait(3)
browser.get("https://hisnet.handong.edu/cis/list.php?Board=KYOM_NOTICE&kang_yy=2020&kang_hakgi=1&CIS_GWAMOK=&AG=1")
notice = browser.find_element_by_name('login')
print()

browser.implicitly_wait(3)
browser.find_element_by_class_name('cls_AlignLeft listBody')

# browser.get(f"read.php?id=113301&Page=1&Board=KYOM_EXTRA&CateCode=2959&dflag=")
browser.navigate().back();

#WebElement formElement = driver.findElement(By.name("form_w"));
#List<WebElement> allFormChildElements = formElement.findElements(By.xpath("*"));
#browser.find_element_by_class_name('content')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


element = browser.find_element_by_name('content')
#WebDriverWait(browser, 5).until(
#    EC.presence_of_element_located((By.ID, "content"))
#  # Wait until the `text_to_score` element appear (up to 5 seconds)
browser.execute_script('oEditors.getById["content"].setIR("11")')
browser.find_element_by_name('form_w').submit()
browser.implicitly_wait(3)
browser.switch_to_frame('MyIFrame').switch_to_alert().accept();




import pymongo

conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.get_database('mongo_test')
collection = db.get_collection('customer')

collection.insert_one({"name":"cbchoi", "category":1, "region":'Daejeon'})

results = collection.find()

[print(result) for result in results]
'''