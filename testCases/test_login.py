import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getpassword()
    logger=LogGen.loggen()
    def test_loginpageTitle(self,setup):

        self.logger.info("Started Test_001_Login")
        self.logger.info("Verifying test_loginpageTitle")
        #self.driver=webdriver.Chrome()
        self.driver = setup

        self.driver.get(self.baseURL) # launching the webpage
        self.login_page=Login(setup)
        actual_title=self.driver.title
        if actual_title=="Login Page":
            assert True
            self.logger.info("test_loginpageTitle->> Title pass  ")
        else:
            assert False
            self.logger.info("test_loginpageTitle->> Title Fail  ")

    def test_homePageTitle(self,setup):
        #self.driver=webdriver.Chrome()
        self.logger.info("Verifying test_homePageTitle")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login_page=Login(self.driver)
        self.login_page.setUserName(self.username)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()
        actual_title=self.driver.title
        print(actual_title)
        time.sleep(2)
        self.driver.close()

        if actual_title=="EXAMSDashboard":
            assert True
            self.logger.info("test_homePageTitle->> Title pass")
        else:
            assert False
            self.logger.info("test_homePageTitle->> Title Fail")






