from Library import Config_Reader
from selenium.webdriver.support.select import Select

class LoginClass:
#contructer will set it to global
    def __init__(self, obj):
        global driver
        driver = obj
#logging in process
    def enter_email(self, email):
        driver.find_element_by_name(Config_Reader.fetchElementLocators("Login", "email_name")).send_keys(
            email)

    def enter_password(self, password):
        driver.find_element_by_name(Config_Reader.fetchElementLocators("Login", "password_name")).send_keys(
            password)

    def click_login_button(self):
        driver.find_element_by_xpath(Config_Reader.fetchElementLocators("Login", "login_button_xpath")).click()

#logging out process
    def click_settings_button(self):
        # object = Select(driver.find_element_by_class_name('settings icon'))
        # object.select_by_visible_text("Logout")
        driver.find_element_by_css_selector(Config_Reader.fetchElementLocators("Login", "settings_button_css")).click()

    def click_logout_button(self):
        driver.find_element_by_xpath(Config_Reader.fetchElementLocators("Login", "logout_button_xpath")).click()
