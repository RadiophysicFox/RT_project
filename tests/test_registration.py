import pytest
from pages.auth_page import AuthPage


@pytest.mark.xfail(reason="Логотип и продуктовый слоган отсутствуют - ROS-001")
def test_find_all_elements_on_page(web_browser):
    """Проверяем, что все необходимые элементы присутствуют на странице регистрации"""

    # Открыть страницу авторизации ЛК Ростелеком
    page = AuthPage(web_browser)

    # Перейти на страницу Регистрации
    page.btn_reg.click()

    # Найти логотип в шапке страницы
    assert bool(page.logo_head) is True

    # Найти логотип в левой части страницы
    assert bool(page.logo_body) is True

    # Найти название и продуктовый слоган кабинета в левой части страницы
    assert page.title_body.get_text() == 'Личный кабинет'
    assert page.text_body.get_text() == 'Персональный помощник в цифровом мире Ростелекома'

    # Найти поле имя в правой части страницы
    assert bool(page.name) is True

    # Найти поле фамилия в правой части страницы
    assert bool(page.surname) is True

    # Найти поле регион в правой части страницы
    assert bool(page.region) is True

    # Найти поле email или мобильный телефон в правой части страницы
    assert bool(page.email) is True

    # Найти поле пароль в правой части страницы
    assert bool(page.password) is True

    # Найти поле подтверждение пароля в правой части страницы
    assert bool(page.confirm) is True

    # Найти кнопку зарегистрироваться в правой части страницы
    assert bool(page.btn_enter) is True

    # Найти пользовательское соглашение в правой части страницы
    assert bool(page.agreement_body) is True

    # Найти пользовательское соглашение в футере
    assert bool(page.agreement_footer) is True

    # Найти информацию о копирайте
    assert bool(page.copyright) is True
    assert page.copyright.get_text() == '© 2023 ПАО «Ростелеком». 18+'

    # Найти телефон службы поддержки в футере
    assert bool(page.telephone) is True
    assert page.telephone.get_text() == '8 800 100 0 800'


def test_registration_with_empty_fields(web_browser):
    """Проверяем, что при попытке регистрации с пустыми полями под каждым полем возникает соответствующая ошибка"""

    # Открыть страницу авторизации ЛК Ростелеком
    page = AuthPage(web_browser)

    # Перейти на страницу Регистрации
    page.btn_reg.click()

    # Нажать Зарегистрироваться
    page.btn_enter.click()

    # Убедиться что под каждым полем появилась ошибка
    assert page.errors.count() == 5

    # Проверить текст для каждой ошибки
    assert page.errors[0].text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    assert page.errors[1].text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    assert page.errors[2].text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    assert page.errors[3].text == 'Длина пароля должна быть не менее 8 символов'
    assert page.errors[4].text == 'Длина пароля должна быть не менее 8 символов'


def test_registration_with_email_positive_case(web_browser):
    """Проверяем, что при правильном заполнении полей оказываемся на странице подтверждения кода из письма"""

    # Открыть страницу авторизации ЛК Ростелеком
    page = AuthPage(web_browser)

    # Перейти на страницу Регистрации
    page.btn_reg.click()

    # Заполнить все поля валидными данными
    page.name.send_keys('Пользователь')
    page.surname.send_keys('Тестовый')
    page.email.send_keys('test2002@test.com')
    page.password.send_keys('20.Qwerty.2023')
    page.confirm.send_keys('20.Qwerty.2023')

    # Нажать Зарегистрироваться
    page.btn_enter.click()

    # Убедиться что мы оказались на странице с ожиданием кода из письма и сделать скриншот
    assert page.email_confirm.get_text() == 'Подтверждение email'
    page.email_confirm.highlight_and_make_screenshot(file_name='email_confirm.png')


def test_registration_with_phone_number_positive_case(web_browser):
    """Проверяем, что при правильном заполнении полей оказываемся на странице подтверждения кода из смс"""

    # Открыть страницу авторизации ЛК Ростелеком
    page = AuthPage(web_browser)

    # Перейти на страницу Регистрации
    page.btn_reg.click()

    # Заполнить все поля валидными данными
    page.name.send_keys('Пользователь')
    page.surname.send_keys('Тестовый')
    page.email.send_keys('+79003202893')
    page.password.send_keys('20.Qwerty.2023')
    page.confirm.send_keys('20.Qwerty.2023')

    # Нажать Зарегистрироваться
    page.btn_enter.click()

    # Убедиться что мы оказались на странице с ожиданием кода из смс и сделать скриншот
    assert page.email_confirm.get_text() == 'Подтверждение телефона'
    page.email_confirm.highlight_and_make_screenshot(file_name='phone_confirm.png')


