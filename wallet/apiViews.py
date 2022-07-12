from cryptography.fernet import Fernet
from .wallet_api import WalletsClient
from .models import WalletModel
import os
from django.conf import settings
from django.utils.decorators import login_required

wallet = WalletsClient(secret_key=os.environ.get('WALLET_SECRET_KEY'), public_key=os.environ.get('WALLET_PUBLIC_KEY'))
fernet = Fernet(settings.ENCRYPTION_KEY)