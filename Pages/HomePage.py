import time

from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):

    def __init__(self, driver): # Calling constructor and passing driver reference
        super().__init__(driver) # Calling super class which is BasePage constructor driver

    def gotoNewCars(self):
        # self.moveTo("newCars_Button_XPATH")
        self.click("newCars_Button_XPATH")
        time.sleep(3)
        self.selectSuggestion("findNewCars_Elements_XPATH")

        # return the function which is responsible to get next page(To achieve chaining)
        return NewCarsPage(self.driver)

    def gotoCompareCars(self):
        pass

    def gotoUsedCars(self):
        pass