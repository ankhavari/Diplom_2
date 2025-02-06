import pytest
import requests
import allure

from utils.urls import URLS
from utils.handlers import Handlers
from utils.user_data import UserData

@allure.suite('Создание пользователя')
class TestCreateUser:
    @allure.title('Успешное создание пользователя')
    @allure.description('Создаем пользователя с валидными данными. Запрос возвращает правильный код ответа, \
    а ключ "success" значение "true"')
    def test_create_user_success(self, login_and_delete_user):
        response = requests.post(f'{URLS.MAIN_URL}{Handlers.CREATE_USER}', data=login_and_delete_user)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Нельзя создать пользователя с такими же данными')
    @allure.description('Пытаемся создать пользователя, который уже зарегистрирован. \
    Запрос возвращает правильный код ответа и сообщение о причине ошибки')
    def test_create_duplicate_user_return_error(self, ):
        response = requests.post(f'{URLS.MAIN_URL}{Handlers.CREATE_USER}', data=UserData.registered_user)
        assert response.status_code == 403 and "User already exists" in response.text

    @allure.title('Нельзя создать пользователя, не заполнив все обязательные поля')
    @allure.description('Пытаемся создать пользователя, не заполнив одно из обязательных полей. \
    Запрос возвращает правильный код ответа и сообщение о причине ошибки')
    @pytest.mark.parametrize("user_data", [UserData.generating_user_data_with_password(),
                                           UserData.generating_user_data_without_email(),
                                           UserData.generating_user_data_without_name()])
    def test_create_user_with_incorrect_data_return_error(self, user_data):
        response = requests.post(f'{URLS.MAIN_URL}{Handlers.CREATE_USER}', data=user_data)
        assert response.status_code == 403 and "Email, password and name are required fields" in response.text