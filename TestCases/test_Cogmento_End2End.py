from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import Config_Reader
from Pages import Login_Page
from Pages import Navigation
from Pages import Create_Form
import pytest
import time


def test_Login():
    driver = InitiateDriver.startBrowser()
#Logging in
    login = Login_Page.LoginClass(driver)
    login.enter_email('PyTestUser001@gmail.com')
    login.enter_password('PyTestPass')
    login.click_login_button()

#Navigating Left Hand Nav
    nav = Navigation.NavigationClass(driver)
    time.sleep(3)
    nav.click_Home()
    nav.click_Calendar()
    nav.click_Contacts()
    nav.click_Companies()
    nav.click_Deals()
    nav.click_Tasks()
    nav.click_Cases()
    nav.click_Calls()
    nav.click_Documents()
    nav.click_Email()
    nav.click_Campaigns()
    nav.click_Forms()

#Creating Form
    form = Create_Form.Create_Form_Class(driver)
    form.click_New_button()
    form.enter_name('Mr. PyTest')
    form.enter_intro_text('Nice to meet you!')
    form.enter_completion_text('See you next time!')
    form.click_Save_button()
    time.sleep(3)
    #form.click_Submit_button()

# Logging out
    login = Login_Page.LoginClass(driver)
    login.click_settings_button()
    time.sleep(3)
    login.click_logout_button()

#  def test_Navigation():
#      driver = InitiateDriver.startBrowser()
#     nav = Navigation.NavigationClass(driver)
#     time.sleep(5)
#     nav.click_Home()
#     nav.click_Calendar()
#     nav.click_Companies()
#     nav.click_Deals()

# def test_Valid_login():
#     driver = InitiateDriver.startBrowser()
#     driver.find_element_by_name(Config_Reader.fetchElementLocators("Login","email_name")).send_keys("PyTestUser001@gmail.com")
#     driver.find_element_by_name(Config_Reader.fetchElementLocators("Login","password_name")).send_keys("PyTestPass")
#     driver.find_element_by_xpath("//div[contains(text(),'Login')]").click()
#     time.sleep(3)
#     assert driver.title == "Cogmento CRM"
#     driver.close()

# @pytest.fixture(scope="module")
# def env_test_setup():
# global driver
# path = "/Users/Naveed/Downloads/chromedriver"
# driver = Chrome(executable_path=path)
# driver.get("https://ui. cogmento.com/")
# driver.maximize_window()
#
# def test_valid_login_credentials():
#     driver.find_element_by_name("email").send_keys("PyTestUser001@gmail.com")
#     driver.find_element_by_name("password").send_keys("PyTestPass")
#     driver.find_element_by_xpath("//div[contains(text(),'Login')]").click()
#     time.sleep(3)
#     assert driver.title == "Cogmento CRM"
#
# def test_invalid_login_credentials():
#     driver.find_element_by_name("email").send_keys("FakeEmail@gmail.com")
#     driver.find_element_by_name("password").send_keys("FakePass")
#     driver.find_element_by_xpath("//div[contains(text(),'Login')]").click()
#     assert driver.find_element_by_name("email").is_displayed()
#
# time.sleep(5)