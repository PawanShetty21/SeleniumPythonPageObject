

'''
- Here "BasePage" is name of the file and also class name
- All pages should extend BasePage class

'''
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Utilities import ConfigReader

import logging
from Utilities.LogUtil import Logger

# object = className(to know from which test,log level)
log = Logger(__name__,logging.INFO)

class BasePage:

    def __init__(self, driver): # Calling constructor and passing driver reference
        self.driver = driver

# Creating keyword driven flow for click, type, get title operations
# For clicking
    def click(self, locator): # Passing locator agrs to fetch from calling functions

        if str(locator).endswith("_XPATH"): # Use validation to check if the locator is Xpath, Css etc
            self.driver.find_element_by_xpath(ConfigReader.readConfig("locators", locator)).click() # Passing Section and Key
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css(ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(ConfigReader.readConfig("locators", locator)).click()
            #object.logger.info("Info" + converting into str(locator))
        log.logger.info("Clicking on an element: "+ str(locator))

# For typing
    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(ConfigReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing in an element: " + str(locator)+ "Value entered as: "+str(value))

# For Dropdown
    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element_by_xpath(ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element_by_css(ConfigReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            dropdown= self.driver.find_element_by_id(ConfigReader.readConfig("locators", locator)).send_keys(value)


        select = Select(dropdown)
        select.select_by_visible_text(value)

        log.logger.info("Selecting from an element: " + str(locator) + "Value selected as: " + str(value))

# For Move to an element
    def moveTo(self, locator):

        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element_by_xpath(ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element_by_css(ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element_by_id(ConfigReader.readConfig("locators", locator))


        action = ActionChains(self.driver)
        action.move_to_element(element)

        log.logger.info("Moving to an element: "+ str(locator))


# For suggestion box
    def selectSuggestion(self, locator):

        print("**********Inside select Suggestion**********")

        if str(locator).endswith("_XPATH"):
            suggestion = self.driver.find_elements_by_xpath(ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            suggestion = self.driver.find_elements_by_css(ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            suggestion = self.driver.find_elements_by_id(ConfigReader.readConfig("locators", locator))


        for res in suggestion:
            print(res.text)
            if "Find New Cars" == res.text:
                res.click()
                break

        log.logger.info("Selecting from suggestion: "+ str(locator))
