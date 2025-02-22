import importlib

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load devserver data"

    def handle(self, *args, **options):
        for app in settings.INSTALLED_APPS:
            try:
                importlib.import_module(f"{app}.devserver_data")
            except ModuleNotFoundError:
                pass
