from selenium.webdriver.common.by import By

class ElementLocators:
    LK_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p') # Кнопка "Личный кабинет"
    LOGIN_EMAIL = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input') # Поле "Email"
    LOGIN_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input') # Поле "Пароль"
    REGISTRATION_LINK = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a') # Кнопка "Зарегистрироваться"
    REGISTRATION_FORM_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input') # Поле "Имя" на форме в форме регистрации
    REGISTRATION_FORM_EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input') # Поле "Email" в форме регистрации
    REGISTRATION_FORM_PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input') # Поле "Пароль" в форме регистрации
    REGISTRATION_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button') # Кнопка "Зарегистрироваться" на странице регистрации
    REGISTRATION_FORM_LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a') # Кнопка "Войти" на странице регистрации
    MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button') # Кнопка "Войти" в аккаунт на главной странице
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a') # Кнопка "Восстановить пароль"
    RESTORE_PASSWORD_LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a') # Кнопка "Войти" на странице восстановления пароля
    CONSTRUCTOR_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p') # Кнопка "Конструктор"
    STELLAR_BURGERS_LOGO = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a') # Логотип Stellar Burgers
    EXIT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button') # Кнопка "Выход" в личном кабинете
    BUN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span') # Кнопка "Булки"
    SAUCE_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]') # Кнопка "Соусы"
    FILLING_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span') # Кнопка "Начинки"
    INVALID_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p') # Сообщение об ошибке "Некорректный пароль"
    PROFILE_NAME = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[1]/div/div/input') # Имя пользователя
    LK_LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button') # Кнопка "Войти" в личном кабинете
    OFFER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button') # Кнопка "Оформить заказ"
    ENTER_HEADER = (By.XPATH, '//*[@id="root"]/div/main/div/h2') # Заголовок "Вход"
    RESTORE_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button') # Кнопка "Восстановить"
    CONSTRUCTOR_HEADER = (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1') # Заголовок "Соберите бургер"
