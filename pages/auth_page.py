from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    name = WebElement(name='firstName')

    surname = WebElement(name='lastName')

    email = WebElement(id='address')

    password = WebElement(id='password')

    confirm = WebElement(id='password-confirm')

    btn_enter = WebElement(class_name='rt-btn')

    btn_reg = WebElement(id='kc-register')

    errors = ManyWebElements(class_name='rt-input-container__meta--error')

    logo_head = WebElement(class_name='rt-logo main-header__logo')

    logo_body = WebElement(class_name='rt-logo what-is-container__logo')

    title_body = WebElement(class_name='what-is__title')

    text_body = WebElement(class_name='what-is__desc')

    region = WebElement(xpath='//div[2]/div/div/input')

    agreement_body = WebElement(xpath='//div[5]/a')

    agreement_footer = WebElement(id='rt-footer-agreement-link')

    copyright = WebElement(xpath='//*[@id="app-footer"]/div[1]/div[1]')

    telephone = WebElement(class_name='rt-footer-right__support-phone')

    email_confirm = WebElement(class_name='card-container__title')

    already_registered_window = WebElement(class_name='card-modal__card-wrapper')

    already_registered_text = WebElement(class_name='card-modal__title')

    already_registered_enter_btn = WebElement(name='gotoLogin')

    already_registered_reset_btn = WebElement(id='reg-err-reset-pass')

    telephone_tab = WebElement(id='t-btn-tab-phone')

    email_tab = WebElement(id='t-btn-tab-mail')

    login_tab = WebElement(id='t-btn-tab-login')

    forgot_password_btn = WebElement(id='forgot_password')

    vk_btn = WebElement(id='oidc_vk')

    ok_btn = WebElement(id='oidc_ok')

    mail_btn = WebElement(id='oidc_mail')

    google_btn = WebElement(id='oidc_google')

    yandex_btn = WebElement(id='oidc_ya')

    personal_account_tab = WebElement(id='t-btn-tab-ls')

    username = WebElement(id='username')

    texts = ManyWebElements(class_name='rt-input__placeholder')

    user_info = WebElement(class_name='user-info__name-container')

    error = WebElement(id='form-error-message')

    logout_btn = WebElement(id='logout-btn')


