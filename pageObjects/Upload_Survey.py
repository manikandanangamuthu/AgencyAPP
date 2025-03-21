import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class survey:

    #locators
    btn_upload_survey_xpath="//a[normalize-space()='Upload Survey']"
    file_btn_xpath="//input[@id='flFileName']"
    btn_upload_xpath="//input[@value='Upload']"
    #constructors
    def __init__(self,setup):
        self.driver = setup # Pass the driver from test cases

    #Methods
    def clk_upload_management_button(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, self.btn_UploadManagement_LINK_TEXT)))
        element.click()

    def clk_upload_survey_button(self):

        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.btn_upload_survey_xpath)))
        element.click()

    def clk_CSV_File(self):
        file_path = "C:\\Users\\05444\\PycharmProjects\\AgencyApp\\TestData\\Survey_UPLOAD_ENG.csv"
        # file_path = os.path.abspath(f"testData/{companylogo}")  # Dynamic file path
        file_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.file_btn_xpath))
        )
        file_input.send_keys(file_path)

    def clk_upload_btn(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.btn_upload_xpath)))
        element.click()

