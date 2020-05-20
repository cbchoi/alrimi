import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from urllib import parse

# 게시판 글 읽기
#browser.get(f"https://hisnet.handong.edu/cis/list.php?Board=KYOM_EXTRA&CateCode=2959")

def post_thread(browser, subject, content):
	browser.get(f"https://hisnet.handong.edu/cis/write.php?Board=KYOM_EXTRA&CateCode=2959&CIS_GWAMOK=20200101SIT32004&dflag=")
	browser.find_element_by_name('subject').send_keys(subject)

	#WebElement formElement = driver.findElement(By.name("form_w"));
	#List<WebElement> allFormChildElements = formElement.findElements(By.xpath("*"));
	#browser.find_element_by_class_name('content')

	element = browser.find_element_by_name('content')
	#WebDriverWait(browser, 5).until(
	#    EC.presence_of_element_located((By.ID, "content"))
	#)  # Wait until the `text_to_score` element appear (up to 5 seconds)
	browser.execute_script(f'oEditors.getById["content"].setIR("{content}")')
	browser.execute_script('CheckFormW(document.form_w)')
	#browser.switch_to_frame("MyIFrame")
	browser.implicitly_wait(5)

	try:
	    WebDriverWait(browser, 3).until(EC.alert_is_present(),
	                                   'Timed out waiting for PA creation ' +
	                                   'confirmation popup to appear.')

	    alert = browser.switch_to.alert
	    alert.accept()
	    print("alert accepted")
	except TimeoutException:
	    print("no alert")

def handle_alert(browser):
	try:
	    WebDriverWait(browser, 3).until(EC.alert_is_present(),
	                                   'Timed out waiting for PA creation ' +
	                                   'confirmation popup to appear.')

	    alert = browser.switch_to.alert
	    alert.accept()
	    print("alert accepted")
	except TimeoutException:
	    print("no alert")

options = Options()
options.headless = False
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://hisnet.handong.edu/login/login.php")

browser.find_element_by_name('id').send_keys('loveetls')
browser.find_element_by_name('password').send_keys('sit32004')
browser.find_element_by_name('login').submit()
browser.implicitly_wait(3)

post_thread(browser, "nice", "Hello, World!!")