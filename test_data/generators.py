import random
import string
from dataclasses import dataclass


class DataGenerator:
    """Класс для генерации тестовых данных"""

    @staticmethod
    def random_string(length: int = 10) -> str:
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    @staticmethod
    def random_email() -> str:
        username = DataGenerator.random_string(8)
        domain = DataGenerator.random_string(5)
        return f"{username}@{domain}.com"

    @staticmethod
    def random_password(length: int = 12) -> str:
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

    @staticmethod
    def random_phone() -> str:
        return f"+7{''.join(random.choices(string.digits, k=10))}"


@dataclass
class UserData:
    """Структура данных пользователя"""
    email: str
    password: str

    @classmethod
    def create_random(cls):
        return cls(
            email=DataGenerator.random_email(),
            password=DataGenerator.random_password()
        )