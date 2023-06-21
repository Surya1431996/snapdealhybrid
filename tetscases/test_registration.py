from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

from pages.RegistrationPage import RegistrationPage


@pytest.mark.usefixtures("setup1")
class TestRegister:
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_with_all_fields(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teja05863@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("8985209431")
        registration_page.enter_to_name_field("surya")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("Surya@143")
        registration_page.enter_to_pass_conti_field()
        wrnmsg = "Please enter verification code (OTP) sent to:"
        assert self.driver.find_element(By.XPATH, "//*[@id='login-register-modal']/div/div[10]/div[2]/p").text.__eq__(
            wrnmsg)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_invalid_email(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teja05863@gmail")
        wrnmsg = "Please enter a valid mobile number or email"
        assert self.driver.find_element(By.ID, "userName-error").text.__eq__(wrnmsg)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_registered_email(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("ast98490@gmail.com")
        registration_page.enter_to_cont_field()

        wrnmsg = "Please enter verification code (OTP) sent to:"
        assert self.driver.find_element(By.XPATH, "//*[@id='login-register-modal']/div/div[8]/div[2]/p").text.__eq__(
            wrnmsg)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_invalid_mobile_no(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teju89011@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("898520943")
        registration_page.enter_to_name_field("surya")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("Surya@143")
        registration_page.enter_to_pass_conti_field()

        wrnmsg = "Please enter a valid mobile number"
        assert self.driver.find_element(By.ID, "j_number-error").text.__eq__(wrnmsg)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_registered_mobile_no(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teju89011@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("9560432706")
        registration_page.enter_to_name_field("surya")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("Surya@143")
        registration_page.enter_to_pass_conti_field()
        wrnmsg = "An account already exists with +91 9560432706"
        assert self.driver.find_element(By.ID, "signup-message").text.__eq__(wrnmsg)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_invalid_name(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teju89011@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("8985209431")
        registration_page.enter_to_name_field("s")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("Surya@143")
        registration_page.enter_to_pass_conti_field()

        wrnmsg = "Please enter a valid name"
        assert self.driver.find_element(By.ID, "j_name-error").text.__eq__(wrnmsg)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_invalid_password(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teju89011@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("8985209431")
        registration_page.enter_to_name_field("surya")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("Surya")
        registration_page.enter_to_pass_conti_field()

        wrnmsg = "Please enter a valid password"
        assert self.driver.find_element(By.ID, "j_password-error").text.__eq__(wrnmsg)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_valid_mobileno_invalidnameandinvalidpassword(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teju89011@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("8985209431")
        registration_page.enter_to_name_field("")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("")
        registration_page.enter_to_pass_conti_field()

        wrnmsg = "Please enter your name"
        assert self.driver.find_element(By.ID, "j_name-error").text.__eq__(wrnmsg)
        print("True")
        wrnmsg1 = "Please enter a password"
        assert self.driver.find_element(By.ID, "j_password-error").text.__eq__(wrnmsg1)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_invalid_mobileno_validnameandinvalidpassword(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teju89011@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("")
        registration_page.enter_to_name_field("surya")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("")
        registration_page.enter_to_pass_conti_field()

        wrnmsg = "Please enter a mobile number"
        assert self.driver.find_element(By.ID, "j_number-error").text.__eq__(wrnmsg)
        print("True")
        wrnmsg1 = "Please enter a password"
        assert self.driver.find_element(By.ID, "j_password-error").text.__eq__(wrnmsg1)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_invalid_mobileno_invalidnameandvalidpassword(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teju89011@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("")
        registration_page.enter_to_name_field("")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("surya123")
        registration_page.enter_to_pass_conti_field()

        wrnmsg = "Please enter a mobile number"
        assert self.driver.find_element(By.ID, "j_number-error").text.__eq__(wrnmsg)
        print("True")
        wrnmsg1 = "Please enter your name"
        assert self.driver.find_element(By.ID, "j_name-error").text.__eq__(wrnmsg1)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_valid_mobileno_validnameandinvalidpassword(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teju89011@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("8985209431")
        registration_page.enter_to_name_field("surya")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("")
        registration_page.enter_to_pass_conti_field()

        wrnmsg1 = "Please enter a password"
        assert self.driver.find_element(By.ID, "j_password-error").text.__eq__(wrnmsg1)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_valid_mobileno_invalidnameandvalidpassword(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teju89011@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("8985209431")
        registration_page.enter_to_name_field("")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("surya123")
        registration_page.enter_to_pass_conti_field()

        wrnmsg = "Please enter your name"
        assert self.driver.find_element(By.ID, "j_name-error").text.__eq__(wrnmsg)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_invalid_mobileno_validnameandvalidpassword(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teju89011@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("")
        registration_page.enter_to_name_field("surya")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("surya123")
        registration_page.enter_to_pass_conti_field()

        wrnmsg = "Please enter a mobile number"
        assert self.driver.find_element(By.ID, "j_number-error").text.__eq__(wrnmsg)
        print("True")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_with_empty_fields(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.enter_to_sigin_page()
        registration_page.enter_to_register_page()
        registration_page.enter_to_frame_field()
        registration_page.enter_to_mob_field("teja05863@gmail.com")
        registration_page.enter_to_cont_field()
        registration_page.enter_to_email_field("")
        registration_page.enter_to_name_field("")
        registration_page.enter_to_dob_field()
        registration_page.enter_to_password_field("")
        registration_page.enter_to_pass_conti_field()
        wrnmsg = "Please enter a mobile number"
        assert self.driver.find_element(By.ID, "j_number-error").text.__eq__(wrnmsg)
        print("True")
        wrnmsg1 = "Please enter your name"
        assert self.driver.find_element(By.ID, "j_name-error").text.__eq__(wrnmsg1)
        print("True")
        wrnmsg2 = "Please enter a password"
        assert self.driver.find_element(By.ID, "j_password-error").text.__eq__(wrnmsg2)
        print("True")










