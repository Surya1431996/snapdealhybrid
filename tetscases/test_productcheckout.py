import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from utilities.customlogger import LogGen
from pages.itemcheckout_page import ProductPage


@pytest.mark.usefixtures("setup1")
class TestLogin:
    logger = LogGen.Loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_with_all_validproductcod(self):
        self.logger.info("*****************Test valid product with cod  started****************************")
        product_page = ProductPage(self.driver)
        product_page.valid_title()
        product_page.valid_product("Laptops")
        product_page.search_butto()
        product_page.title3()
        product_page.search_item()
        product_page.title4()
        product_page.item()
        product_page.buynow()
        product_page.title5()
        product_page.glogin()
        product_page.enter_to_emailfield("ast984904@gmail.com")
        product_page.enter_to_next()
        product_page.enter_to_passwordfield("surya@123")
        product_page.enter_to_passnext()
        product_page.dapin("201307")
        product_page.daname("surya teja")
        product_page.daaddress("403, isthara pg, morna, sector 35, Noida")
        product_page.dalocality("near hospital")
        product_page.daaltmob("9560432706")
        product_page.daradiobtn()
        product_page.dasavecont()
        product_page.dapymbtn()
        product_page.dacod()
        product_page.daplc()
        product_page.codtitle()
        self.logger.info("*****************Text is valid****************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_with_all_productpaymentdebitcard(self):
        self.logger.info("*****************Test valid product with cod  started****************************")
        product_page = ProductPage(self.driver)
        product_page.valid_title()
        product_page.valid_product("Laptops")
        product_page.search_butto()
        product_page.title3()
        product_page.search_item()
        product_page.title4()
        product_page.item()
        product_page.buynow()
        product_page.title5()
        product_page.glogin()
        product_page.enter_to_emailfield("ast984904@gmail.com")
        product_page.enter_to_next()
        product_page.enter_to_passwordfield("surya@123")
        product_page.enter_to_passnext()
        product_page.dapin("201307")
        product_page.daname("surya teja")
        product_page.daaddress("403, isthara pg, morna, sector 35, Noida")
        product_page.dalocality("near hospital")
        product_page.daaltmob("9560432706")
        product_page.daradiobtn()
        product_page.dasavecont()
        product_page.dapymbtn()
        product_page.dadd()
        product_page.dacno("5260990218592810")
        product_page.mon()
        product_page.yy()
        product_page.dacvv("861")
        product_page.dapay()
        self.logger.info("*****************Text is valid****************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_with_all_registeredfieldnetb(self):
        self.logger.info("*****************Test valid product with cod  started****************************")
        product_page = ProductPage(self.driver)
        product_page.valid_title()
        product_page.valid_product("Laptops")
        product_page.search_butto()
        product_page.title3()
        product_page.search_item()
        product_page.title4()
        product_page.item()
        product_page.buynow()
        product_page.title5()
        product_page.glogin()
        product_page.enter_to_emailfield("ast984904@gmail.com")
        product_page.enter_to_next()
        product_page.enter_to_passwordfield("surya@123")
        product_page.enter_to_passnext()
        product_page.dapin("201307")
        product_page.daname("surya teja")
        product_page.daaddress("403, isthara pg, morna, sector 35, Noida")
        product_page.dalocality("near hospital")
        product_page.daaltmob("9560432706")
        product_page.daradiobtn()
        product_page.dasavecont()
        product_page.dapymbtn()
        product_page.danb()
        product_page.otb()
        product_page.dascpa()
        product_page.bank()
        product_page.banktitle()
        self.logger.info("*****************Text is valid****************************")
