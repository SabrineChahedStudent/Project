import os
import sys
import json

sys.path.append(os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from rest_framework.test import APIRequestFactory
from apps.tickets.views import MesTicketsView
from django.contrib.auth import get_user_model

User = get_user_model()
client = User.objects.filter(role='client').first()

factory = APIRequestFactory()
request = factory.get('/api/tickets/mes-tickets/')
request.user = client

view = MesTicketsView.as_view()
response = view(request)

print(json.dumps(list(response.data)[:2], indent=2))
