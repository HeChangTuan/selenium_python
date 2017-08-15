# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get("http://www.python.org")
driver.get("http://localhost:4000/#/")
# assert "text" in driver.title
# elem = driver.find_element_by_type("text")
elem = driver.find_element_by_xpath("//input[@type='text']")
elem.send_keys("28", Keys.RETURN)
# enterElem = driver.find_element_by_xpath("//span[@text='搜索']")
# enterElem.click()
# elem.send_keys(Keys.RETURN)
driver.quit()