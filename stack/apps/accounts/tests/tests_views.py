from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        pass


    def test_create_superuser(Self):
        pass


