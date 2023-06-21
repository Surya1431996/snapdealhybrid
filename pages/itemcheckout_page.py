import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    search_name = "keyword"
    search_button_xpath = "//*[@id='sdHeader']/div[4]/div[2]/div/div[2]/button/span"
    item_xpath = "//*[@id='js-21-nav']/li[1]/a/div[1]"
    item_id = "662790784700"
    buynow_xpath = "//*[@id='buy-button-id']/span"
    login_id = "username"
    con_id = "login-continue"
    gmlogin = "gplogin"
    username_id = "identifierId"
    cont_xpath = "//*[@id='identifierNext']/div/button/span"
    pass_name = "Passwd"
    pcont_xpath = "//*[@id='passwordNext']/div/button/span"
    zip_xpath = "//input[@id='zip']"
    name_id = "fullName"
    add_id = "address"
    loc_id = "nearestLandmark"
    altmob_id = "alternateMobile"
    btn_xpath = "//*[@id='shipping-address-form']/div/div[10]/div/div[1]"
    scn_id = "delivery-modes-continue"
    paybtn_xpath = "//*[@id='make-payment']"
    cod_xpath = "//*[@id='payment-nav-id']/div[4]"
    place_xpath = "//*[@id='make-payment-button']"
    validation_xpath = "//*[@id='content_wrapper']/div[4]/div[1]/div[1]/div[2]/div/h3"
    dc_xpath = "//*[@id='payment-nav-id']/div[2]"
    dnb_xpath = "//*[@id='payment-nav-id']/div[3]"
    othbank_xpath = "//select[@id='otherNBBanks']"
    cano_xpath = "//*[@id='creditcard-payment-form']/div/div[1]/div[2]/input"
    mon1_id ="CS7"
    yy1_id ="CS8"
    mon_xpath = "//select[@name='expMonth']"
    yy_xpath="//select[@name='expYear']"
    cvv_xpath = "//*[@id='creditcard-payment-form']/div/div[3]/div[2]/div[2]/input"
    pay_xpath = "//*[@id='creditcard-continue']"
    secur_xpath = "//*[@id='securePay']"
    otp_xpath = "//*[@id='dynamicAuthOpen']"
    paym_xpath = "//div[@id='make-payment-button']"
    bank_xpath = "//*[@id='net-banking-list-AXIB-pop']"
    proc_xpath = "//*[@id='net-banking-list-AXIB-pop']/section[2]/button"

    def valid_title(self):
        act_title = "Shop Online for Men, Women & Kids Clothing, Shoes, Home Decor Items"
        if act_title == self.driver.title:
            print("True")
        else:
            print("False")

    def valid_product(self, productname):
        self.driver.find_element(By.NAME, self.search_name).click()
        time.sleep(2)
        self.driver.find_element(By.NAME, self.search_name).send_keys(productname)
        time.sleep(4)

    def search_butto(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        time.sleep(2)

    def search_item(self):

        self.driver.find_element(By.XPATH, self.item_xpath).click()
        time.sleep(2)

    def item(self):
        self.driver.find_element(By.ID, self.item_id).click()
        time.sleep(4)

    def buynow(self):
        handles = self.driver.window_handles
        parenthan = self.driver.current_window_handle
        for handle in handles:
            if handle != parenthan:
                self.driver.switch_to.window(handle)
                act_title = "Buy Laptop Skin aqua Premium vinyl HD printed Easy to Install Laptop Skin/Sticker/Vinyl/Cover for all size laptops Online at Best Price in India - Snapdeal"
                if act_title == self.driver.title:
                    print("True")
                else:
                    print("False")
                self.driver.find_element(By.XPATH, self.buynow_xpath).click()
                time.sleep(3)
                break

    def title3(self):
        act_title = "Snapdeal.com - Online shopping India- Discounts - shop Online Perfumes, Watches, sunglasses etc"
        if act_title == self.driver.title:
            print("True")
        else:
            print("False")

    def title4(self):
        act_title = "Laptop Accessories: Buy Computer & Laptop Accessories Online at Best Prices in India on Snapdeal"
        if act_title == self.driver.title:
            print("True")
        else:
            print("False")

    def title5(self):
        act_title = "Snapdeal Cart Checkout"
        if act_title == self.driver.title:
            print("True")
        else:
            print("False")

    def login(self, mob):
        self.driver.find_element(By.ID, self.login_id).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.login_id).send_keys(mob)
        time.sleep(4)

    def con(self):
        self.driver.find_element(By.ID, self.con_id).click()
        time.sleep(2)

    def glogin(self):
        self.driver.find_element(By.ID, self.gmlogin).click()
        time.sleep(2)

    def enter_to_emailfield(self, email):
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(2)
        self.driver.find_element(By.ID, self.username_id).click()
        self.driver.find_element(By.ID, self.username_id).send_keys(email)
        time.sleep(4)

    def enter_to_next(self):
        self.driver.find_element(By.XPATH, self.cont_xpath).click()
        time.sleep(5)

    def enter_to_passwordfield(self, password):
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(2)
        self.driver.find_element(By.NAME, self.pass_name).send_keys(password)
        time.sleep(2)

    def enter_to_passnext(self):
        self.driver.find_element(By.XPATH, self.pcont_xpath).click()
        time.sleep(5)

    def dapin(self, pin):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.XPATH, self.zip_xpath).clear()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.zip_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.zip_xpath).send_keys(pin)
        time.sleep(4)

    def daname(self, name):
        self.driver.find_element(By.ID, self.name_id).send_keys(name)
        time.sleep(4)

    def daaddress(self, adds):
        self.driver.find_element(By.ID, self.add_id).send_keys(adds)
        time.sleep(4)

    def dalocality(self, loc):
        self.driver.find_element(By.ID, self.loc_id).send_keys(loc)
        time.sleep(4)

    def daaltmob(self, altmob):
        self.driver.find_element(By.ID, self.altmob_id).send_keys(altmob)
        time.sleep(4)

    def daradiobtn(self):
        self.driver.find_element(By.XPATH, self.btn_xpath).click()
        time.sleep(2)

    def dasavecont(self):
        self.driver.find_element(By.ID, self.scn_id).click()
        time.sleep(4)

    def dapymbtn(self):
        self.driver.find_element(By.XPATH, self.paybtn_xpath).click()
        time.sleep(4)

    def dacod(self):
        self.driver.find_element(By.XPATH, self.cod_xpath).click()
        time.sleep(4)

    def daplc(self):
        self.driver.find_element(By.XPATH, self.place_xpath).click()
        time.sleep(4)

    def dadd(self):
        self.driver.find_element(By.XPATH, self.dc_xpath).click()
        time.sleep(4)

    def dacno(self, num):
        self.driver.find_element(By.XPATH, self.cano_xpath).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.cano_xpath).send_keys(num)
        time.sleep(4)

    def mon(self):
        #self.driver.find_element(By.ID, self.mon1_id).click()
        #time.sleep(2)
        dd = Select(self.driver.find_element(By.XPATH, self.mon_xpath))
        time.sleep(2)
        dd.select_by_value("4")

    def yy(self):
        #self.driver.find_element(By.ID, self.yy1_id).click()
        #time.sleep(2)
        dd = Select(self.driver.find_element(By.XPATH, self.yy_xpath))
        time.sleep(2)
        dd.select_by_value("26")

    def dacvv(self, num):
        self.driver.find_element(By.XPATH, self.cvv_xpath).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.cvv_xpath).send_keys(num)
        time.sleep(4)

    def dapay(self):
        self.driver.find_element(By.XPATH, self.pay_xpath).click()
        time.sleep(10)

    def dascpay(self):
        self.driver.find_element(By.XPATH, self.secur_xpath).click()
        time.sleep(10)

    def danb(self):
        self.driver.find_element(By.XPATH, self.dnb_xpath).click()
        time.sleep(4)

    def otb(self):
        #self.driver.find_element(By.ID, self.mon1_id).click()
        #time.sleep(2)
        dd = Select(self.driver.find_element(By.XPATH, self.othbank_xpath))
        time.sleep(2)
        dd.select_by_value("NKMB_N")

    def dascpa(self):
        self.driver.find_element(By.XPATH, self.paym_xpath).click()
        time.sleep(4)

    def bank(self):
        act_title = "Payment Page"
        if act_title == self.driver.title:
            print("True")
        else:
            print("False")
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.bank_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.proc_xpath).click()
        time.sleep(3)

    def banktitle(self):
        act_title = "Axis NB Payment"
        if act_title == self.driver.title:
            print("True")
        else:
            print("False")

    def codtitle(self):
        act_title = "Snapdeal Order Confirmation"
        if act_title == self.driver.title:
            print("True")
        else:
            print("False")








