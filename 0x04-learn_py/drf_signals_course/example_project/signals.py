'''
signals.py

all receivers go here
'''

# relevant imports
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
    pre_delete,
    post_delete,
    m2m_changed,
)

User = settings.AUTH_USER_MODEL

# connect the signal, method 1: pass the relevant parameters: `receiver`, `sender` etc to signal and call it
def user_created_handler_method_1():
    pass
post_save.connect(user_created_handler_method_1, sender=User)

# connect the signal, method 2: pass the relevant parameters:`signal`, `sender` etc to the `receiver` decorator
@receiver(post_save, sender=User)
def user_created_handler_method_2():
    pass