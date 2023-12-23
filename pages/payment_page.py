
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

# Главная страничка
class payment_page(Base):

    url = 'https://www.ebay.com/'

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    buy_btn = '//*[@id="binBtn_btn_1"]'
    main_word_1 = '//*[@id="root"]/div/h1'
    main_word_2 = '//*[@id="mainContent"]/div[1]/section/div[2]/h2'

    # getters
    def get_buy_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_btn)))

    def get_main_word_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_1)))

    def get_main_word_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_2)))

    # setters
    def set_buy_btn(self):
        self.get_buy_btn().click()
        print("Нажали на кнопку покупки")

    # method iphone
    def payment_page(self):
        self.get_url()
        print(f"получаем handle нашего активного окна {self.driver.current_window_handle}")
        self.get_screenshot()
        self.set_buy_btn()
        self.asserts_word(self.get_main_word_1(), "Оформление покупки")
        self.asserts_word_error(self.get_main_word_2(), "The item you are trying to purchase is not available for purchase in your location.  You cannot buy this item.{e203421-1221669x}")
        self.get_screenshot()
        self.close_active_window()


    # method macbook
    def payment_page_2(self):
        self.get_url()
        print(f"получаем handle нашего активного окна {self.driver.current_window_handle}")
        self.get_screenshot()
        self.set_buy_btn()
        self.asserts_word(self.get_main_word_1(), "Оформление покупки")
        self.asserts_word_error(self.get_main_word_2(), "The item you are trying to purchase is not available for purchase in your location.  You cannot buy this item.{e203421-1224781x}")
        self.get_screenshot()
        self.close_active_window()



    def payment_page_3(self):
        self.get_url()
        print(f"получаем handle нашего активного окна {self.driver.current_window_handle}")
        self.get_screenshot()
        self.set_buy_btn()
        self.asserts_word(self.get_main_word_1(), "Обзор доставки")
        self.asserts_word(self.get_main_word_2(), "The item you are trying to purchase is not available for purchase in your location.  You cannot buy this item.{e203421-1224781x}")
        self.get_screenshot()
        self.close_active_window()


