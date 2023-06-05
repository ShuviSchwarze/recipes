from django.test import TestCase
from . import models


# Create your tests here.
class test_models(TestCase):
    def register_user(self, username, password):
        user = models.User(username=username, password=password)
        user.save()
        return user

    def test_register_user(self):
        user = self.register_user("test", "test")
        self.assertEqual(user.username, "test")
        self.assertEqual(user.password, "test")
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)
        self.assertEqual(user.last_login, None)
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')
        self.assertEqual(user.email, '')
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)
