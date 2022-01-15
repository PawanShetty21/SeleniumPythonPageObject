'''

To keep common functions of the application

'''
from Utilities import ConfigReader


class CarBase:

    def __init__(self, driver):
        self.driver = driver

    def getCarTitle(self):
        return self.driver.find_element_by_xpath(ConfigReader.readConfig("locators", "car_Title_XPATH")).text

    def getCarNameAndPrice(self):
        # Adding this comments To check Jenkins auto build triggers
        # Use find_elements
        carName = self.driver.find_elements_by_xpath(ConfigReader.readConfig("locators", "carName_XPATH"))
        carPrice = self.driver.find_elements_by_xpath(ConfigReader.readConfig("locators", "carPrice_XPATH"))

        for i in range (1, len(carPrice)):

            # print(carName[i].text + " Car price is: " + carPrice[i].text)
            print((carName[i].text+" Car price is: "+carPrice[i].text).encode('utf8')) # This is to avoid error in Jenkins





