# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get("https://test.fabrikant.ru/")
        driver.find_element_by_xpath("//button[@type='button']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_name("login[username]").click()
        driver.find_element_by_name("login[username]").clear()
        driver.find_element_by_name("login[username]").send_keys("fabrikant")
        driver.find_element_by_name("login[password]").click()
        driver.find_element_by_name("login[password]").clear()
        driver.find_element_by_name("login[password]").send_keys("Qqqq111!")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Отмена'])[1]/following::span[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_xpath("//div[@id='root']/div/header/div/div[4]/div/div/div/a/span/p[3]").click()
        driver.find_element_by_xpath("//div[@id='root']/div[2]/div/div/div[23]/div/div/h2/div/a/p").click()
        driver.find_element_by_xpath("//div[@id='wrapper']/section[2]/div/button/span/span").click()
        driver.find_element_by_xpath("//div[@id='popupImportFromOOS']/div/div/div[3]/button[5]/span/span").click()
        driver.find_element_by_css_selector("svg._2lO4aRo-GdqweyXs88LYXA > use").click()
        driver.find_element_by_xpath("//div[3]/center/input[2]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
