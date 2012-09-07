# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
import sys

class Command(BaseCommand):
    help = 'Load settings from json file'
    def handle(self, *args, **options):
        from ezconf import ezsettings
        original_settings = ezsettings.as_readable_json()
        ezsettings.reset_settings_with_json_data(sys.stdin.read())
        print "//** Below are original settings were overridden:\n"
        sys.stdout.write(original_settings)
