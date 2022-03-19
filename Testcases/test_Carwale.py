import time

import pytest
import openpyxl

import logging

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from Testcases.BaseTest import BaseTest
from Utilities import DataProvider
from Utilities.LogUtil import Logger

# object = className(to know from which test,log level)
log = Logger(__name__,logging.INFO)


class Test_Carwale(BaseTest):

    # @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("********Inside new car test********")
        home = HomePage(self.driver)
        check_returns = home.gotoNewCars()
        check_returns.selectHyundai()


        time.sleep(10)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand, carTitle",
                             DataProvider.get_data("NewCarsTest"))
    def test_selectCars(self, carBrand,carTitle):
        log.logger.info("******Inside Car Names*********")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        print("Printing car brand:", carBrand)


        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()  # To get Car Title
            print("Car title is: "+title)
            assert title == carTitle, "Not on the correct page as title is not matching"

        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()  # To get Car Title
            print("Car title is: "+title)
            assert title == carTitle, "Not on the correct page as title is not matching"

        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()  # To get Car Title
            print("Car title is: "+title)
            assert title == carTitle, "Not on the correct page as title is not matching"

        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()  # To get Car Title
            print("Car title is: "+title)
            assert title == carTitle, "Not on the correct page as title is not matching"

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand, carTitle",
                             DataProvider.get_data("NewCarsTest"))
    def test_printCarNamesandPrices(self, carBrand,carTitle):
        log.logger.info("******Inside Car Names*********")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        print("Printing car brand:", carBrand)

        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()  # To get Car Title
            # print("Car title is: " + title)
            print(("Car title is: "+title).encode('utf8')) # This is to avoid error in Jenkins

            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()

        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()  # To get Car Title
            # print("Car title is: "+title)
            print(("Car title is: " + title).encode('utf8'))  # This is to avoid error in Jenkins
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()

        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()  # To get Car Title
            # print("Car title is: "+title)
            print(("Car title is: " + title).encode('utf8'))  # This is to avoid error in Jenkins
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()

        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()  # To get Car Title
            # print("Car title is: "+title)
            print(("Car title is: " + title).encode('utf8'))  # This is to avoid error in Jenkins
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()
            #Test GIT REPO
            #Test ammend
            #Added to check branch creation

            # Added to create merge conflict

def pytest_addoption(parser):
    parser.add

