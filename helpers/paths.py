import requests
from helpers.urls import Urls
from helpers.handle import Handle

class UserAPIPaths:
    def post_v1_courier_create(self, data=None):
        url = f"{Urls.URL}{Handle.COURIER}"
        response_object = requests.post(url, json=data)
        return response_object

    def post_v1_courier_login(self, data=None):
        url = f"{Urls.URL}{Handle.LOGIN_COURIER}"
        response_object = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
        return response_object

    def get_v1_orders(self, params=None):
        url = f"{Urls.URL}{Handle.CREATE_ORDER}"
        response_object = requests.get(url, params=params)
        return response_object

    def post_v1_orders(self, data=None):
        url = f"{Urls.URL}{Handle.CREATE_ORDER}"
        response_object = requests.post(url, data=data, headers = {'Content-Type': 'application/json'})
        return response_object