
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

# Главная страничка
class main_pages(Base):

    url = 'https://www.ebay.com/'

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    btn_extended_filter = '//a[@id="gh-as-a"]'
    main_word = '//li[@class="hl-cat-nav__active"]'

    # methods
    def getter_btn_sell_day(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_extended_filter)))

    def get_main_words(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def setter_btn_sell_day(self):
        self.getter_btn_sell_day().click()
        print("Нажали на кнопку")


    def getter_btn_sell_day_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_extended_filter)))

    def get_main_words_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def setter_btn_sell_day_2(self):
        self.getter_btn_sell_day().click()
        print("Нажали на кнопку")


    def action_main_page(self):
        self.get_url()
        self.get_asserts_url("https://www.ebay.com/")
        self.asserts_word(self.get_main_words(), "Главная")
        print(f"handle нашего окна на котором фокус Selenium {self.driver.current_window_handle}")
        self.setter_btn_sell_day()

    def action_main_page_2(self):
        self.get_url()
        self.get_asserts_url("https://www.ebay.com/")
        self.asserts_word(self.get_main_words_2(), "Главная")
        print(f"handle нашего окна на котором фокус Selenium {self.driver.current_window_handle}")
        self.setter_btn_sell_day_2()

    def action_main_page_3(self):
        self.get_url()
        self.get_asserts_url("https://www.ebay.com/")
        self.asserts_word(self.get_main_words_2(), "Главная")
        print(f"handle нашего окна на котором фокус Selenium {self.driver.current_window_handle}")
        self.setter_btn_sell_day_2()