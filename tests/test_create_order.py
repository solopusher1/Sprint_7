import pytest
import allure
import json
from helpers.paths import UserAPIPaths
from helpers.data import Order

class TestCreateOrder:

    @allure.title('Создание заказа')
    @allure.description('При создании заказа можно указать один из цветов, оба цвета, или без указания цвета. Тело ответа содержит track')
    @pytest.mark.parametrize('order_data', [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": [""]}, {"color": ["BLACK", "GREY"]}])
    def test_create_order_with_different_color_parameters_order_created(self, order_data):
        Order.data_order.update(order_data)
        order_data = json.dumps(Order.data_order)
        response = UserAPIPaths().post_v1_orders(data=order_data)

        assert response.status_code == 201 and 'track' in response.json()