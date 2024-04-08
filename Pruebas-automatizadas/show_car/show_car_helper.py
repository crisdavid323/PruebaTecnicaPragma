import time
import random
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShowCarHelper:
    def __init__(self, driver, itemCant: int):
        self.driver = driver
        self.itemCant = itemCant

    def show_car(self):
        try:
            print("Test 2")

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[@class='nav-link'][contains(.,'Cart')]"))).click()
            time.sleep(5)

            id = random.randint(1, self.itemCant)
            delete = "(//a[@href='#'][contains(.,'Delete')])[" + str(id) + "]"
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, delete))).click()

            print(f"Producto '{id}' se elimino del carrito")
            time.sleep(5)

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error al eliminar elementos del carrito: {str(e)}")
