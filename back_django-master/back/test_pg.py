import os
import sys

sys.path.append(os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from apps.tickets.models import Ticket

tickets = Ticket.objects.order_by('-created_at')[:5]
for t in tickets:
    print(f"ID: {t.id} | Titre: {t.titre} | Resume: {repr(t.resume_ia)}")
