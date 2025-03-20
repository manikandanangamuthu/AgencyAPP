import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class Logo:
    # Locators
    btn_UploadManagement_LINK_TEXT = "Upload Management"
    btn_UploadExamLogo_LINK_TEXT = "Upload Exam Logo"
    txt_CompanyName_xpath = "//input[@id='cmpName']"
    btn_CompanyLogo_xpath = "//input[@id='logoFile']"
    btn_Submit_xpath = "//*[@value='Submit']"

    # Constructor
    def __init__(self,setup):
        self.driver = setup # Pass the driver from test cases

    # Methods
    def clk_upload_management_button(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.btn_UploadManagement_LINK_TEXT))
        )
        element.click()

    def clk_upload_exam_logo_button(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.btn_UploadExamLogo_LINK_TEXT))
        )
        element.click()

    def set_company_name(self,companyname):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_CompanyName_xpath))
        )
        element.clear()
        element.send_keys(companyname)

    def upload_company_logo(self):
        """Uploads a file from the testData folder"""
        file_path="C:\\Users\\05444\\PycharmProjects\\AgencyApp\\TestData\\company_logo.jpg"
        #file_path = os.path.abspath(f"testData/{companylogo}")  # Dynamic file path
        file_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_CompanyLogo_xpath))
        )
        file_input.send_keys(file_path)  # Send file path instead of clicking

    def clk_submit_button(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_Submit_xpath))
        )
        element.click()

