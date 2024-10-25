import pytest
from selenium.webdriver.common.by import By

class TestLoginPage:
    def elementsById(self,driver,username, password):
        driver.get("https://www.saucedemo.com/")

        user_input = driver.find_element(By.ID, "user-name")
        user_input.send_keys(username)

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)

        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()

    def test_valid_login(self, driver):
        self.elementsById( driver,"standard_user","secret_sauce")

        #URL Validation
        actual_url = driver.current_url #get url
        assert actual_url == "https://www.saucedemo.com/inventory.html"


    @pytest.mark.parametrize("username, password, error", [
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ("invalidUser", "invalidPass", "Epic sadface: Username and password do not match any user in this service")])
    def test_invalid_login(self,driver, username, password, error):
        self.elementsById(driver,username, password)

        error_mesg_h3 = driver.find_element(By.TAG_NAME,"h3")
        error_mesg_text = error_mesg_h3.text

        assert error_mesg_text == error
