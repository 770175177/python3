#!/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()
web.get('https://www.baidu.com')
input=web.find_element(By.ID, 'kw')
print(input)
input.send_keys('python')
input=web.find_element(By.ID, 'su').click()

time.sleep(10)
web.close()
