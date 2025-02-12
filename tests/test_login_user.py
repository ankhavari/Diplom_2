import pytest
import requests
import allure

from utils.urls import URLS
from utils.handlers import Handlers
from utils.user_data import UserData

@allure.suite('Логин пользователя')
class TestLoginUser:
    @allure.title('Успешная авторизация пользователя')
    @allure.description('Выполняем авторизацию с корректными данными. Запрос возвращает правильный код ответа, \
    а ключ "success" значение "true"')
    def test_login_user_success_result(self):
        response = requests.post(f'{URLS.MAIN_URL}{Handlers.LOGIN_USER}', data=UserData.registered_user)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.title('Возвращается ошибка при попытке авторизации с невалидными данными')
    @allure.description('Пытаемся авторизоваться, заполнив одно из обязательных полей некорректными данными. \
    Запрос возвращает правильный код ответа, а ключ "success" значение "false"')
    @pytest.mark.parametrize("user_data", [UserData.generating_user_data_with_password(),
                                           UserData.generating_user_data_without_email(),
                                           UserData.generating_user_data_without_name()])
    def test_login_user_with_incorrect_data_return_error(self, user_data):
        response = requests.post(f'{URLS.MAIN_URL}{Handlers.LOGIN_USER}', data=user_data)
        assert response.status_code == 401 and response.json().get('success') == False