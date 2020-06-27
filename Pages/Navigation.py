from Library import Config_Reader
from selenium.webdriver import Chrome

class NavigationClass:
#contructer will set it to global
    def __init__(self, obj):
        global driver
        driver = obj

    def click_Home(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "home_link")).click()

    def click_Calendar(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "calendar_link")).click()

    def click_Contacts(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "contacts_link")).click()

    def click_Companies(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "companies_link")).click()

    def click_Deals(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "deals_link")).click()

    def click_Tasks(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "tasks_link")).click()

    def click_Cases(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "cases_link")).click()

    def click_Calls(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "calls_link")).click()

    def click_Documents(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "documents_link")).click()

    def click_Email(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "email_link")).click()

    def click_Campaigns(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "campaigns_link")).click()

    def click_Forms(self):
        driver.find_element_by_link_text(Config_Reader.fetchElementLocators("Navigation", "forms_link")).click()
