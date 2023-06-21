import time
from turtle import title

from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    signin_link_xpath = "//*[@id='sdHeader']/div[4]/div[2]/div/div[3]/div[3]"
    login_link_xpath = "//*[@id='sdHeader']/div[4]/div[2]/div/div[3]/div[3]/div/div/div[2]/div[2]/span[2]/a"
    frame_field_class_name = "userAuth-card"
    mobile_field_id = "userName"
    cont_field_id = "checkUser"
    google_id = "googleUserLogin"
    username_id = "identifierId"
    cont_xpath = "//*[@id='identifierNext']/div/button/span"
    pass_name = "Passwd"
    pcont_xpath = "//*[@id='passwordNext']/div/button/span"
    validation_xpath = "//*[@id='login-register-modal']/div/div[10]/div[1]/p"

    def valid_title(self):
        act_title = "Shop Online for Men, Women & Kids Clothing, Shoes, Home Decor Items"
        if act_title == self.driver.title:
            print("True")
        else:
            print("False")

    def enter_to_sigin_page(self):
        self.driver.find_element(By.XPATH, self.signin_link_xpath).click()
        time.sleep(3)

    def enter_to_register_page(self):
        self.driver.find_element(By.XPATH, self.login_link_xpath).click()
        time.sleep(3)

    def enter_to_frame_field(self):
        self.driver.switch_to.frame(0)

        # iframe_element = self.driver.find_element(By.CLASS_NAME, self.frame_field_class_name)
        # iframe_element.click()
        time.sleep(3)

    def enter_to_mob_field(self, mobile):
        self.driver.find_element("id", self.mobile_field_id).click()
        self.driver.find_element("id", self.mobile_field_id).send_keys(mobile)
        time.sleep(2)

    def enter_to_cont_field(self):
        self.driver.find_element("id", self.cont_field_id).click()
        time.sleep(2)

    def enter_to_google_field(self):
        self.driver.find_element("id", self.google_id).click()
        time.sleep(2)

    def enter_to_emailfield(self, email):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.driver.find_element("id", self.username_id).click()
        self.driver.find_element("id", self.username_id).send_keys(email)
        time.sleep(4)

    def enter_to_next(self):
        self.driver.find_element(By.XPATH, self.cont_xpath).click()
        time.sleep(5)

    def enter_to_passwordfield(self, password):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.driver.find_element(By.NAME, self.pass_name).send_keys(password)
        time.sleep(2)

    def enter_to_passnext(self):
        self.driver.find_element(By.XPATH, self.pcont_xpath).click()
        time.sleep(5)

    def enter_to_titlefield(self):

        wrnmsg = "Create an account on Snapdeal"
        assert self.driver.find_element(By.XPATH, self.validation_xpath).__eq__(wrnmsg)


        print("True")

    def enter_to_valid_titlefield(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)

        act_title = "Shop Online for Men, Women & Kids Clothing, Shoes, Home Decor Items"
        if act_title == self.driver.title:
            print("True")
        else:
            print("False")




