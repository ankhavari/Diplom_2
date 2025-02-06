import pytest
import requests

from utils.handlers import Handlers
from utils.urls import URLS
from utils.user_data import UserData

@pytest.fixture(scope='function')
def login_and_delete_user():
    payload = UserData.generating_user_data()
    yield payload
    resp = requests.post(f'{URLS.MAIN_URL}{Handlers.LOGIN_USER}', json=payload)
    token = resp.json()['accessToken']
    requests.delete(f'{URLS.MAIN_URL}{Handlers.USER_DATA}', headers={'Authorization': f'{token}'})

@pytest.fixture(scope='function')
def create_and_delete_user():
    payload = UserData.generating_user_data()
    resp = requests.post(f'{URLS.MAIN_URL}{Handlers.CREATE_USER}', json=payload)
    token = resp.json()['accessToken']
    yield payload, token
    requests.delete(f'{URLS.MAIN_URL}{Handlers.USER_DATA}', headers={'Authorization': f'{token}'})