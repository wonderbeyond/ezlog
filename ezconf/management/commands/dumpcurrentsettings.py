# coding=utf-8
'''Dump current settings to json'''
from django.core.management.base import BaseCommand, CommandError
import sys

class Command(BaseCommand):
    help = 'Dump current ezsettings as json'
    def handle(self, *args, **options):
        from ezconf import ezsettings
        sys.stdout.write(ezsettings.as_readable_json().encode('utf-8'))

