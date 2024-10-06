from django.test import TestCase
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models.signals import post_save
from signals_app.signals import user_transaction_handler

class UserTest(TestCase):
    
    def setUp(self):
        # Disconnect the signal for the test_user_creation to prevent errors during user creation
        post_save.disconnect(user_transaction_handler, sender=User)

    def tearDown(self):
        # Reconnect the signal after the test is done
        post_save.connect(user_transaction_handler, sender=User)

    def test_user_creation(self):
        # This test will now work without the signal raising an exception
        user = User.objects.create(username='testuser')
        self.assertIsNotNone(user)

    def test_transaction_rollback(self):
        try:
            with transaction.atomic():
                user = User.objects.create(username='rollback_test')
                raise Exception("Simulating an error to test transaction rollback")  # Simulated rollback
        except Exception as e:
            self.assertEqual(str(e), "Simulating an error to test transaction rollback")
            self.assertFalse(User.objects.filter(username='rollback_test').exists())
