# coding=utf-8
import string, os, sys  

reload(sys)  
sys.setdefaultencoding('utf8')
import unittest
import random
import itertools
import time
import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        cf = ConfigParser.ConfigParser()
        cf.read("config.conf")
        #return all section
        secs = cf.sections()
        print 'sections:', secs
         
        opts = cf.options("user")
        print 'options:', opts
         
        kvs = cf.items("user")
        print 'db:', kvs
         
        #read by type
        db_host = cf.get("user", "user_account")
        db_port = cf.get("user", "user_password")
         
        #read int
        threads = cf.getint("patient", "patient_test_code")
         
        print "db_host:", db_host
        print "db_port:", db_port
         
        print "thread:", threads
         
        # driver.get("http://www.gzmed.gov.cn/rhin_gzmed/xxgk/ylxx/index.html")
        # # self.assertIn("Python", driver.title)
        
        # time.sleep(5)
        # for x in range(0, 200):
        #     dataTable = driver.find_element_by_xpath("/html/body/div/div[2]/div[4]/table")
        #     allChildren = dataTable.find_elements_by_tag_name("a")
        #     for child in allChildren:
        #         print 'len(allChildren): ' + child.get_attribute('innerHTML')
        #     nextBtn = driver.find_element_by_class_name('next').click()
        #     time.sleep(5)


        

        # time.sleep(10)
        # newBtn = driver.find_element_by_xpath("//html/body/div/div/div[3]/div/div/div[2]/span[1]/button")
        # newBtn.click()
        # driver.implicitly_wait(3)
        # list = ['自1', '动2', '测3', '试4', '动5', '测6', '自7', '试8', '9', '动10', '自', '动', '测', '试'] 
        # slice = random.sample(list, 3)  #从list中随机获取5个元素，作为一个片断返回 
        # nameInput = driver.find_element_by_xpath("//html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/input")
        # nameInput.send_keys(slice)
        # phoneInput = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/input")
        # phoneInput.send_keys('13400000002')
        # dateInput = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[3]/div[1]/input")
        # dateInput.click()
        # curDateInput = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/span[26]")
        # curDateInput.click()
        # gendStr = ''
        # genderRan = random.randint(1, 2)
        # gendStr = str(genderRan)
        # genderRadio = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[4]/div[1]/div/div["+gendStr+"]/b")
        # genderRadio.click()
        # saveBtn = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/span[2]/button")
        # saveBtn.click()
        # driver.implicitly_wait(10)
        # searchelem = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div[2]/div/input")
        # serachkey = slice[0] + slice[1] + slice[2]
        # print serachkey
        # searchelem.send_keys(unicode(serachkey, errors='replace'), Keys.RETURN)
        # driver.implicitly_wait(15)
        # patientBtn = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div[3]/table/tr[2]/td[3]/a")
        # patientBtn.click()
        # driver.implicitly_wait(5)
        # delBtn = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/span[4]/button")
        # delBtn.click()
        # driver.implicitly_wait(1)
        # confirmBtn = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[4]/div[2]/div[1]/div[2]/div/span[2]/button")
        # confirmBtn.click()
        # assert "No results found." not in driver.page_source

    # def tearDown(self):
    #     print 'completed......'
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()