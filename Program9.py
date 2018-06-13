import platform
import time
from selenium import webdriver
x=int(input("Which browser to use?\n1.Firefox\n2.PhantomJS\n"))
if (x==1):
    browser = webdriver.Firefox()
else:
    browser = webdriver.PhantomJS('./phantomjs.exe')
browser.get("https://ums.lpu.in/lpuums/LoginNew.aspx")
browser.find_element_by_id("txtU").send_keys('11502105')
browser.find_element_by_id("Txtpw").send_keys('321G@mers')
browser.find_element_by_id("iBtnLogins").click()
time.sleep(2)
browser.find_element_by_id("Txtpw").send_keys('321G@mers')
browser.find_element_by_id("iBtnLogins").click()
browser.get("https://ums.lpu.in/lpuums/frmStudentResultDisplay.aspx")
html = browser.page_source
print (html)