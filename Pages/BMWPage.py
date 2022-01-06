from Pages.BasePage import BasePage


class BMWPage(BasePage):

    def __init__(self, driver): # Calling constructor and passing driver reference
        super().__init__(driver) # Calling super class which is BasePage constructor driver
