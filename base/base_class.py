import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    # Это для проверки ЮРЛ
    def get_url(self):
        get_curret_url = self.driver.current_url
        print(f"Наш url {get_curret_url}")

    # Это для спарсивания ЮРЛ
    def get_asserts_url(self,result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f"мы спарсили, URL совпадает {result}")

    def asserts_word(self, word, result):
        get_words = word.text
        if get_words == result:
            print(f"Мы успешно зашли и спарсили со страницы:  {get_words}")
        else:
            print("Ошибка возможно отказ или не доставляют в Россию")

    def asserts_word_error(self, word, result):
        get_words = word.text
        assert get_words == result
        print(f"Мы спрасили значение и видим что товар в РФ не доставляют:  {get_words}")

    def switch_to_active_window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        print(f"переводим фокус Selenium на другой handle: {window_after}")

    def close_active_window(self):
        print("Закрываем активное окно")
        self.driver.close()

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screnn = f"screenshot{now_date}.png"
        self.driver.save_screenshot('/Users/artem/Desktop/pythonFinishProject/screen/' + name_screnn)
        print("Сделали скриншот")


