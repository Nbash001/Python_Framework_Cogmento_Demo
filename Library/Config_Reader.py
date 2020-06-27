import configparser

def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("./Config_Files/Config.cfg")
    return config.get(section,key)
# ./ will take you to the directory above which we need right now.


def fetchElementLocators(section, key):
    config = configparser.ConfigParser()
    config.read("./Config_Files/Elements.cfg")
    return config.get(section,key)
