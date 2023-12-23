import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.authorization_page import authorization_page
from pages.extented_filter import extented_filter
from pages.extented_filter_2 import extented_filter_2
from pages.extented_filter_3 import extented_filter_3
from pages.main_pages import main_pages
from pages.payment_page import payment_page
from pages.item_search import item_search

def test_buy_iphone_pages(set_group, set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    options.page_load_strategy = 'eager'
    base_url = 'https://www.ebay.com/'
    driver.get(base_url)
    driver.maximize_window()

    print("начало теста c Iphone")

    # Метод главной страницы
    m_pages = main_pages(driver)
    m_pages.action_main_page()

    # Метод расширенного поиска
    e_filter = extented_filter(driver)
    e_filter.choice_filter()

    # Метод поиска айфона
    i_search = item_search(driver)
    i_search.item_search()

    # метод авторизации
    print(f"список всех наших handle: {driver.window_handles}")
    a_user = authorization_page(driver)
    a_user.authorization_user_page()

    # метод покупки
    print(f"список всех наших handle: {driver.window_handles}")
    p_page = payment_page(driver)
    p_page.payment_page()

    print("конец теста с Iphone")

def test_buy_mackbook_pages(set_group, set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    options.page_load_strategy = 'eager'
    base_url = 'https://www.ebay.com/'
    driver.get(base_url)
    driver.maximize_window()

    print("начало теста c macbook")

    # Метод главной страницы
    m_pages = main_pages(driver)
    m_pages.action_main_page_2()

    # Метод расширенного поиска
    e_filter = extented_filter_2(driver)
    e_filter.choice_filter_2()

#     # Метод поиска макбука
    i_search = item_search(driver)
    i_search.item_search_2()

    # метод авторизации
    print(f"список всех наших handle: {driver.window_handles}")
    a_user = authorization_page(driver)
    a_user.authorization_user_page_2()

    # метод покупки
    print(f"список всех наших handle: {driver.window_handles}")
    p_page = payment_page(driver)
    p_page.payment_page_2()

    print("конец теста с macbook")


def test_buy_apple_watch_pages(set_group, set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    options.page_load_strategy = 'eager'
    base_url = 'https://www.ebay.com/'
    driver.get(base_url)
    driver.maximize_window()

    print("начало теста c apple watch")

    # Метод главной страницы
    m_pages = main_pages(driver)
    m_pages.action_main_page_3()

    # Метод расширенного поиска
    e_filter = extented_filter_3(driver)
    e_filter.choice_filter_3()

#     # Метод поиска макбука
    i_search = item_search(driver)
    i_search.item_search_3()

    # метод авторизации
    print(f"список всех наших handle: {driver.window_handles}")
    a_user = authorization_page(driver)
    a_user.authorization_user_page_3()

    # метод покупки
    print(f"список всех наших handle: {driver.window_handles}")
    p_page = payment_page(driver)
    p_page.payment_page_3()

    print("конец теста с apple watch")