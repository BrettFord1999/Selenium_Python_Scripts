#This script sets all your current Connectwise tickets to be scheduled for the current date

# web automation for Connectwise
from selenium import webdriver
import time
from datetime import date
from selenium.webdriver.common.keys import Keys
today = date.today()
today = today.strftime("%m/%d/%Y")

driver = webdriver.Edge(executable_path='C:\webdrivers\msedgedriver.exe')
driver.implicitly_wait(7)

driver.get('https://connect.sagiss.com')
driver.maximize_window()



companyid = driver.find_element_by_xpath('//*[@id="company"]')
companyid.send_keys('sagiss')

username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('bford')


loginbutton = driver.find_element_by_xpath('//*[@id="loginBtn"]')
loginbutton.click()

time.sleep(3)

#Window handles
print("First window title = " + driver.title)
print(driver.window_handles)
#Switch windows
driver.switch_to.window(driver.window_handles[1])
proceed = driver.find_element_by_xpath('//*[@id="sso-session-dialog"]/table/tbody/tr[2]/td/input[1]')
proceed.click()

driver.switch_to.window(driver.window_handles[0])


#My list click
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[3]/div/div').click()

ticket = (len(driver.find_elements_by_xpath('//*[@id="srboardmember-listview-scroller"]/div[1]/table/tbody[2]/tr[*]')))

for elements in range(1,15):
    element = driver.find_element_by_css_selector("#srboardmember-listview-scroller > div.GE0S-T1CAVF > table > tbody:nth-child(2) > tr:nth-child("+str(ticket)+") > td:nth-child(10)")
    element.click()
    ticket = int(ticket) - 1
    time.sleep(1)
    #Click Brett Ford
    driver.find_element_by_xpath('//*[@title="Brett Ford"]').click()
    #click input box for date
    driver.find_element_by_css_selector('#x-auto-138-input').click()
    driver.find_element_by_css_selector('#x-auto-138-input').clear()
    driver.find_element_by_css_selector('#x-auto-138-input').send_keys(str(today) + Keys.ENTER)
    time.sleep(1)
    save = driver.find_element_by_xpath("//*[@class='GE0S-T1CLDJ GE0S-T1CNOI GE0S-T1CCEJ cw_buttonSave']")
    save.click()
    time.sleep(3)
    #This handles schedule conflict popups
    try:
      driver.find_element_by_xpath('//*[@id="x-auto-219"]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/div/div/div').click()
    except:
      print("no conflict")
