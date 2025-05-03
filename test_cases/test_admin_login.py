import time

import pytest
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_config
from base_pages.Login_Admin_Page import Login_Admin_Page
from selenium import webdriver



class Test_01_Admin_Login:
    admin_page_url = Read_config.get_admin_page_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invlid_username = Read_config.get_invalidpassword()


    def test_title_verification(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(10)
        act_dashboard_text = self.driver.find_element(By.XPATH,"//div[@class='content-header']").text
        if act_dashboard_text == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False

    def test_invalid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invlid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(5)
        error_message = self.driver.find_element(By.XPATH,"//li").text
        if error_message == "The credentials provided are incorrect":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()

