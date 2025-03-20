
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import Login
from pageObjects.Upload_Management import upload_management

class Test_Upload_Survey:

    Baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getpassword()


    def test_upload_survey_file(self,setup):
        self.driver=setup
        self.driver.get(self.Baseurl)
        self.driver.maximize_window()


        lp = Login(self.driver)  # calling login page
        lp.setUserName(self.username)  # Enter username
        lp.setPassword(self.password)  # Enter Password
        lp.clickLogin()  # click login button

        up=upload_management(self.driver)  # calling upload management page
        up.clk_upload_management_button() # click upload management button


        






