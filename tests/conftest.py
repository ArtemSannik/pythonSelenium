import pytest

@pytest.fixture()
def set_up():
    print("Начало теста модуля добавления товара в корзину")
    yield
    print("Конец теста модуля ")


@pytest.fixture(scope='module')
def set_group():
    print("Вошли в систему")
    yield
    print("Вышли из системы")
