from faker import Faker

class UserData:
    @staticmethod
    # метод возвращает словарь со сгенерированными данными для email, пароля и имени
    def generating_user_data():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.name()
        reg_data = {"email": email, "password": password, "name": name}
        return reg_data

    # метод возвращает словарь со сгенерированными данными для пароля и имени
    @staticmethod
    def generating_user_data_without_email():
        fake = Faker()
        password = fake.password()
        name = fake.name()
        reg_data = {"password": password, "name": name}
        return reg_data

    @staticmethod
    def generating_user_data_with_password():
        fake = Faker()
        email = fake.email()
        name = fake.name()
        reg_data = {"email": email, "name": name}
        return reg_data

    @staticmethod
    def generating_user_data_without_name():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        reg_data = {"email": email, "password": password}
        return reg_data

    registered_user = {
        "email": "viking@yandex.ru",
        "password": "Viking123",
        "name": "Viking",
    }