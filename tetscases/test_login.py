import pytest
from selenium import webdriver
import time
from utilities.customlogger import LogGen
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup1")
class TestLogin:
    logger = LogGen.Loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_with_all_registeredfield(self):
        self.logger.info("*****************TestLogin mandatory fileds started****************************")
        login_page = LoginPage(self.driver)
        login_page.valid_title()
        self.logger.info("*****************Title is valid****************************")
        login_page.enter_to_sigin_page()
        login_page.enter_to_register_page()
        login_page.enter_to_frame_field()
        login_page.enter_to_mob_field("ast98490@gmail.com")
        login_page.enter_to_cont_field()

        wrnmsg = "Please enter verification code (OTP) sent to:"
        assert self.driver.find_element(By.XPATH, "//*[@id='login-register-modal']/div/div[8]/div[2]/p").text.__eq__(
            wrnmsg)
        print("True")
        self.logger.info("*****************Text is valid****************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_with_all_notregistermail(self):
        self.logger.info("*****************TestLogin not registered fileds started****************************")
        login_page = LoginPage(self.driver)
        login_page.valid_title()
        self.logger.info("*****************Title is valid****************************")
        login_page.enter_to_sigin_page()
        login_page.enter_to_register_page()
        login_page.enter_to_frame_field()
        login_page.enter_to_mob_field("asshahi1991@gmail.com")
        login_page.enter_to_cont_field()

        wrnmsg = "Create an account on Snapdeal"
        assert self.driver.find_element(By.XPATH, "//*[@id='login-register-modal']/div/div[10]/div[1]/p").text.__eq__(
            wrnmsg)
        print("True")
        self.logger.info("*****************Text is valid****************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_with_all_invalidmail(self):
        self.logger.info("*****************TestLogin invalid mail fileds started****************************")
        login_page = LoginPage(self.driver)
        login_page.valid_title()
        self.logger.info("*****************Title is valid****************************")
        login_page.enter_to_sigin_page()
        login_page.enter_to_register_page()
        login_page.enter_to_frame_field()
        login_page.enter_to_mob_field("assha")
        login_page.enter_to_cont_field()

        wrnmsg = "Please enter a valid mobile number or email"
        assert self.driver.find_element(By.ID, "userName-error").text.__eq__(wrnmsg)

        print("True")
        self.logger.info("*****************Text is valid****************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_with_all_emptyfields(self):
        self.logger.info("*****************TestLogin all empty fileds started****************************")
        login_page = LoginPage(self.driver)
        login_page.valid_title()
        self.logger.info("*****************Title is valid****************************")
        login_page.enter_to_sigin_page()
        login_page.enter_to_register_page()
        login_page.enter_to_frame_field()
        login_page.enter_to_mob_field(" ")
        login_page.enter_to_cont_field()

        wrnmsg = "Please enter your mobile number or email"
        assert self.driver.find_element(By.ID, "userName-error").text.__eq__(wrnmsg)

        print("True")
        self.logger.info("*****************Text is valid****************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_with_usinggoogle(self):
        self.logger.info("*****************TestLogin with google mail started****************************")
        login_page = LoginPage(self.driver)
        login_page.valid_title()
        self.logger.info("*****************Title is valid****************************")
        login_page.enter_to_sigin_page()
        login_page.enter_to_register_page()
        login_page.enter_to_frame_field()
        login_page.enter_to_google_field()
        login_page.enter_to_emailfield("ast98490441@gmail.com")
        login_page.enter_to_next()
        login_page.enter_to_passwordfield("surya@123")
        login_page.enter_to_passnext()
        login_page.enter_to_titlefield()
        self.logger.info("*****************Title is valid****************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_with_usingregistergoogle(self):
        self.logger.info("*****************TestLogin with register google mail started****************************")
        login_page = LoginPage(self.driver)
        login_page.valid_title()
        self.logger.info("*****************Title is valid****************************")
        login_page.enter_to_sigin_page()
        login_page.enter_to_register_page()
        login_page.enter_to_frame_field()
        login_page.enter_to_google_field()
        login_page.enter_to_emailfield("ast98490441@gmail.com")
        login_page.enter_to_next()
        login_page.enter_to_passwordfield("surya@123")
        login_page.enter_to_passnext()
        login_page.enter_to_valid_titlefield()
        self.logger.info("*****************Title is valid****************************")
