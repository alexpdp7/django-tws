import importlib
import os
import pathlib
import tempfile

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Remove devserver migrations"

    def handle(self, *args, **options):
        for app in settings.INSTALLED_APPS:
            try:
                module = importlib.import_module(f"{app}")
                module_path = pathlib.Path(module.__file__).parent
                for file in (module_path / "migrations").glob(
                    "*_devserver_migration.py"
                ):
                    file.unlink()
            except ModuleNotFoundError:
                pass
