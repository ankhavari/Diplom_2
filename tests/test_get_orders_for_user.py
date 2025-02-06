import requests
import allure

from utils.ingredients_data import IngredientsData
from utils.urls import URLS
from utils.handlers import Handlers

@allure.suite('Получение заказов конкретного пользователя')
class TestGetOrdersForUser:
    @allure.title('Получение заказов авторизованного пользователя')
    @allure.description('Получаем список заказов, предварительно выполнив авторизацию')
    def test_get_orders_for_user_with_auth_success(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[1]}
        requests_create_order = requests.post(f'{URLS.MAIN_URL}{Handlers.CREATE_ORDER}', headers=token,
                                              data=IngredientsData.correct_ingredient_data)
        response_get_order = requests.get(f'{URLS.MAIN_URL}{Handlers.GET_ORDER}', headers=token)
        assert requests_create_order.status_code == 200 and response_get_order.json()['orders'][0]['number'] == \
               requests_create_order.json()['order']['number']

    @allure.title('Возвращается ошибка при попытке получить список заказов у неавторизованного пользователя')
    @allure.description('Пытаемся получить список заказов, не выполняя авторизацию')
    def test_get_orders_for_user_without_auth_return_error(self):
        resp =requests.get(f'{URLS.MAIN_URL}{Handlers.GET_ORDER}')
        assert resp.status_code == 401 and resp.json()['message'] == 'You should be authorised'