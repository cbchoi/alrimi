import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

from urllib import parse

options = Options()
options.headless = False
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://hisnet.handong.edu/login/login.php")

browser.find_element_by_name('id').send_keys('loveetls')
browser.find_element_by_name('password').send_keys('sit32004')
browser.find_element_by_name('login').submit()
browser.implicitly_wait(3)

# 게시판 글 읽기
#browser.get(f"https://hisnet.handong.edu/cis/list.php?Board=KYOM_EXTRA&CateCode=2959")

browser.get(f"https://hisnet.handong.edu/cis/write.php?Board=KYOM_EXTRA&CateCode=2959&dflag=")
browser.find_element_by_name('subject').send_keys('loveetls')

#WebElement formElement = driver.findElement(By.name("form_w"));
#List<WebElement> allFormChildElements = formElement.findElements(By.xpath("*"));
#browser.find_element_by_class_name('content')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


element = browser.find_element_by_name('content')
#WebDriverWait(browser, 5).until(
#    EC.presence_of_element_located((By.ID, "content"))
#)  # Wait until the `text_to_score` element appear (up to 5 seconds)
browser.execute_script('oEditors.getById["content"].setIR("11")')
browser.find_element_by_name('form_w').submit()
browser.implicitly_wait(3)
browser.switch_to_frame('MyIFrame').switch_to_alert().accept();

