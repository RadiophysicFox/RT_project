from pages.auth_page import AuthPage
from selenium.webdriver.common.keys import Keys


def test_find_all_elements_on_page(web_browser):
    """Проверяем, что все необходимые элементы присутствуют на странице авторизации"""

    # Открыть страницу авторизации ЛК Ростелеком
    page = AuthPage(web_browser)

    # Найти логотип в шапке страницы
    assert bool(page.logo_head) is True

    # Найти логотип в левой части страницы
    assert bool(page.logo_body) is True

    # Найти название и продуктовый слоган кабинета в левой части страницы
    assert page.title_body.get_text() == 'Личный кабинет'
    assert page.text_body.get_text() == 'Персональный помощник в цифровом мире Ростелекома'

    # Найти таб Телефон в правой части страницы
    assert bool(page.telephone_tab) is True

    # Найти поле Мобильный телефон и проверить подсказку на нём в правой части страницы
    assert bool(page.username) is True
    assert page.texts[0].text == 'Мобильный телефон'

    # Найти поле Пароль и проверить подсказку на нём в правой части страницы
    assert bool(page.password) is True
    assert page.texts[1].text == 'Пароль'

    # Найти таб Почта в правой части страницы
    assert bool(page.email_tab) is True

    # Перейти на таб Почта
    page.email_tab.click()

    # Найти поле Электронная почта и проверить подсказку на нём в правой части страницы
    assert bool(page.username) is True
    assert page.texts[0].text == 'Электронная почта'

    # Найти поле Пароль и проверить подсказку на нём в правой части страницы
    assert bool(page.password) is True
    assert page.texts[1].text == 'Пароль'

    # Найти таб Логин в правой части страницы
    assert bool(page.login_tab) is True

    # Перейти на таб Логин
    page.login_tab.click()

    # Найти поле Логин и проверить подсказку на нём в правой части страницы
    assert bool(page.username) is True
    assert page.texts[0].text == 'Логин'

    # Найти поле Пароль и проверить подсказку на нём в правой части страницы
    assert bool(page.password) is True
    assert page.texts[1].text == 'Пароль'

    # Найти таб Лицевой счёт в правой части страницы
    assert bool(page.personal_account_tab) is True

    # Перейти на таб Лицевой счёт
    page.personal_account_tab.click()

    # Найти поле Лицевой счёт и проверить подсказку на нём в правой части страницы
    assert bool(page.username) is True
    assert page.texts[0].text == 'Лицевой счёт'

    # Найти поле Пароль и проверить подсказку на нём в правой части страницы
    assert bool(page.password) is True
    assert page.texts[1].text == 'Пароль'

    # Найти кнопку Войти в правой части страницы
    assert bool(page.btn_enter) is True

    # Найти кнопку Забыл пароль в правой части страницы
    assert bool(page.forgot_password_btn) is True

    # Найти пользовательское соглашение в правой части страницы
    assert bool(page.agreement_body) is True

    # Найти кнопку Войти с помощью VK в правой части страницы
    assert bool(page.vk_btn) is True

    # Найти кнопку Войти с помощью OK в правой части страницы
    assert bool(page.ok_btn) is True

    # Найти кнопку Войти с помощью Mail в правой части страницы
    assert bool(page.mail_btn) is True

    # Найти кнопку Войти с помощью Google в правой части страницы
    assert bool(page.google_btn) is True

    # Найти кнопку Войти с помощью Yandex в правой части страницы
    assert bool(page.yandex_btn) is True

    # Найти кнопку Зарегистрироваться в правой части страницы
    assert bool(page.btn_reg) is True

    # Найти пользовательское соглашение в футере
    assert bool(page.agreement_footer) is True

    # Найти информацию о копирайте
    assert bool(page.copyright) is True
    assert page.copyright.get_text() == '© 2023 ПАО «Ростелеком». 18+'

    # Найти телефон службы поддержки в футере
    assert bool(page.telephone) is True
    assert page.telephone.get_text() == '8 800 100 0 800'


