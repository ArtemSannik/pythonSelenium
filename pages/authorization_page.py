import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class authorization_page(Base):

    url = 'https://www.ebay.com/'

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы
    btn_auth = '//*[@id="gh-ug"]/a'
    input_auth = '//input[@id="userid"]'
    input_pass = '//input[@id="pass"]'
    btn_continue = '//button[@id="signin-continue-btn"]'
    btn_enter = '//button[@id="sgnBt"]'
    main_word = '//*[@id="signin-reg-msg"]'
    btn_next = '//a[@id="passkeys-cancel-btn"]'
    main_word_2 = '//*[@id="gh-ug"]'

    # Getters
    def get_btn_auth(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_auth)))

    def get_main_word_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_2)))

    def get_btn_next(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_next)))

    def get_btn_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_enter)))

    def get_input_auth(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_auth)))

    def get_btn_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_continue)))


    def get_mains_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_input_pass(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_pass)))

    # Setters
    def set_btn_next(self):
        self.get_btn_next().click()
        print("Нажали на кнопку ")
    def set_btn_auth(self):
        self.get_btn_auth().click()
        print("Нажали на кнопку ")

    def set_input_auth(self,user_auth):
        self.get_input_auth().send_keys(user_auth)
        print("Написали логин")

    def set_btn_continue(self):
        self.get_btn_continue().click()
        print("Нажали на вход")

    def set_input_pass(self,user_pass):
        self.get_input_pass().send_keys(user_pass)
        print("Написали пароль")

    def set_btn_enter(self):
        self.get_btn_enter().click()
        print("Нажали на вход")


    def authorization_user_page(self):
        self.get_url()
        self.switch_to_active_window()
        self.set_btn_auth()
        self.asserts_word(self.get_mains_word(), "Войдите в eBay или создайте учетную запись")
        self.set_input_auth("test_testing2023@mail.ru")
        self.set_btn_continue()
        self.set_input_pass("testing_test")
        self.set_btn_enter()
        # self.set_btn_next()
        self.asserts_word(self.get_main_word_2(), "Здравствуйте, mamba!")

    def authorization_user_page_2(self):
        self.get_url()
        self.switch_to_active_window()
        self.set_btn_auth()
        print(f"получаем handle нашего активного окна {self.driver.current_window_handle}")
        self.asserts_word(self.get_mains_word(), "Войдите в eBay или создайте учетную запись")
        self.set_input_auth("test_testing2023@mail.ru")
        self.set_btn_continue()
        self.set_input_pass("testing_test")
        self.set_btn_enter()
        # self.set_btn_next()
        self.asserts_word(self.get_main_word_2(), "Здравствуйте, mamba!")

    def authorization_user_page_3(self):
        self.get_url()
        self.switch_to_active_window()
        self.set_btn_auth()
        print(f"получаем handle нашего активного окна {self.driver.current_window_handle}")
        self.asserts_word(self.get_mains_word(), "Войдите в eBay или создайте учетную запись")
        self.set_input_auth("test_testing2023@mail.ru")
        self.set_btn_continue()
        self.set_input_pass("testing_test")
        self.set_btn_enter()
        # self.set_btn_next()
        self.asserts_word(self.get_main_word_2(), "Здравствуйте, mamba!")