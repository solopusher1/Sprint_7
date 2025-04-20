import allure
from helpers.paths import UserAPIPaths
from helpers.user_generator import generating_user_data_without_password
from helpers.user_generator import generating_user_data_without_login

class TestCreateCourier:

    @allure.title('Создание курьера с верными данными')
    @allure.description('Создаем курьера с верными данными. запрос возвращает правильный код и текст ответа')
    def test_create_courier_positive_result(self, prepare_and_del_courier):
        response_body = '{"ok":true}'
        response = UserAPIPaths().post_v1_courier_create(data=prepare_and_del_courier)

        assert response.status_code == 201 and response_body == response.text

    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description('При попытке создать курьера с данными, которые уже есть в бд возвращается соответствующая ошибка')
    def test_request_with_duplicate_login_return_error(self, login_and_del_user):
        response = UserAPIPaths().post_v1_courier_create(data=login_and_del_user)

        assert response.status_code == 409 and 'Этот логин уже используется' in response.text

    @allure.title('Нельзя создать курьера не заполнив пароль')
    @allure.description('При попытке создать курьера не заполнив поле пароль, возвращается соответствующая ошибка')
    def test_create_courier_without_password_return_error(self):
        response = UserAPIPaths().post_v1_courier_create(data=generating_user_data_without_password())

        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Нельзя создать курьера, не заполнив поле логин')
    @allure.description('При попытке создать курьера не заполнив  логин, возвращается соответствующая ошибка')
    def test_create_courier_without_login_return_error(self):
        response = UserAPIPaths().post_v1_courier_create(data=generating_user_data_without_login())

        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text