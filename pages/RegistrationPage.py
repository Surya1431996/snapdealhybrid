import time

from selenium.webdriver.common.by import By


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    signin_link_xpath = "//*[@id='sdHeader']/div[4]/div[2]/div/div[3]/div[3]"
    reg_link_xpath = "//*[@id='sdHeader']/div[4]/div[2]/div/div[3]/div[3]/div/div/div[2]/div[2]/span[1]"
    frame_field_class_name = "userAuth-card"
    mobile_field_id = "userName"
    cont_field_id = "checkUser"
    email_field_id = "j_number"
    name_field_id = "j_name"
    dob_field_id = "j_dob"
    pass_field_id = "j_password"
    continue_button_id = "userSignup"
    otp_filed_name = "otpValue"
    otpcontinue_button_id = "registerUser"
    puz_help_id = "home_children_button"
    valid_text_xpath = "//*[@id='account-login']/div[1]"

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
        self.driver.find_element(By.XPATH, self.reg_link_xpath).click()
        time.sleep(3)

    def enter_to_frame_field(self):
        self.driver.switch_to.frame(0)

        iframe_element = self.driver.find_element(By.CLASS_NAME, self.frame_field_class_name)
        iframe_element.click()
        time.sleep(3)

    def enter_to_mob_field(self, mobile):
        self.driver.find_element("id", self.mobile_field_id).click()
        self.driver.find_element("id", self.mobile_field_id).send_keys(mobile)
        time.sleep(2)

    def enter_to_cont_field(self):
        self.driver.find_element("id", self.cont_field_id).click()
        time.sleep(2)

    def enter_to_email_field(self, email):
        self.driver.find_element("id", self.email_field_id).click()
        self.driver.find_element("id", self.email_field_id).send_keys(email)
        time.sleep(2)

    def enter_to_name_field(self, name):
        self.driver.find_element("id", self.name_field_id).click()
        self.driver.find_element("id", self.name_field_id).send_keys(name)
        time.sleep(2)

    def enter_to_dob_field(self):
        self.driver.find_element("id", self.dob_field_id).click()

        pre_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/table/thead/tr[2]/th[1]")
        nex_btn = self.driver.find_element(By.XPATH,
                                           "//div[@class='datepicker-days']//th[@class='next'][normalize-space()='»']")
        year_month = self.driver.find_element(By.XPATH, "//th[normalize-space()='June 1998']")

        while year_month.text != 'May 1996':
            pre_btn.click()
        time.sleep(3)

        dates = self.driver.find_element(By.XPATH, "//div//table//tbody//tr//td[@class='day'][text()='24']")
        dates.click()
        time.sleep(5)

    def enter_to_password_field(self, password):
        self.driver.find_element("id", self.pass_field_id).click()
        self.driver.find_element("id", self.pass_field_id).send_keys(password)
        time.sleep(2)

    def enter_to_pass_conti_field(self):
        self.driver.find_element("id", self.continue_button_id).click()
        time.sleep(2)

    def enter_to_otp_field(self, otp):
        self.driver.find_element(By.NAME, self.otp_filed_name).send_keys(otp)
        time.sleep(20)

    def enter_to_otp_conti_field(self):
        self.driver.find_element("id", self.otpcontinue_button_id).click()
        time.sleep(2)

    def enter_title1(self):
        act_title = self.driver.title

        if act_title == "Shop Online for Men, Women & Kids Clothing, Shoes, Home Decor Items":
            print("True")

        else:
            print("False")


