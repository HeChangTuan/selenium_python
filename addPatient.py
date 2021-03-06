# coding=utf-8
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
import unittest
import random
import itertools
import time
import ConfigParser
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cf = ConfigParser.ConfigParser()
cf.read("config.conf")
class addPatient(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument(cf.get("browserOptions", "ContentType"))
        options.add_argument(cf.get("browserOptions", "Authorization"))
        options.add_argument(cf.get("browserOptions", "UserAgent"))
        # print options.getArgument()
        self.driver = webdriver.Chrome(chrome_options=options)
    
    def test_search_in_python_org(self):
        driver = self.driver
        list = ['Ke', '2l', '4A', 'O4', 'p5', 'm6', 's7K', 'eL8', 'f9', 'Iw0', 'xR', 'Ub', 'Tx', 'Yq'] 
        slice = random.sample(list, 8)
        nickList = ['自1', '动2', '测3', '试4', '动5', '测6', '自7', '试8', '9', '动10', '自', '动', '测', '试']
        nickSlice = random.sample(nickList, 3)
        nickStr = nickSlice[2] + nickSlice[1] + nickSlice[0]
        nameList = ['自', '动', '测', '试']
        nameSlice = random.sample(nameList, 3)
        nameStr = nameSlice[0] + nameSlice[1] + nameSlice[2]
        manuallyOpenId = cf.get("wx", "manuallyOpenId")
        openIdStr = """localStorage.setItem("openId", '""" + manuallyOpenId + """');"""
        getLocalStorage = """return localStorage.getItem("openId");"""
        url = "https://www.peoplesmedic.com/app/#/?comAppId=wxaacbcd85e20d5386&hospitalId=2c92be085b8a6b16015b8a80afc70004&state=789&appid=wx321d996e7d403afc&openId="+manuallyOpenId+"&nick_name="+nickStr+"&sex=1&image=http://wx.qlogo.cn/mmopen/DmTSLTdleeuBvVv92afjgmE86TYic9DE7TUu4XB8Hcq8j4n0Z8T7ay4mkll6sHnYiau9Ck7BjSia0XchyicSdnxsE6fymic6vnBEy/0"
        # url = "http://localhost:3111/app/#/?comAppId=wxaacbcd85e20d5386&hospitalId=2c92be085b8a6b16015b8a80afc70004&state=789&appid=wx321d996e7d403afc&openId="+manuallyOpenId+"&nick_name="+nickStr+"&sex=1&image=http://wx.qlogo.cn/mmopen/DmTSLTdleeuBvVv92afjgmE86TYic9DE7TUu4XB8Hcq8j4n0Z8T7ay4mkll6sHnYiau9Ck7BjSia0XchyicSdnxsE6fymic6vnBEy/0"
        driver.get(url)
        driver.execute_script(openIdStr)
        time.sleep(5)
        # driver.refresh()
        driver.get(url)
        # checkLocalStorage = driver.execute_script(getLocalStorage)
        # print driver.current_url
        # print checkLocalStorage
        time.sleep(5)
        accountBtn = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div[2]/ul/li[3]/a").click()
        time.sleep(2)
        myPatientBtn = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div[1]/section[3]/div[2]/div[2]/li[1]/a").click()
        time.sleep(3)
        addBtn = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div[2]/button").click()
        time.sleep(1)
        nameInput = driver.find_element_by_name("name").send_keys(nameStr.decode())
        # nicknameInput = driver.find_element_by_name("nickname").send_keys(nickStr.decode())
        gendStr = ''
        genderRan = random.randint(1, 2)
        gendStr = str(genderRan)
        time.sleep(1)
        genderRaido = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div[3]/div[2]/div[2]/div/div[3]/div/div/article[" + gendStr + "]/span").click()
        yearInput = driver.find_element_by_name("year").send_keys("1965")
        monthInput = driver.find_element_by_name("month").send_keys("4")
        dayInput = driver.find_element_by_name("date").send_keys("15")
        submitBtn = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div[3]/div[2]/div[1]/div/button[2]").click()
        time.sleep(5)
        # self.assertIn("Python", driver.title)
        

    def tearDown(self):
        print 'completed......'
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()