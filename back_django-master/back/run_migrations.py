import os
import sys
import django
from django.core.management import call_command

sys.path.append(os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

print("Running makemigrations...")
call_command('makemigrations', 'tickets')
print("Running migrate...")
call_command('migrate', 'tickets')
print("Done!")
