from email.policy import default
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from register.models import CustomUser
import uuid



class WalletModel(models.Model):
    id = uuid.uuid4(default=uuid.uuid4, editable=False, primary_key=True )
    user = models.OneToOneField('CustomUser', on_delete=models.SET_NULL)
    balance = models.DecimalField(decimal_places=2, max_digits=100)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100)

    