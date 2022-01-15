from datetime import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Utilities import ConfigReader


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# To take screenshot of failed test cases
@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


# @pytest.fixture(params=["chrome", "firefox"], scope="class") # with chrome and firefox
# For class level execution
# @pytest.fixture(params=["chrome"], scope="class")
@pytest.fixture(params=["chrome"], scope="function")
def get_browser(request):
    if request.param == "chrome":
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(executable_path = '../PageObjectModelFramework/Drivers/chromedriver')

    # if request.param == "firefox":
    #     # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    #     driver = webdriver.Firefox(executable_path='/Users/admin/PycharmProjects/PageObjectModelFramework/Drivers/geckodriver')

    request.cls.driver = driver

    # driver.get("https://www.facebook.com/") # To directly pass the url
    driver.get(ConfigReader.readConfig("basic info", "testURL"))  # To pass url from Conftest using ConfigReader
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver  # returning driver
    driver.quit()
