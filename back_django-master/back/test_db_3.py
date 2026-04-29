import psycopg2

try:
    conn = psycopg2.connect('dbname=postgres user=postgres password=0010010716 host=127.0.0.1 port=5432 sslmode=disable')
    print("SUCCESS")
except Exception as e:
    print(repr(e))
