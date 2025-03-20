import time

from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import Login
from pageObjects.Upload_Company_Logo import Logo

class Test_companyLogo:


    baseURL=ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getpassword()
    logo = ReadConfig.upload_companylogo()
    Company_Name="Mani"
    #companylogo="C:\\Users\\05444\\PycharmProjects\\AgencyApp\\TestData\\company_logo.jpg"

    def test_companylogo(self,setup):

        self.driver=setup
        self.driver.get(self.baseURL) # Launching the application

        #call login page for enter username and  password and click submit button

        lp=Login(self.driver) # calling login page
        lp.setUserName(self.username) # Enter username
        lp.setPassword(self.password) # Enter Password
        lp.clickLogin() # click login button


        logo=Logo(self.driver)
        logo.clk_upload_management_button()
        logo.clk_upload_exam_logo_button()
        logo.set_company_name(self.Company_Name)
        logo.upload_company_logo()
        logo.clk_submit_button()
        time.sleep(10)







