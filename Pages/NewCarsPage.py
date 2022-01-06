from Pages.BasePage import BasePage


class NewCarsPage(BasePage):

    def __init__(self, driver): # Calling constructor and passing driver reference
        super().__init__(driver) # Calling super class which is BasePage constructor driver

    def selectHyundai(self):
        print("Inside selectHyundai")
        self.click("hyundai_XPATH")

    def selectToyota(self):
        self.click("toyota_XPATH")

    def selectBMW(self):
        self.click("BMW_XPATH")

    def selectHonda(self):
        self.click("honda_XPATH")