24/04/2026

Script em Python para consumir a [PokeAPI](https://pokeapi.co/) e salvar os dados dos 100 primeiros Pokémons em uma tabela PostgreSQL.

## O que o código faz

O arquivo `pokeapi.py`:

1. Lê credenciais de banco pelo módulo `database`.
2. Conecta em um PostgreSQL com `psycopg2`.
3. Remove e recria a tabela `pokeapi`.
4. Busca os Pokémons de `1` a `100` na PokeAPI.
5. Insere cada resposta JSON na coluna `body` (tipo `JSONB`).
6. Faz `commit` ao final.

## Requisitos

- Python 3.10+
- PostgreSQL ativo e acessível
- Pacotes Python:
  - `psycopg2-binary`
  - `requests`

Instale as dependências com:

```bash
pip install psycopg2-binary requests
```

## Configuração de credenciais

O script espera um módulo `database.py` com uma função `secrets()` retornando um dicionário com as chaves:

- `host`
- `port`
- `database`
- `user`
- `pass`

Exemplo mínimo de `database.py`:

```python
def secrets():
    return {
        "host": "localhost",
        "port": 5432,
        "database": "seu_banco",
        "user": "seu_usuario",
        "pass": "sua_senha",
    }
```

## Como executar

No diretório do projeto:

```bash
python pokeapi.py
```

Se tudo estiver certo, você verá mensagens como:

- `Pokémon 1 inserido com sucesso.`
- `Pokémon 2 inserido com sucesso.`

## Observações

- A tabela `pokeapi` é apagada e recriada em toda execução.
- Se quiser preservar dados, remova o `DROP TABLE IF EXISTS pokeapi;` do script.
