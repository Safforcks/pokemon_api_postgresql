import psycopg2
import database
import requests
import json

secretos = database.secrets()

conn = psycopg2.connect(
    port=secretos["port"],
    host=secretos["host"],
    database=secretos["database"],
    user=secretos["user"],
    password=secretos["pass"],
    connect_timeout=3
)

cur = conn.cursor()

sql = """
DROP TABLE IF EXISTS pokeapi;
CREATE TABLE IF NOT EXISTS pokeapi (id INTEGER, body JSONB);
"""
print(sql)
cur.execute(sql)

for i in range(1, 101):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        data = resposta.json()
        sql = "INSERT INTO pokeapi (id, body) VALUES (%s, %s)"
        cur.execute(sql, (i, json.dumps(data)))
        print(f"Pokémon {i} inserido com sucesso.")
    else:
        print(f"Erro ao obter dados do Pokémon {i}: {resposta.status_code}")

conn.commit()
