from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.title_page = (By.XPATH, "//span[@class='title']")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name' and text()= '{}']")
        self.adicionar_ao_carrinho = (By.XPATH, "//*[text()='Add to cart']")

    def verificar_login_successful(self):
        self.verificar_elemento(self.title_page)

    def adicionar_ao_carrinho(self, name_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(name_item))
        self.click(item)
        self.click(self.adicionar_ao_carrinho)
