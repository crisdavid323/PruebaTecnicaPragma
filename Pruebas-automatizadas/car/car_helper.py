import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CarHelper:
    def __init__(self, driver, items_to_add):
        self.driver = driver
        self.items_to_add = items_to_add

    def add_car(self):
        try:
            # Seleccionar elementos para agregar al carrito

            print("Test 1")
            for item in self.items_to_add:
                itemTemp = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, item)))
                item_name = item
                itemTemp.click()

                # Esperar a que el botón "Add to cart" esté disponible
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[@href='#'][contains(.,'Add to cart')]")))

                # Hacer clic en el botón "Add to cart"
                add_to_cart_button = self.driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Add to cart')]")
                add_to_cart_button.click()

                try:
                    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
                    alert = self.driver.switch_to.alert
                    alert_text = alert.text

                    # Aceptar la alerta
                    alert.accept()

                except NoAlertPresentException:
                    print("No se encontró una alerta presente")

                print(f"Producto '{item_name}' agregado al carrito")

                # Esperar un segundo antes de volver a la página anterior
                time.sleep(2)

                # Volver a la página anterior
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//a[@class='nav-link'][contains(.,'Home (current)')]"))).click()

                time.sleep(3)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, 0)")
            time.sleep(2)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error al agregar elementos al carrito: {str(e)}")
