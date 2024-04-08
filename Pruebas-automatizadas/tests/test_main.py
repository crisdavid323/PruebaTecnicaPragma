import unittest
import os
from selenium import webdriver
from buy_car.buy_car_helper import BuyCarHelper
from car.car_helper import CarHelper
import HtmlTestRunner
from show_car.show_car_helper import ShowCarHelper


class TestMain(unittest.TestCase):
    items_to_add = ["//a[contains(.,'Samsung galaxy s6')]", "//a[contains(.,'Nokia lumia 1520')]",
                    "//a[contains(.,'Sony vaio i5')]", "//a[contains(.,'Nexus 6')]", "//a[contains(.,'Iphone 6 32gb')]"]

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.demoblaze.com/index.html")
        cls.driver.maximize_window()

    def test_1_add_to_cart(self):
        car_helper = CarHelper(self.driver, self.items_to_add)
        car_helper.add_car()

    def test_2_show_to_cart(self):
        show_car_helper = ShowCarHelper(self.driver, len(self.items_to_add))
        show_car_helper.show_car()

    def test_3_buy_to_cart(self):
        buy_car_helper = BuyCarHelper(self.driver)
        buy_car_helper.buy_car()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    # Obtener la ruta absoluta del directorio de informes
    reports_dir = os.path.abspath("../reportsDoc")
    # Ejecutar las pruebas y generar un informe HTML en la ubicación especificada
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=reports_dir))
