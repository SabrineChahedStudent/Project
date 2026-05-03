import os
import sys
import django

sys.path.append(os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.tickets.models import Ticket

tickets = Ticket.objects.order_by('-created_at')[:5]
for t in tickets:
    print(f"ID: {t.id}")
    print(f"Title: {t.titre}")
    print(f"Desc: {t.description}")
    print(f"Resume: {t.resume_ia}")
    print("-" * 20)
