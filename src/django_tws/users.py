from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager
from django.db import DEFAULT_DB_ALIAS


def user_manager() -> UserManager:
    return get_user_model()._default_manager.db_manager(DEFAULT_DB_ALIAS)
