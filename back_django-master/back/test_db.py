import sys
import psycopg2

try:
    psycopg2.connect('dbname=reclamations_at user=postgres password=0010010716 host=127.0.0.1 port=5432')
except Exception as e:
    print("ERROR:")
    print(repr(e))
    if hasattr(e, 'pgerror'):
        print("PG_ERROR:", repr(e.pgerror))
