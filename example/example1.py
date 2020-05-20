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

browser.find_element_by_name('id').send_keys(LOGIN_ID)
browser.implicitly_wait(3)
time.sleep(2)
browser.find_element_by_name('password').send_keys(LOGIN_PW)
browser.implicitly_wait(3)
time.sleep(2)
browser.find_element_by_name('login').submit()
browser.implicitly_wait(3)

# 게시판 글 읽기
time.sleep(2)
browser.find_element_by_xpath('//*[@id="td_box32"]').click()
notice = browser.find_element_by_xpath('//*[@id="tr_box_32"]/table/tbody')
time.sleep(2)
print(notice.text)

# 과제정보
time.sleep(2)
browser.find_element_by_xpath('//*[@id="td_box34"]').click()
hw = browser.find_element_by_xpath('//*[@id="tr_box_34"]/table/tbody')
time.sleep(2)
print(hw.text)

# 과제 상세리스트
browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').click()
hw_d = browser.find_element_by_xpath('//*[@id="att_list"]/tbody')
time.sleep(2)
print(hw_d.text)

# 게시판 상세리스트
browser.back()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="td_box32"]').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').click()
time.sleep(2)
notice_d1 = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[1]')
print(notice_d1.text)

time.sleep(2)
browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[4]/td/table/tbody/tr/td/div/a[1]').click()
time.sleep(2)
notice_d1 = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[1]')
print(notice_d1.text)

# 쿠키 지우기
time.sleep(2)
browser.delete_all_cookies()
time.sleep(5)
#/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[1]