def test_automatic_switch_tabs_on_page(web_browser):
    """Проверяем, что табы автоматически переключаются в зависимости от введённого пользователем значения для
    авторизации на странице авторизации"""

    # Открыть страницу авторизации ЛК Ростелеком
    page = AuthPage(web_browser)

    # Ввести почту в поле Мобильный телефон
    page.username.send_keys('polzovatel.novyy.80@mail.ru')

    # Перейти на поле Пароль
    page.username.send_keys(Keys.TAB)

    # Проверить что авторизация переключилась на таб Почта (к классу таба добавилось rt-tab--active)
    assert page.email_tab.get_attribute('className') == 'rt-tab rt-tab--small rt-tab--active'

    # Очистить поле Почта
    page.username.send_keys(Keys.CONTROL + "a" + Keys.DELETE)

    # Ввести телефон в поле Почта
    page.username.send_keys('+79003202893')

    # Перейти на поле Пароль
    page.username.send_keys(Keys.TAB)

    # Проверить что авторизация переключилась на таб Мобильный телефон (к классу таба добавилось rt-tab--active)
    assert page.telephone_tab.get_attribute('className') == 'rt-tab rt-tab--small rt-tab--active'

    # Очистить поле Мобильный телефон
    page.username.send_keys(Keys.CONTROL + "a" + Keys.DELETE)

    # Ввести логин в поле Мобильный телефон
    page.username.send_keys('polzovatel')

    # Перейти на поле Пароль
    page.username.send_keys(Keys.TAB)

    # Проверить что авторизация переключилась на таб Логин (к классу таба добавилось rt-tab--active)
    assert page.login_tab.get_attribute('className') == 'rt-tab rt-tab--small rt-tab--active'

    # Очистить поле Логин
    page.username.send_keys(Keys.CONTROL + "a" + Keys.DELETE)

    # Ввести почту в поле Логин
    page.username.send_keys('polzovatel.novyy.80@mail.ru')

    # Перейти на поле Пароль
    page.username.send_keys(Keys.TAB)

    # Проверить что авторизация переключилась на таб Почта (к классу таба добавилось rt-tab--active)
    assert page.email_tab.get_attribute('className') == 'rt-tab rt-tab--small rt-tab--active'

    # Очистить поле Почта
    page.username.send_keys(Keys.CONTROL + "a" + Keys.DELETE)

    # Ввести лицевой счёт в поле Почта
    page.username.send_keys('274659475645')

    # Перейти на поле Пароль
    page.username.send_keys(Keys.TAB)

    # Проверить что авторизация переключилась на таб Лицевой счёт (к классу таба добавилось rt-tab--active)
    assert page.personal_account_tab.get_attribute('className') == 'rt-tab rt-tab--small rt-tab--active'

    # Очистить поле Лицевой счёт
    page.username.send_keys(Keys.CONTROL + "a" + Keys.DELETE)

    # Ввести почту в поле Лицевой счёт
    page.username.send_keys('polzovatel.novyy.80@mail.ru')

    # Перейти на поле Пароль
    page.username.send_keys(Keys.TAB)

    # Проверить что авторизация переключилась на таб Почта (к классу таба добавилось rt-tab--active)
    assert page.email_tab.get_attribute('className') == 'rt-tab rt-tab--small rt-tab--active'

    # Очистить поле Почта
    page.username.send_keys(Keys.CONTROL + "a" + Keys.DELETE)

    # Ввести логин в поле Почта
    page.username.send_keys('polzovatel')

    # Перейти на поле Пароль
    page.username.send_keys(Keys.TAB)

    # Проверить что авторизация переключилась на таб Логин (к классу таба добавилось rt-tab--active)
    assert page.login_tab.get_attribute('className') == 'rt-tab rt-tab--small rt-tab--active'

    # Очистить поле Логин
    page.username.send_keys(Keys.CONTROL + "a" + Keys.DELETE)

    # Ввести лицевой счёт в поле Логин
    page.username.send_keys('274659475645')

    # Перейти на поле Пароль
    page.username.send_keys(Keys.TAB)

    # Проверить что авторизация переключилась на таб Лицевой счёт (к классу таба добавилось rt-tab--active)
    assert page.personal_account_tab.get_attribute('className') == 'rt-tab rt-tab--small rt-tab--active'

    # Очистить поле Лицевой счёт
    page.username.send_keys(Keys.CONTROL + "a" + Keys.DELETE)

    # Ввести логин в поле Лицевой счёт
    page.username.send_keys('polzovatel')

    # Перейти на поле Пароль
    page.username.send_keys(Keys.TAB)

    # Проверить что авторизация переключилась на таб Логин (к классу таба добавилось rt-tab--active)
    assert page.login_tab.get_attribute('className') == 'rt-tab rt-tab--small rt-tab--active'


def test_successful_authorization_with_email(web_browser):
    """Проверяем, что при успешной авторизации через Почту открывается страница личного кабинета"""

    # Открыть страницу авторизации ЛК Ростелеком
    page = AuthPage(web_browser)

    # Перейти на табу Почта
    page.email_tab.click()

    # Ввести корректные почту и пароль
    page.username.send_keys('polzovatel.novyy.80@mail.ru')
    page.password.send_keys('23.Qwerty.2023')

    # Нажать на кнопку Войти
    page.btn_enter.click()

    # Проверить что открылась страница личного кабинета и сделать скриншот
    assert bool(page.user_info) is True
    page.wait_page_loaded(sleep_time=3)
    page.user_info.highlight_and_make_screenshot(file_name='lk.png')


