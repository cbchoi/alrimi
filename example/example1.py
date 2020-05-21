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

options = Options()
options.headless = False
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)

browser.get("https://hisnet.handong.edu/login/login.php")

# python_input.py
LOGIN_ID = input("아이디를 입력해주세요.")
LOGIN_PW = input("비밀번호를 입력해주세요.")

print("{name}님 환영합니다.".format(name=LOGIN_ID))

browser.find_element_by_name('id').send_keys(LOGIN_ID)
browser.implicitly_wait(3)
time.sleep(2)
browser.find_element_by_name('password').send_keys(LOGIN_PW)
browser.implicitly_wait(3)
time.sleep(2)
browser.find_element_by_name('login').submit()
browser.implicitly_wait(3)

# 게시판 글 읽기
def list(browser):
	browser.get("https://hisnet.handong.edu/for_student/main.php")
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="td_box32"]').click()
	notice = browser.find_element_by_xpath('//*[@id="tr_box_32"]/table/tbody')
	time.sleep(2)
	print(notice.text)
	search = '//input[@name="email_address"]'
	

# 과제정보
def HW(browser):
	browser.get("https://hisnet.handong.edu/for_student/main.php")
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="td_box34"]').click()
	hw = browser.find_element_by_xpath('//*[@id="tr_box_34"]/table/tbody')
	time.sleep(2)
	print(hw.text)

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
	notice_d1 = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[1]')
	print(notice_d1.text)

#browser.find_element_by_class_name(cls_AlignLeft listBody)


# 쿠키 지우기
def end(browser):
	time.sleep(2)
	browser.delete_all_cookies()
	time.sleep(5)
	print("clear!")
#/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[1]

def main(browser):
	z = input("최근 공지사항 = list입력 / 모든 공지사항 =  list_all입력 / 최근 과제 = HW입력 / 모든 과제 = HW_all 입력")
	if z == 'list':
		list(browser)
	elif z == 'list_all':
		list_all(browser)
	elif z == 'HW':
		HW(browser)
	elif z == 'HW_all':
		HW_all(browser)

main(browser)