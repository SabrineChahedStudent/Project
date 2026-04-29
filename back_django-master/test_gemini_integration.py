import os
import sys

# Add the back directory to the sys path so we can import from apps
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'back')))

# Need to set DJANGO_SETTINGS_MODULE to use decouple / Django models if they are imported
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back.settings')
django.setup()

from apps.tickets.hf_triage import run_hf_triage

res = run_hf_triage("Internet ADSL", "Mon internet ne marche plus")
print("Response:", res)
