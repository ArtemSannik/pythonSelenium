import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


# страница с расширенными настройками
class extented_filter_3(Base):

    url = 'https://www.ebay.com/'

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы
    # Введите ключевые слова или номер товара
    input_product = '//input[@id ="_nkw"]'
    input_select = '//select[@id="s0-1-17-4[0]-7[1]-_in_kw"]'
    input_choice = '//*[@id="s0-1-17-4[0]-7[1]-_in_kw"]/option[3]'
    input_select_2 = '//select[@id ="s0-1-17-4[0]-7[3]-_sacat"]'
    input_choice_item = '//*[@id="s0-1-17-4[0]-7[3]-_sacat"]/option[7]'
    # Поиск, включая
    input_checkbox_choice = '//span[@class="checkbox"]'
    input_price_min = '//input[@id ="s0-1-17-5[2]-@range-comp[]-@range-textbox[]-textbox"]'
    input_price_max = '//input[@id ="s0-1-17-5[2]-@range-comp[]-@range-textbox[]_1-textbox"]'
    # Формат покупки
    input_radio_button_choice = '//label[@for ="s0-1-17-6[3]-[2]-LH_BIN"]'
    input_radio_button_choice_2 = '//label[@for ="s0-1-17-6[4]-[0]-LH_ItemCondition"]'
    # Показать результаты
    input_checkbox_choice_2 = '/html/body/div[2]/div/main/form/fieldset[6]/div[1]/span'
    input_checkbox_choice_3 = '/html/body/div[2]/div/main/form/fieldset[6]/div[2]/span'
    # Варианты доставки
    input_delivery = '/html/body/div[2]/div/main/form/fieldset[7]/div[1]/span'
    # Местоположение
    input_location_radio_button = '//label[@for ="s0-1-17-6[7]-[3]-LH_PrefLoc"]'
    # поиск по фильтрам
    btn_search = '/html/body/div[2]/div/main/form/div[2]/button'
    main_word = '//div[@class="adv-heading__title large-text-2"]'


    # Getters
    def get_input_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_product)))

    def get_input_select(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_select)))


    def get_input_choice(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_choice)))

    def get_input_select_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_select_2)))

    def get_input_choice_item(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_choice_item)))

    def get_input_checkbox_choice(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_checkbox_choice)))

    def get_input_price_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_price_min)))

    def get_input_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_price_max)))

    def get_input_radio_button_choice(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_radio_button_choice)))

    def get_input_radio_button_choice_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_radio_button_choice_2)))

    def get_input_checkbox_choice_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_checkbox_choice_2)))

    def get_input_checkbox_choice_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_checkbox_choice_3)))

    def get_input_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_delivery)))

    def get_input_location_radio_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_location_radio_button)))

    def get_btn_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_search)))

    def get_main_words(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Setters
    def set_input_product(self, user_input):
        self.get_input_product().send_keys(user_input)
        print("Тут пишем товар который хотим")
        #


    def set_input_select(self):
        self.get_input_select().click()
        print("Тут выпадающий список с описанием ")

    def set_input_choice(self):
        self.get_input_choice().click()
        print("Тут выбираем точное описание ")

    def set_input_select_2(self):
        self.get_input_select_2().click()
        print("Тут список из категорий ")


    def set_input_choice_item(self):
        self.get_input_choice_item().click()
        print("Тут выбираем компьютеры")

    def set_input_checkbox_choice(self):
        self.get_input_checkbox_choice().click()
        print("Тут click")

    def set_input_price_min(self, user_price_min):
        self.get_input_price_min().send_keys(user_price_min)
        print("Тут пишем price min")

    def set_input_price_max(self, user_price_max):
        self.get_input_price_max().send_keys(user_price_max)
        print("Тут пишем товар price max")

    def set_input_radio_button_choice(self):
        self.get_input_radio_button_choice().click()
        print("Тут ystal click")

    def set_input_radio_button_choice_2(self):
        self.get_input_radio_button_choice_2().click()
        print("Тут click")

    def set_input_checkbox_choice_2(self):
        self.get_input_checkbox_choice_2().click()
        print("click")

    def set_input_checkbox_choice_3(self):
        self.get_input_checkbox_choice_3().click()
        print("click")

    def set_input_delivery(self):
        self.get_input_delivery().click()
        print("click")

    def set_input_location_radio_button(self):
        self.get_input_location_radio_button().click()
        print("click")

    def set_btn_search(self):
        self.get_btn_search().click()
        print("Тут click search")


    def choice_filter_3(self):
        self.get_url()
        self.get_asserts_url("https://www.ebay.com/sch/ebayadvsearch")
        print(f"получаем handle нашего активного окна {self.driver.current_window_handle}")
        self.asserts_word(self.get_main_words(), "Расширенный поиск")
        self.set_input_product("apple watch")
        self.set_input_select()
        self.set_input_choice()
        self.set_input_select_2()
        self.driver.execute_script("window.scrollBy(0,400)", "")
        self.set_input_choice_item()
        self.set_input_checkbox_choice()
        self.set_input_price_min("15000")
        self.set_input_price_max("350000")
        self.driver.execute_script("window.scrollBy(0,400)", "")
        self.set_input_radio_button_choice()
        self.set_input_radio_button_choice_2()
        self.set_input_checkbox_choice_3()
        self.set_input_delivery()
        self.set_input_location_radio_button()
        self.set_btn_search()







