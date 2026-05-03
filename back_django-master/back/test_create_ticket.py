import os
import sys

sys.path.append(os.path.abspath('.'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()

from apps.tickets.serializers import CreerTicketSerializer
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory
import json

User = get_user_model()
client = User.objects.filter(role='client').first()

factory = APIRequestFactory()
request = factory.post('/api/tickets/mes-tickets/', {
    'titre': 'Test AI Summary',
    'description': 'Mon internet ne marche pas',
    'type_service': 1,
    'historique_ia': 'Client: Internet is broken\nAssistant: Did you restart?\nClient: Yes it is still broken'
}, format='json')
request.user = client

serializer = CreerTicketSerializer(data=request.data, context={'request': request})
if serializer.is_valid():
    ticket = serializer.save()
    print("Ticket ID:", ticket.id)
    print("Resume IA generated:", ticket.resume_ia)
else:
    print("ERRORS:", serializer.errors)
