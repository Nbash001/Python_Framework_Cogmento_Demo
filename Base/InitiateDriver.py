from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import Config_Reader

def startBrowser():
    global driver

    if ((Config_Reader.readConfigData('Details','Browser')) =="chrome"):
        path = "./Driver/chromedriver"
        driver = Chrome(executable_path=path)
    elif ((Config_Reader.readConfigData('Details','Browser')) =="firefox"):
        path = "./Driver/geckodriver"
        driver = Firefox(executable_path=path)
    else:
        path = "/Users/Naveed/Downloads/chromedriver"
        driver = Chrome(executable_path=path)

    driver.get(Config_Reader.readConfigData('Details','Application_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()