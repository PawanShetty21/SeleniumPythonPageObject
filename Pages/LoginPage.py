from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class Login(BasePage):

    def __init__(self, driver): # Calling constructor and passing driver reference
        super().__init__(driver) # Calling super class which is BasePage constructor driver



    def enterLoginDetails(self, username, password):
        self.type("username_XPATH", username)
        self.type("password_XPATH",password)


