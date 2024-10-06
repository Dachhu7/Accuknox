# signals_app/signals.py

import threading
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Question 1: Synchronous Execution
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal received for user: {instance.username}")

# Question 2: Same Thread Execution
@receiver(post_save, sender=User)
def user_thread_handler(sender, instance, **kwargs):
    current_thread = threading.current_thread().name
    print(f"Signal received in thread: {current_thread}")

# Question 3: Same Transaction Execution
@receiver(post_save, sender=User)
def user_transaction_handler(sender, instance, **kwargs):
    print(f"Signal received for user: {instance.username}")
    raise Exception("Simulating an error to test transaction rollback")
