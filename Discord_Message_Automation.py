from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
message1 = 'Automation testing please ignore'
driver.implicitly_wait(10)

driver.get('https://www.discord.com/login')

username = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input')
username.send_keys('Email here')
password = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input')
password.send_keys('password here')
signin = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]')
signin.click()
time.sleep(3)


links = driver.find_elements_by_css_selector("a[href*='/channels/@me/']")
for link in links:
    link.click()
    messagebox = driver.find_element_by_css_selector('#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div > div > div > div.content-98HsJk > div.chat-3bRxxu > div.content-yTz4x3 > main > form > div > div.scrollableContainer-2NUZem.webkit-HjD9Er > div > div.textArea-12jD-V.textAreaSlate-1ZzRVj.slateContainer-3Qkn2x > div.markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP')
    messagebox.send_keys(message1)
    messagebox.send_keys(Keys.ENTER)
    time.sleep(2)
