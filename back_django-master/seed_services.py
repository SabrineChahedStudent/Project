import os
import sys
import django

sys.path.append(os.path.abspath('back'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.tickets.models import TypeService

types = [
    {'id': 1, 'code': 'ADSL', 'libelle': 'Internet ADSL', 'priorite_defaut': 2},
    {'id': 2, 'code': 'FIBER', 'libelle': 'Internet Fiber', 'priorite_defaut': 2},
    {'id': 3, 'code': 'FIXE', 'libelle': 'Téléphonie Fixe', 'priorite_defaut': 2},
    {'id': 4, 'code': '4GLTE', 'libelle': '4G LTE', 'priorite_defaut': 2},
    {'id': 5, 'code': 'IPTV', 'libelle': 'IPTV', 'priorite_defaut': 2},
    {'id': 6, 'code': 'AUTRE', 'libelle': 'Autre', 'priorite_defaut': 2},
]

created_count = 0
for t in types:
    obj, created = TypeService.objects.get_or_create(id=t['id'], defaults=t)
    if created:
        created_count += 1
        print(f"Created TypeService: {t['libelle']}")

print(f"Total created: {created_count}")