def test_registration_already_registered_user(web_browser):
    """Проверяем, что при попытке регистрации уже зарегистрированного пользователя получаем соответствующее окно"""

    # Открыть страницу авторизации ЛК Ростелеком
    page = AuthPage(web_browser)

    # Перейти на страницу Регистрации
    page.btn_reg.click()

    # Заполнить все поля валидными данными уже зарегистрированного пользователя
    page.name.send_keys('Пользователь')
    page.surname.send_keys('Тестовый')
    page.email.send_keys('polzovatel.novyy.80@mail.ru')
    page.password.send_keys('23.Qwerty.2023')
    page.confirm.send_keys('23.Qwerty.2023')

    # Нажать Зарегистрироваться
    page.btn_enter.click()

    # Убедиться что появилось окно с текстом что учётная запись уже существует
    assert bool(page.already_registered_window) is True
    assert page.already_registered_text.get_text() == 'Учётная запись уже существует'

    # Убедиться что в окне присутствуют кнопки Войти и Восстановить пароль
    assert bool(page.already_registered_enter_btn) is True
    assert page.already_registered_enter_btn.get_text() == 'Войти'
    assert bool(page.already_registered_reset_btn) is True
    assert page.already_registered_reset_btn.get_text() == 'Восстановить пароль'


class TestNameField:
    def test_registration_with_name_less_than_2_symbols(self, web_browser):
        """Проверяем, что при попытке регистрации с именем менее 2 символов возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле имя 1 символ
        page.name.send_keys('Т')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[0].text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    def test_registration_with_name_more_than_30_symbols(self, web_browser):
        """Проверяем, что при попытке регистрации с именем более 30 символов возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле имя 31 символ
        page.name.send_keys('Тестертестертестертестертестерс')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[0].text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    def test_registration_with_name_with_latin_symbols(self, web_browser):
        """Проверяем, что при попытке регистрации с именем с латинскими буквами возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле имя латинские символы
        page.name.send_keys('Test')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[0].text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


class TestSurnameField:
    def test_registration_with_surname_less_than_2_symbols(self, web_browser):
        """Проверяем, что при попытке регистрации с фамилией менее 2 символов возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле фамилия 1 символ
        page.surname.send_keys('Т')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[0].text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    def test_registration_with_name_more_than_30_symbols(self, web_browser):
        """Проверяем, что при попытке регистрации с фамилией более 30 символов возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле фамилия 31 символ
        page.surname.send_keys('Тестертестертестертестертестерс')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[0].text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    def test_registration_with_name_with_latin_symbols(self, web_browser):
        """Проверяем, что при попытке регистрации с фамилией с латинскими буквами возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле фамилия латинские символы
        page.surname.send_keys('Test')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[0].text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


class TestEmailField:
    def test_registration_with_incorrect_email_format(self, web_browser):
        """Проверяем, что при попытке регистрации с некорректной почтой возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле email некорректную почту
        page.email.send_keys('exampleemail.ru')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[0].text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

    def test_registration_with_short_telephone_number(self, web_browser):
        """Проверяем, что при попытке регистрации с коротким номером телефона возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле email слишком короткий номер
        page.email.send_keys('+7980765')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[0].text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

    def test_registration_with_long_phone_number(self, web_browser):
        """Проверяем, что при попытке регистрации с длинным телефонным номером возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле email очень длинный номер
        page.email.send_keys('+37598067594373')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[0].text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'


class TestPasswordField:
    def test_registration_with_short_password(self, web_browser):
        """Проверяем, что при попытке регистрации с паролем меньше 8 символов возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле Пароль и Подтверждение Пароля - пароль меньше 8 символов
        page.password.send_keys('Q12w3E')
        page.confirm.send_keys('Q12w3E')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[3].text == 'Длина пароля должна быть не менее 8 символов'
        assert page.errors[4].text == 'Длина пароля должна быть не менее 8 символов'

    def test_registration_with_password_without_upper_letters(self, web_browser):
        """Проверяем, что при попытке регистрации с паролем без заглавных букв возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле Пароль и Подтверждение Пароля - пароль без заглавных букв
        page.password.send_keys('q12w3e4r')
        page.confirm.send_keys('q12w3e4r')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[0].text == 'Пароль должен содержать хотя бы одну заглавную букву'
        assert page.errors[1].text == 'Пароль должен содержать хотя бы одну заглавную букву'

    def test_registration_with_password_without_digits(self, web_browser):
        """Проверяем, что при попытке регистрации с паролем без цифр возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле Пароль и Подтверждение Пароля - пароль без цифр
        page.password.send_keys('QwErTyYu')
        page.confirm.send_keys('QwErTyYu')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[0].text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'
        assert page.errors[1].text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

    def test_registration_with_password_with_cyrillic_symbols(self, web_browser):
        """Проверяем, что при попытке регистрации с паролем с кириллицей возникает соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле Пароль и Подтверждение Пароля - пароль из кириллических букв
        page.password.send_keys('ТестПароль')
        page.confirm.send_keys('ТестПароль')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[3].text == 'Пароль должен содержать только латинские буквы'
        assert page.errors[4].text == 'Пароль должен содержать только латинские буквы'

    def test_registration_with_not_correct_password_confirmation(self, web_browser):
        """Проверяем, что при попытке регистрации, когда пароль не совпадает с подтверждением пароля возникает
        соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на страницу Регистрации
        page.btn_reg.click()

        # Ввести в поле Пароль и Подтверждение Пароля - разные пароли
        page.password.send_keys('1Q2w3E4r')
        page.confirm.send_keys('1Q2w3E4rt')

        # Нажать Зарегистрироваться
        page.btn_enter.click()

        # Проверить текст ошибки под полем
        assert page.errors[3].text == 'Пароли не совпадают'
