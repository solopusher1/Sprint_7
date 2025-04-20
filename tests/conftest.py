import pytest
import requests
from helpers.paths import UserAPIPaths
from helpers.handle import Handle
from helpers.urls import Urls
from helpers.user_generator import register_new_courier_and_return_login_password
from helpers.user_generator import generating_user_data

@pytest.fixture(scope='function')
def login_and_del_user():
    login_pass = register_new_courier_and_return_login_password()
    resp = UserAPIPaths().post_v1_courier_login(data=login_pass)
    id_courier = resp.json()['id']
    yield login_pass
    payload ={
        "id": id_courier,
    }
    requests.delete(f'{Urls.URL}{Handle.COURIER}{id_courier}', json=payload)

@pytest.fixture(scope='function')
def prepare_and_del_courier():
    login_pass = generating_user_data()
    yield login_pass
    resp = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}', json=login_pass)
    id_courier = resp.json()['id']
    payload ={
        "id": id_courier,
    }
    requests.delete(f'{Urls.URL}{Handle.COURIER}', json=payload)