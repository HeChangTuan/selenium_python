# coding=utf-8
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
import unittest
import random
import itertools
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class loginClosedLoop(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('Content-Type="application/json"')
        options.add_argument('Authorization="pmJwtSecret"')
        options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 wechatdevtools/0.7.0 MicroMessenger/6.3.9 Language/zh_CN webview/0"')
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
        manuallyOpenId = 'ox_' + slice[0] + slice[1] + slice[2] + slice[3] + slice[4] + slice[5] + slice[6] + slice[7]
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
        time.sleep(30)
        checkTeam = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div[2]/div[3]/button").click()
        driver.implicitly_wait(5)
        choiceTeam = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div/ul/li[3]").click()
        driver.implicitly_wait(5)
        focusTeam = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div[3]/button").click()
        phoneNOList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        phoneSlice = random.sample(phoneNOList, 8)
        phoneStr = '134' + phoneSlice[0] + phoneSlice[1] + phoneSlice[2] + phoneSlice[3] + phoneSlice[4] + phoneSlice[5] + phoneSlice[6] + phoneSlice[7]
        time.sleep(3)
        phoneInput = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div/div[1]/div[2]/div/input").send_keys(phoneStr)
        sendCodeBtn = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div/div[1]/div[2]/button").click()
        verifycodeInput = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div/div[1]/div[3]/div/input").send_keys("1716")
        nextBtn = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div/div[1]/button").click()
        time.sleep(3)
        nameInput = driver.find_element_by_name("name").send_keys(nameStr.decode())
        # nickInput = driver.find_element_by_xpath("//@input[name='nickname']").send_keys(nickStr)
        gendStr = ''
        genderRan = random.randint(1, 2)
        gendStr = str(genderRan)
        time.sleep(3)
        genderRadio = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div/div[2]/div/div[3]/div/div/article["+gendStr+"]/span").click()
        yearInput = driver.find_element_by_name("year").send_keys("1965")
        monthInput = driver.find_element_by_name("month").send_keys("4")
        dayInput = driver.find_element_by_name("date").send_keys("15")
        submitBtn = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div/div[2]/button").click()
        time.sleep(3)
        # self.assertIn("Python", driver.title)
        

    def tearDown(self):
        print 'completed......'
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()