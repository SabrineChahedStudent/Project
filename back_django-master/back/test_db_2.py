import psycopg2

try:
    psycopg2.connect('host=127.0.0.1 port=12345')
except Exception as e:
    print(repr(e))
