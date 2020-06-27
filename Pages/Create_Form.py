from Library import Config_Reader
from selenium.webdriver import Chrome

class Create_Form_Class:
#contructer will set it to global
    def __init__(self, obj):
        global driver
        driver = obj

    def click_New_button(self):
        driver.find_element_by_xpath(Config_Reader.fetchElementLocators("Create_Form", "new_button_xpath")).click()

    def enter_name(self, name):
        driver.find_element_by_name(Config_Reader.fetchElementLocators("Create_Form", "enter_name_name")).send_keys(
            name)

    def enter_intro_text(self, intro):
        driver.find_element_by_name(Config_Reader.fetchElementLocators("Create_Form", "enter_intro_name")).send_keys(
            intro)

    def enter_completion_text(self, outro):
        driver.find_element_by_name(Config_Reader.fetchElementLocators("Create_Form", "enter_completion_name")).send_keys(
            outro)

    def click_Save_button(self):
        driver.find_element_by_xpath(Config_Reader.fetchElementLocators("Create_Form", "save_button_xpath")).click()

    def click_Submit_button(self):
        driver.find_element_by_xpath(Config_Reader.fetchElementLocators("Create_Form", "submit_button_xpath")).click()
