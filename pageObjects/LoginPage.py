from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

class Login:

    testbox_username_name = "username"
    textbox_password_name = "password"
    button_login_xpath = "//*[@value='Login']"
    button_logout_linktext = "Logout"
  #==========================================
    def __init__(self,setup):
        self.driver=setup

    def setUserName(self,username):

       element = self.driver.find_element(By.NAME, self.testbox_username_name)
       element.clear()
       element.send_keys(username)#

    def setPassword(self,password):
        element = self.driver.find_element(By.NAME, self.textbox_password_name)
        element.clear()
        element.send_keys(password)  #

    def clickLogin(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.button_login_xpath))
        )
        element.click()

    def clickLogout(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.button_logout_linktext))
        )
        element.click()


