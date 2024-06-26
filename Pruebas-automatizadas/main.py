# main.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from car.car_helper import CarHelper


class Main:
    def __init__(self, driver):
        self.driver = driver

    def run(self):
        car_helper = CarHelper(self.driver)
        car_helper.add_car()


if __name__ == "__main__":
    # Configurar el navegador
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/index.html")
    driver.maximize_window()

    main = Main(driver)
    main.run()

    driver.quit()
