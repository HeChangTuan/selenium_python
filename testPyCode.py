# coding=utf-8
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
import unittest
import random
import itertools
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://localhost:4000/#/")
        # self.assertIn("Python", driver.title)
        
        newBtn = driver.find_element_by_xpath("//html/body/div/div/div[3]/div/div/div[2]/span[1]/button")
        newBtn.click()
        driver.implicitly_wait(3)
        list = ['自1', '动2', '测3', '试4', '动5', '测6', '自7', '试8', '9', '动10', '自', '动', '测', '试'] 
        slice = random.sample(list, 3)  #从list中随机获取5个元素，作为一个片断返回  
        print slice
        nameInput = driver.find_element_by_xpath("//html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/input")
        nameInput.send_keys(slice)
        phoneInput = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[2]/div[1]/input")
        phoneInput.send_keys('13400000002')
        dateInput = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[3]/div[1]/input")
        dateInput.click()
        curDateInput = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/span[26]")
        curDateInput.click()
        gendStr = ''
        genderRan = random.randint(1, 2)
        gendStr = str(genderRan)
        genderRadio = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[2]/div/div/div[4]/div[1]/div/div["+gendStr+"]/b")
        genderRadio.click()
        saveBtn = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/div[2]/span[2]/button")
        saveBtn.click()
        driver.implicitly_wait(5)
        elem = driver.find_element_by_xpath("//input[@type='text']")
        print slice[0]
        elem.send_keys(unicode(slice[0], errors='replace'), Keys.RETURN)
        driver.implicitly_wait(2)
        patientBtn = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div/div[3]/table/tr[2]/td[3]/a")
        driver.implicitly_wait(5)
        # assert "No results found." not in driver.page_source

    def tearDown(self):
        print 'completed......'
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()