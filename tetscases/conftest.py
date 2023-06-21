import pytest
from selenium import webdriver
from utilities import ReadConfigurations


@pytest.fixture()
def setup1(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    #app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get("https://www.snapdeal.com/")
    request.cls.driver = driver
    yield
    driver.quit()
