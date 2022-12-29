import time
import server
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestLoginView:
    def test_login_view(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get("http://127.0.0.1:5000/")

        time.sleep(2)

        field_email = driver.find_element(By.ID, "email_field")
        field_email.send_keys("john@simplylift.co")
        time.sleep(2)
        field_email.submit()
        time.sleep(2)
        assert f"Welcome, john@simplylift.co" in driver.page_source

        driver.quit()
