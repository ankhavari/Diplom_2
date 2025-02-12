import requests
import allure
from utils.text_constants import TextConstants
from utils.urls import URLS
from utils.handlers import Handlers
from utils.user_data import UserData

@allure.suite('Изменение данных пользователя')
class TestChangingUserData:

    @allure.title('Изменение email авторизованного пользователя')
    @allure.description('Редактируем email у авторизованного пользователя, запрос возвращает правильный код ответа')
    def test_change_user_email_with_auth(self, create_and_delete_user):
        payload = {'email': UserData.generating_user_data()['email']}
        token = {'Authorization': create_and_delete_user[1]}
        resp = requests.patch(f'{URLS.MAIN_URL}{Handlers.USER_DATA}', headers=token, json=payload)
        assert resp.status_code == 200 and resp.json()['user']['email'] == payload["email"]

    @allure.title('Изменение пароля авторизованного пользователя')
    @allure.description('Редактируем пароль у авторизованного пользователя, запрос возвращает правильный код ответа')
    def test_change_password_with_auth(self, create_and_delete_user):
        payload = {'password': UserData.generating_user_data()['password']}
        token = {'Authorization': create_and_delete_user[1]}
        resp = requests.patch(f'{URLS.MAIN_URL}{Handlers.USER_DATA}', headers=token, json=payload)
        assert resp.status_code == 200 and resp.json().get("success") is True

    @allure.title('Изменение имени авторизованного пользователя')
    @allure.description('Редактируем имя у авторизованного пользователя, запрос возвращает правильный код ответа')
    def test_change_user_name_with_auth(self, create_and_delete_user):
        payload = {'name': UserData.generating_user_data()['name']}
        token = {'Authorization': create_and_delete_user[1]}
        resp = requests.patch(f'{URLS.MAIN_URL}{Handlers.USER_DATA}', headers=token, json=payload)
        assert resp.status_code == 200 and resp.json()['user']['name'] == payload["name"]

    @allure.title('Возвращается ошибка при попытке изменить данные у неавторизованного пользователя')
    @allure.description(
        'При попытке редактирования данных у неавторизованного пользователя, возвращается соответствующая ошибка')
    def test_change_user_dara_without_auth_return_error(self):
        resp = requests.patch(f'{URLS.MAIN_URL}{Handlers.USER_DATA}', headers=UserData.generating_user_data())
        assert resp.status_code == 401 and resp.json()['message'] == TextConstants.authorization_error