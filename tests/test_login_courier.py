import allure
import pytest
from helpers.data import User
from helpers.paths import UserAPIPaths

class TestLoginCourier:

    @allure.title('Авторизация курьера с верными данными возвращает id')
    @allure.description('Проверка что логин с верными данными возвращает id')
    def test_login_courier_positive_result(self, login_and_del_user):
        response = UserAPIPaths().post_v1_courier_login(data=login_and_del_user)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Ошибка авторизации если логин или пароль неверные')
    @allure.description('Проверка что при логине с неверными данными будет 404')
    def test_login_courier_not_found_return_error(self):
        response = UserAPIPaths().post_v1_courier_login(data=User.data_incorrect)
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.text

    @allure.title('Ошибка авторизации если логин или пароль пустые')
    @allure.description('Проверка авторизации с путыми полем логина и пароля')
    @pytest.mark.parametrize('data_without_login_or_password', [User.data_without_login, User.data_without_password])
    def test_login_courier_not_all_data_return_error(self, data_without_login_or_password):
        response = UserAPIPaths().post_v1_courier_login(data=data_without_login_or_password)

        assert response.status_code == 400 and 'Недостаточно данных для входа' in response.text