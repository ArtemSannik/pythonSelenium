
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class item_search(Base):

    url = 'https://www.ebay.com/'

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы
    item_iphone = '//*[@id="item4df9d0d2ec"]/div/div[2]/a/div/span'
    item_macbook = '//*[@id="item47129fd617"]/div/div[2]/a/div/span'
    item_watch = '//*[@id="item427a78ec27"]/div/div[2]/a/div/span'



    # Getters
    def get_item(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_iphone)))

    def get_item_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_macbook)))

    def get_item_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_watch)))

    # Setters
    def set_item(self):
        self.get_item().click()
        print("Выбрали Iphone")

    # Setters
    def set_item_2(self):
        self.get_item_2().click()
        print("Выбрали Macbook")

    def set_item_3(self):
        self.get_item_3().click()
        print("Выбрали apple watch")

    def item_search(self):
        self.get_url()
        self.get_asserts_url("https://www.ebay.com/sch/i.html?_nkw=Iphone&_in_kw=3&_sacat=15032&LH_TitleDesc=1&_udlo=15000&_udhi=150000&LH_BIN=1&LH_ItemCondition=1000&LH_RPA=1&LH_FS=1&LH_PrefLoc=2")
        print(f"получаем handle нашего активного окна {self.driver.current_window_handle}")
        self.driver.execute_script("window.scrollBy(0,100)", "")
        self.set_item()


    def item_search_2(self):
        self.get_url()
        self.get_asserts_url("https://www.ebay.com/sch/i.html?_nkw=Macbook+pro&_in_kw=3&_sacat=58058&LH_TitleDesc=1&_udlo=15000&_udhi=350000&LH_BIN=1&LH_ItemCondition=1000&LH_RPA=1&LH_FS=1&LH_PrefLoc=2")
        print(f"получаем handle нашего активного окна {self.driver.current_window_handle}")
        self.driver.execute_script("window.scrollBy(0,100)", "")
        self.set_item_2()


    def item_search_3(self):
        self.get_url()
        self.get_asserts_url("https://www.ebay.com/sch/i.html?_nkw=apple+watch&_in_kw=3&_sacat=15032&LH_TitleDesc=1&_udlo=15000&_udhi=350000&LH_BIN=1&LH_ItemCondition=1000&LH_RPA=1&LH_FS=1&LH_PrefLoc=2")
        print(f"получаем handle нашего активного окна {self.driver.current_window_handle}")
        self.driver.execute_script("window.scrollBy(0,100)", "")
        self.set_item_3()