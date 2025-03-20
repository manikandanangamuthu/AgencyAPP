import pytest
from selenium import webdriver
from selenium.webdriver.chrome import options, service
from selenium.webdriver.chrome.options import Options

from pageObjects.LoginPage import Login




@pytest.fixture()
def setup():


     chrome_options = Options()
     #chrome_options.add_argument('--ignore-certificate-errors')
     chrome_options.add_argument("--ignore-certificate-errors")
     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
     chrome_options.add_argument("--disable-extensions")
     #driver=webdriver.Chrome()
     driver = webdriver.Chrome(options=chrome_options)
     driver.maximize_window()
     return driver