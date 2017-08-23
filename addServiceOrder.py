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
        manuallyOpenId = 'ox_KOxBN7ptz9X0KIwnsIEjJkfjc'
        openIdStr = """localStorage.setItem("openId", '""" + manuallyOpenId + """');"""
        getLocalStorage = """return localStorage.getItem("openId");"""
        teamNum = '4' #修改为需要测试的团队序列号,从左至右,由1开始
        serviceName = '测试服务2' #修改为需要测试的服务名
        orderVar = 'afternoon' #需要预约时段 morning or afternoon 
        timeVar = '12:00 - 12:30' #需要的具体时间段
        dateStr = '25' #需要选择的日期
        patientName = '自测动' #需要测试预约的就诊人
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
        doctorBtn = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div[2]/ul/li[2]/a").click()
        time.sleep(2)
        if teamNum != '1': 
            choiceTeam = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div[1]/section[2]/div/div[2]/div[2]/div[2]/div["+teamNum+"]").click()
            time.sleep(2)
        serviceLabel = driver.find_element_by_xpath("//label[contains(text(), '"+serviceName+"')]")
        serviceBtn = serviceLabel.find_element_by_xpath("..").click()
        time.sleep(2)
        datespan = driver.find_element_by_xpath("//span[contains(text(), '"+dateStr+"')]")
        dateParent = datespan.find_element_by_xpath("..")
        if orderVar == 'morning':
            dateParent.find_element_by_xpath(".//span[3]").click()
        else:
            dateParent.find_element_by_xpath(".//span[4]").click()
        # bookingBtn = driver.find_elements_by_xpath("//span[contains(@class, 'Calendar_"+orderVar+"')]")[0]
        # print bookingBtn
        # bookingBtn.click()
        time.sleep(2)
        timeBtn = driver.find_element_by_xpath("//span[contains(text(),'"+timeVar+"')]").click()
        nextBtn = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div[2]/div[2]/div[1]/div/button[2]").click()
        time.sleep(3)
        patientCtrl = driver.find_element_by_xpath("//strong[contains(text(),'"+patientName+"')]")
        patientCtrl.find_element_by_xpath("..//span").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/section/article/div/div[1]/div[2]/button").click()
        time.sleep(10)
        # self.assertIn("Python", driver.title)
        

    def tearDown(self):
        print 'completed......'
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()