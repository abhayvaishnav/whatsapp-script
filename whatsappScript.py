from selenium import webdriver
import time

chrome_browser = webdriver.Chrome()
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(10)

user_name = "Manashvi"

user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()

message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
message_box.send_keys('This message was sent usnig python script')

message_box = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
message_box.click()

time.sleep(100)