class TestNegativeAuthorization:
    def test_authorization_with_incorrect_email(self, web_browser):
        """Проверяем, что при попытке авторизации с некорректной почтой появляется соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на табу Почта
        page.email_tab.click()

        # Ввести некорректную почту и корректный пароль
        page.username.send_keys('polzovatel80@mail.ru')
        page.password.send_keys('23.Qwerty.2023')

        # Нажать на кнопку Войти
        page.btn_enter.click()

        # Проверить что появилась соответствующая ошибка:
        assert page.error.get_text() == 'Неверный логин или пароль'

        # Проверить что кнопка Забыл пароль выделилась рыжим цветом (значение класса кнопки изменилось с
        # login-form__forgot-pwd--muted на login-form__forgot-pwd--animated)
        assert page.forgot_password_btn.get_attribute('className') == 'rt-link rt-link--orange login-form__forgot-pwd' \
                                                                      ' login-form__forgot-pwd--animated'

    def test_authorization_with_incorrect_password(self, web_browser):
        """Проверяем, что при попытке авторизации с некорректным паролем появляется соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Перейти на табу Почта
        page.email_tab.click()

        # Ввести корректную почту и некорректный пароль
        page.username.send_keys('polzovatel.novyy.80@mail.ru')
        page.password.send_keys('23.Qwerty')

        # Нажать на кнопку Войти
        page.btn_enter.click()

        # Проверить что появилась соответствующая ошибка:
        assert page.error.get_text() == 'Неверный логин или пароль'

        # Проверить что кнопка Забыл пароль выделилась рыжим цветом (значение класса кнопки изменилось с
        # login-form__forgot-pwd--muted на login-form__forgot-pwd--animated)
        assert page.forgot_password_btn.get_attribute('className') == 'rt-link rt-link--orange login-form__forgot-pwd' \
                                                                      ' login-form__forgot-pwd--animated'

    def test_authorization_with_incorrect_phone(self, web_browser):
        """Проверяем, что при попытке авторизации с некорректным телефоном появляется соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Выполнить успешную регистрацию и выйти чтобы не запрашивался код картинки от многочисленных попыток
        # некорректной авторизации
        page.email_tab.click()
        page.username.send_keys('polzovatel.novyy.80@mail.ru')
        page.password.send_keys('23.Qwerty.2023')
        page.btn_enter.click()
        page.logout_btn.click()

        # Ввести некорректный телефон и корректный пароль
        page.username.send_keys('+79003202893')
        page.password.send_keys('23.Qwerty.2023')

        # Нажать на кнопку Войти
        page.btn_enter.click()

        # Проверить что появилась соответствующая ошибка:
        assert page.error.get_text() == 'Неверный логин или пароль'

        # Проверить что кнопка Забыл пароль выделилась рыжим цветом (значение класса кнопки изменилось с
        # login-form__forgot-pwd--muted на login-form__forgot-pwd--animated)
        assert page.forgot_password_btn.get_attribute(
            'className') == 'rt-link rt-link--orange login-form__forgot-pwd' \
                            ' login-form__forgot-pwd--animated'

    def test_authorization_with_incorrect_login(self, web_browser):
        """Проверяем, что при попытке авторизации с некорректным логином появляется соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Выполнить успешную регистрацию и выйти чтобы не запрашивался код картинки от многочисленных попыток
        # некорректной авторизации
        page.email_tab.click()
        page.username.send_keys('polzovatel.novyy.80@mail.ru')
        page.password.send_keys('23.Qwerty.2023')
        page.btn_enter.click()
        page.logout_btn.click()

        # Перейти на табу Логин
        page.login_tab.click()

        # Ввести некорректный логин и корректный пароль
        page.username.send_keys('polzovatel')
        page.password.send_keys('23.Qwerty.2023')

        # Нажать на кнопку Войти
        page.btn_enter.click()

        # Проверить что появилась соответствующая ошибка:
        assert page.error.get_text() == 'Неверный логин или пароль'

        # Проверить что кнопка Забыл пароль выделилась рыжим цветом (значение класса кнопки изменилось с
        # login-form__forgot-pwd--muted на login-form__forgot-pwd--animated)
        assert page.forgot_password_btn.get_attribute('className') == 'rt-link rt-link--orange login-form__forgot-pwd' \
                                                                      ' login-form__forgot-pwd--animated'

    def test_authorization_with_incorrect_personal_account(self, web_browser):
        """Проверяем, что при попытке авторизации с некорректным лицевым счётом появляется соответствующая ошибка"""

        # Открыть страницу авторизации ЛК Ростелеком
        page = AuthPage(web_browser)

        # Выполнить успешную регистрацию и выйти чтобы не запрашивался код картинки от многочисленных попыток
        # некорректной авторизации
        page.email_tab.click()
        page.username.send_keys('polzovatel.novyy.80@mail.ru')
        page.password.send_keys('23.Qwerty.2023')
        page.btn_enter.click()
        page.logout_btn.click()

        # Перейти на табу Лицевой счёт
        page.personal_account_tab.click()

        # Ввести некорректный логин и корректный пароль
        page.username.send_keys('274659475645')
        page.password.send_keys('23.Qwerty.2023')

        # Нажать на кнопку Войти
        page.btn_enter.click()

        # Проверить что появилась соответствующая ошибка:
        assert page.error.get_text() == 'Неверный логин или пароль'

        # Проверить что кнопка Забыл пароль выделилась рыжим цветом (значение класса кнопки изменилось с
        # login-form__forgot-pwd--muted на login-form__forgot-pwd--animated)
        assert page.forgot_password_btn.get_attribute('className') == 'rt-link rt-link--orange login-form__forgot-pwd' \
                                                                      ' login-form__forgot-pwd--animated'











