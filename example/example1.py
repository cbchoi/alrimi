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

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from urllib import parse
from instance.credential import *
import pymongo


conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.get_database('mongo_db')
collection = db.get_collection('customer')

options = Options()
options.headless = False
browser = webdriver.Chrome(executable_path="./chromedriver", options=options)
LOGIN_ID = collection.find_one({"id"})
LOGIN_PW = collection.find_one({"pw"})

#browser.get("https://hisnet.handong.edu/login/login.php")

# python_input.py
#LOGIN_ID = input("아이디를 입력해주세요.")
#LOGIN_PW = input("비밀번호를 입력해주세요.")

#print("{name}님 환영합니다.".format(name=LOGIN_ID))

def first(LOGIN_ID, LOGIN_PW):
	browser.get("https://hisnet.handong.edu/login/login.php")
	time.sleep(2)
	print('!!!')
	browser.find_element_by_name('id').send_keys(LOGIN_ID)
	browser.implicitly_wait(3)
	time.sleep(1)
	browser.find_element_by_name('password').send_keys(LOGIN_PW)
	browser.implicitly_wait(3)
	time.sleep(1)
	browser.find_element_by_name('login').submit()
	browser.implicitly_wait(3)

# 게시판 글 읽기
def list(browser):
	browser.get("https://hisnet.handong.edu/for_student/main.php")
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="td_box32"]').click()
	notice = browser.find_element_by_xpath('//*[@id="tr_box_32"]/table/tbody')
	time.sleep(1)
	print(notice.text)
	
	return notice.text

	

# 과제정보
def HW(browser):
	browser.get("https://hisnet.handong.edu/for_student/main.php")
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="td_box34"]').click()
	hw = browser.find_element_by_xpath('//*[@id="tr_box_34"]/table/tbody')
	time.sleep(2)
	print(hw.text)

	return hw.text

# 과제 상세리스트
def HW_all(browser):
	browser.get("https://hisnet.handong.edu/for_student/main.php")
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="td_box34"]').click()
	time.sleep(1)
	browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').click()
	hw_d = browser.find_element_by_xpath('//*[@id="att_list"]/tbody')
	time.sleep(2)
	print(hw_d.text)

# 게시판 상세리스트
def list_all(browser):
	browser.get("https://hisnet.handong.edu/for_student/main.php")
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="td_box32"]').click()
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').click()
	time.sleep(2)
	number = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[4]/td/table/tbody')
	number_text = number.text
	number_list = number_text.split('ㆍ 0')
	print(number_list)
	for i in number_list:
		browser.get(f"https://hisnet.handong.edu/cis/list.php?dflag=&Page={i}&Board=KYOM_NOTICE&CIS_GWAMOK=&AG=1")
		notice_d1 = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[1]')
		print(notice_d1.text)
	#https://hisnet.handong.edu/cis/list.php?dflag=&Page=1&Board=KYOM_NOTICE&CIS_GWAMOK=&AG=1
	notice_d1 = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[1]')
	print(notice_d1.text)

#browser.find_element_by_class_name(cls_AlignLeft listBody)
def mondb(list, hw):
	mongo.collection.insert_one({'게시판':list}, {'과제':hw})
	result = mongo.collection.find()
	[print(result) for result in result]

# 쿠키 지우기
def end(browser):
	time.sleep(2)
	browser.delete_all_cookies()
	time.sleep(5)
	print("clear!")
#/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[1]

def main(browser):
	first(LOGIN_ID, LOGIN_PW)
	list(browser)
	list_all(browser)
	HW(browser)
	HW_all(browser)
	end(browser)
	mondb(list(browser),HW(browser))

#main(browser)