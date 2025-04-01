import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        #set up webdriver for Chrome
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):

        #call on chrome webdriver, specify target website and confirm title of webpage
        driver = self.driver
        driver.get("https://blazedemo.com/")
        self.assertIn("BlazeDemo", driver.title)

        #select options from drop down menus
        elem1 = driver.find_element(By.XPATH, '//select[@name="fromPort"]/option[text()="Portland"]')
        elem1.click()
        elem2 = driver.find_element(By.XPATH, '//select[@name="toPort"]/option[text()="Berlin"]')
        elem2.click()
        
        #navigate to next webpage and confirm title
        button1 = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        button1.click()
        self.assertIn("BlazeDemo - reserve", driver.title)

        #confirm drop down choice from previous page is in text on this page
        driver.find_element(By.XPATH, "//h3[text()[contains(., 'Portland')]]")

        #navigate to next page using first flight option and confirm title of new webpage
        button2 = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        button2.click()
        time.sleep(3)
        self.assertIn("BlazeDemo Purchase", driver.title)

        #confirm appropriate airport code
        driver.find_element(By.XPATH, "//h2[text()[contains(., 'TLV')]]")

        #fill out contact information
        driver.find_element(By.NAME, "inputName").send_keys("Han Solo")
        driver.find_element(By.NAME, "address").send_keys("99 Yavin 4")
        driver.find_element(By.NAME, "city").send_keys("Echo Base")
        driver.find_element(By.NAME, "state").send_keys("Hoth")
        driver.find_element(By.NAME, "zipCode").send_keys("99999")
        driver.find_element(By.XPATH, "//select[@name=\"cardType\"]/option[text()=\"Diner's Club\"]")
        driver.find_element(By.NAME, "creditCardMonth").send_keys("10")
        driver.find_element(By.NAME, "creditCardYear").send_keys("2254")
        driver.find_element(By.NAME, "nameOnCard").send_keys("Han Solo")
        driver.find_element(By.NAME, "rememberMe").click()

        #navigate to next page and confirm title
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        time.sleep(3)
        self.assertIn("BlazeDemo Confirmation", driver.title)

        #confirm thank you message
        driver.find_element(By.XPATH, "//h1[text()[contains(., 'Thank you')]]")

        #navigate back to starting page
        driver.find_element(By.LINK_TEXT, "Travel The World").click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()