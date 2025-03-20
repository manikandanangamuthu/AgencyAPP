from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class upload_management:

    #locators
    btn_UploadManagement_LINK_TEXT = "Upload Management"

    #Constructors
    def __init__(self,setup):
        self.driver = setup # Pass the driver from test cases

    #methods
    def clk_upload_management_button(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, self.btn_UploadManagement_LINK_TEXT)))
        element.click()