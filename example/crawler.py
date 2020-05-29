from evsim.system_simulator import SystemSimulator
from evsim.behavior_model_executor import BehaviorModelExecutor
from evsim.system_message import SysMessage
from evsim.definition import *

from config import *
from instance.credential import *

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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
import pymongo

'''conn = pymongo.MongoClient('mongodb://localhost:27017')
db = conn.get_database('mongo_db')
collection = db.get_collection('Hisnet')'''

options = Options()
options.headless = False
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options = options)

class Crawler(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

        # Open CSV
        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)
        self.insert_state("PROCESS", 20)

        self.insert_input_port("report")

        # telegram
        self.updater = Updater(TELEGRAM_TOKEN, use_context=True)

        self.conn = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.conn.get_database('mongo_db')
        self.collection = self.db.get_collection('Hisnet')

    def ext_trans(self, port, msg):
        if port == "report":
            results = self.collection.find()
            # {"id" : user, "pw" : user_pw, "chat_id"
            for result in results:
                result['id']
                result['pw']
                print(result)

                self.first(result['id'], result['pw'])
                notice_lst = self.ilist(browser)
                homework_lst = self.HW(browser)
                self.mondb(result['id'], notice_lst, homework_lst, result['id'])
                self.end(browser)

            self._cur_state = "PROCESS"
            

    def output(self):
        if self._cur_state == "PROCESS":

            # if homework exist
            # Hisnet에서 모든 document를 가져옴
            results = self.collection.find()
            # {"id" : user, "pw" : user_pw, "chat_id"
            for result in results:
                result['id']
                result['pw']
                result['chat_id']
                print(result)

                self.first(result['id'], result['pw'])
                notice_lst = self.ilist(browser)
                homework_lst = self.HW(browser)
                self.mondb(result['id'], notice_lst, homework_lst, result['chat_id'])
                self.end(browser)



    def first(self, LOGIN_ID, LOGIN_PW):
        browser.get("https://hisnet.handong.edu/login/login.php")
        time.sleep(0.3)
        print('!!!')
        browser.find_element_by_name('id').send_keys(LOGIN_ID)
        browser.implicitly_wait(3)
        time.sleep(0.3)
        browser.find_element_by_name('password').send_keys(LOGIN_PW)
        browser.implicitly_wait(3)
        time.sleep(0.3)
        browser.find_element_by_name('login').submit()
        browser.implicitly_wait(3)


        # 게시판 글 읽기
    def ilist(self, browser):
        browser.get("https://hisnet.handong.edu/for_student/main.php")
        time.sleep(0.3)
        browser.find_element_by_xpath('//*[@id="td_box32"]').click()
        notice = browser.find_element_by_xpath('//*[@id="tr_box_32"]/table/tbody')
        time.sleep(0.3)
        print(notice.text)

        return notice.text


    # 과제정보
    def HW(self, browser):
        browser.get("https://hisnet.handong.edu/for_student/main.php")
        time.sleep(0.3)
        browser.find_element_by_xpath('//*[@id="td_box34"]').click()
        hw = browser.find_element_by_xpath('//*[@id="tr_box_34"]/table/tbody')
        time.sleep(0.3)
        print(hw.text)

        return hw.text


    # 과제 상세리스트
    def HW_all(self, browser):
        browser.get("https://hisnet.handong.edu/for_student/main.php")
        time.sleep(0.3)
        browser.find_element_by_xpath('//*[@id="td_box34"]').click()
        time.sleep(0.3)
        browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').click()
        hw_d = browser.find_element_by_xpath('//*[@id="att_list"]/tbody')
        time.sleep(0.3)
        print(hw_d.text)

        return hw_d.text


    # 게시판 상세리스트
    def list_all(self, browser):
        browser.get("https://hisnet.handong.edu/for_student/main.php")
        time.sleep(0.3)
        browser.find_element_by_xpath('//*[@id="td_box32"]').click()
        time.sleep(0.3)
        browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/table/tbody/tr[1]/td[2]').click()
        time.sleep(0.3)
        number = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[4]/td/table/tbody')
        number_text = number.text
        number_list = number_text.split('ㆍ 0')
        notice_d = ''
        print(number_list)
        for i in number_list:
            browser.get(f"https://hisnet.handong.edu/cis/list.php?dflag=&Page={i}&Board=KYOM_NOTICE&CIS_GWAMOK=&AG=1")
            notice_d1 = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[1]')
            print(notice_d1.text)
            notice_d = notice_d + notice_d1.text
        #https://hisnet.handong.edu/cis/list.php?dflag=&Page=1&Board=KYOM_NOTICE&CIS_GWAMOK=&AG=1
        #notice_d1 = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr[4]/td/table/tbody/tr[1]')

        return notice_d

    #browser.find_element_by_class_name(cls_AlignLeft listBody)
    def mondb(self, LOGIN_ID, notice_lst, hw_lst, chatid):
        #co = self.collection.find_one({"id" : LOGIN_ID},{'게시판' : { "$exists" : True}})
        #ho = self.collection.find_one({"id" : LOGIN_ID},{'과제' : { "$exists" : True}})


        co1 = self.collection.find_one({"id" : LOGIN_ID}, {"_id":False,"게시판":True})
        
        if co1 != {}:
            if co1["게시판"] != notice_lst:
                self.collection.update({'id' : LOGIN_ID}, {"$set":{"게시판": notice_lst}})
                self.updater.bot.send_message(chatid, "update")
        else:
            self.collection.update({'id' : LOGIN_ID}, {"$set":{"게시판": notice_lst}})
            self.updater.bot.send_message(chatid, "first ^^")
        ho1 = self.collection.find_one({"id" : LOGIN_ID}, {"_id":False,"과제":True})
        if ho1 != {}:
            if ho1["과제"] != hw_lst:
                self.collection.update({'id' : LOGIN_ID}, {"$set":{"과제": hw_lst}})
                self.updater.bot.send_message(chatid, "update")
        else:
            self.collection.update({'id' : LOGIN_ID}, {"$set":{"과제": hw_lst}})
                    
    # 쿠키 지우기
    def end(self, browser):
        time.sleep(0.3)
        browser.delete_all_cookies()
        time.sleep(2)
        print("clear!") 
        browser.get('https://hisnet.handong.edu/login/logout.php')

    def int_trans(self):
        if self._cur_state == "PROCESS":
            self._cur_state = "PROCESS"