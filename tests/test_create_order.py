import requests
import allure

from utils.urls import URLS
from utils.handlers import Handlers
from utils.ingredients_data import IngredientsData

@allure.suite('Создание пользователя')
class TestCreateOrder:

    @allure.title('Успешное создание заказа авторизованным пользователем')
    @allure.description('Создаем заказ предварительно выполнив авторизацию. Запрос возвращает правильный код ответа, \
    а ключ "success" значение "true"')
    def test_create_order_with_auth(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[1]}
        response = requests.post(f'{URLS.MAIN_URL}{Handlers.CREATE_ORDER}', headers=token,
                                 data=IngredientsData.correct_ingredient_data)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Успешное создание заказа неавторизованным пользователем')
    @allure.description('Создаем заказ не выполняя авторизацию. Запрос возвращает правильный код ответа, \
        а ключ "success" значение "true"')
    def test_create_order_without_auth(self):
        response = requests.post(f'{URLS.MAIN_URL}{Handlers.CREATE_ORDER}',
                                 data=IngredientsData.correct_ingredient_data)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Возвращается ошибка при попытке создать заказ без игредиентов')
    @allure.description('Пытаемся создать заказ без указания ингредиентов. Запрос возвращает правильный код ответа \
    и сообщение о причине ошибки')
    def test_create_order_without_ingredients(self):
        response = requests.post(f'{URLS.MAIN_URL}{Handlers.CREATE_ORDER}')
        assert response.status_code == 400 and response.json()['message'] == "Ingredient ids must be provided"

    @allure.title('Возвращается ошибка при попытке создать заказ с невалидным хэшем игредиентов')
    @allure.description('Пытаемся создать заказ с невалидным хэшем ингредиентов. \
    Запрос возвращает правильный код ответа и сообщение о причине ошибки')
    def test_create_order_with_invalid_hash_ingredients(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[1]}
        response = requests.post(f'{URLS.MAIN_URL}{Handlers.CREATE_ORDER}', headers = token,
                                 data=IngredientsData.incorrect_ingredient_data)
        assert response.status_code == 500 and 'Internal Server Error' in response.text