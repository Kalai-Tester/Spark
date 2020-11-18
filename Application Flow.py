import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://stagingapp.celohealth.com/")
driver.find_element_by_xpath("//button[@id='login']").click()
driver.find_element_by_id("Username").send_keys("qa.candidate+01@celohealth.com")
driver.find_element_by_id("Password").send_keys("3tQp+,/Q")
driver.find_element_by_css_selector("button[name='button']").click()
time.sleep(5)
driver.find_element_by_css_selector("#pin_code").send_keys('1410')
time.sleep(5)
driver.find_element_by_css_selector("#pin_code_confirm").send_keys('1410')
time.sleep(2)
elm = driver.find_element_by_xpath("//body/app-root[1]/div[1]/div[1]/app-pinscreen[1]/div[1]/div[1]/div[1]/div[3]/button[1]")
elm.click()
time.sleep(5)
driver.find_element_by_xpath("//div[@class='mid ng-tns-c130-5']").click()
time.sleep(2)
driver.find_element_by_id("celo-send-message-textarea").send_keys("Hi")
driver.find_element_by_xpath("//div[@class='bar']/button").click()
time.sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'Secure Library')]").click()
time.sleep(2)
driver.find_element_by_css_selector("span[class='lowercase']").click()

#driver.find_element_by_xpath("//div[@class='name']").click()
time.sleep(2)
#driver.find_element_by_xpath("//button[@id='celo-logout-button']/div[1]").click()

#xpath using Travesing tags:


# Xpath using text
#driver.find_element_by_xpath("//div[text()='Create new message']").click()





#driver.find_element_by_css_selector("#pin_code_confirm").send_keys('1234')

#pin = driver.find_element_by_css_selector("//input[@id='pin_code']")
#pin.send_keys('1234')

#driver.find_element_by_css_selector("input[name='passcode']").send_keys('1234')

# pin = driver.find_element_by_xpath("//input[@id='pin_code']")
# pin.send_keys('1234')



#driver.find_element_by_css_selector("input[name='passcodeConfirm']").send_keys("1234")
#driver.find_element_by_id("pin_code_confirm").send_keys("1234")
#driver.find_element_by_css_selector("button[class='mat-focus-indicator celo-primary-button fw mat-button mat-button-base mat-primary mat-button-disabled']").click()

