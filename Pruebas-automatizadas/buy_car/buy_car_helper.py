import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.show_report import Validate


class BuyCarHelper:
    def __init__(self, driver):
        self.driver = driver
        self.fields_completed = {
            'name': False,
            'country': False,
            'city': False,
            'credit card': False,
            'month': False,
            'year': False,
        }

    def buy_car(self):
        try:
            print("Test 3")

            place_order_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][contains(.,'Place Order')]")))
            place_order_button.click()

            time.sleep(5)

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))).send_keys(
                    "Cristhian Montaño")
                self.fields_completed['name'] = True
            except TimeoutException:
                self.fields_completed['name'] = False

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'country')]"))).send_keys(
                    "Colombia")
                self.fields_completed['country'] = True
            except TimeoutException:
                self.fields_completed['country'] = False

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'city')]"))).send_keys(
                    "Bogotá")
                self.fields_completed['city'] = True
            except TimeoutException:
                self.fields_completed['city'] = False

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'card')]"))).send_keys(
                    "123456789")
                self.fields_completed['credit card'] = True
            except TimeoutException:
                self.fields_completed['credit card'] = False

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'month')]"))).send_keys(
                    "Abril")
                self.fields_completed['month'] = True
            except TimeoutException:
                self.fields_completed['month'] = False

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'year')]"))).send_keys(
                    "2024")
                self.fields_completed['year'] = True
            except TimeoutException:
                self.fields_completed['year'] = False

            validator = Validate(self.fields_completed)
            validator.showValidate()

            place_order_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][contains(.,'Purchase')]")))
            place_order_button.click()

            time.sleep(5)

            succes_buy_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//button[@class='confirm btn btn-lg btn-primary'][contains(.,'OK')]")))
            succes_buy_button.click()

            time.sleep(5)

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error al pagar los elementos del carrito: {str(e)}")
