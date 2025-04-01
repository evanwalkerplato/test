import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        #set up webdriver for Chrome
        self.driver = webdriver.Chrome()

    def PhiladelphiaBeunosAires(self):

        #call on chrome webdriver, specify target website and confirm title of webpage
        driver = self.driver
        driver.get("https://blazedemo.com/")
        self.assertIn("BlazeDemo", driver.title)

        #select options from drop down menus
        elem1 = driver.find_element(By.XPATH, '//select[@name="fromPort"]/option[text()="Philadelphia"]')
        elem1.click()
        elem2 = driver.find_element(By.XPATH, '//select[@name="toPort"]/option[text()="Beunos Aires"]')
        elem2.click()
        
        #navigate to next webpage and confirm title
        button1 = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        button1.click()
        self.assertIn("BlazeDemo - reserve", driver.title)

        #confirm drop down choice from previous page is in text on this page
        driver.find_element(By.XPATH, "//h3[text()[contains(., 'Philadelphia')]]")
        driver.find_element(By.XPATH, "//h3[text()[contains(., 'Beunos Aires')]]")



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()