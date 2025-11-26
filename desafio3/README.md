# Desafio 3 — Docker Compose Orquestrando Serviços

Descrição
- Solução: aplicação com 3 serviços orquestrados por Docker Compose: web (Flask), db (Postgres) e cache (Redis).

Arquitetura e decisões técnicas
- Compose define serviços: `app`, `db` (Postgres:16) e `cache` (Redis:7).
- Variáveis de ambiente: `DATABASE_URL` e `REDIS_HOST` como configurado em [desafio3/docker-compose.yml](desafio3/docker-compose.yml).
- Endpoints expostos pelo serviço `app`:
  - [`app.hello`](desafio3/app/app.py) => `/`
  - [`app.add`](desafio3/app/app.py) => `/add/<nome>`
  - [`app.listar`](desafio3/app/app.py) => `/listar`
  - [`app.show_cache`](desafio3/app/app.py) => `/cache`
- A aplicação usa `psycopg2` para Postgres e `redis` para cache.

Funcionamento detalhado
- `docker-compose up --build` cria rede interna, posta `app` em 8080.
- `app` cria tabela se necessário e escreve nomes no banco; também escreve último nome em Redis.

Instruções de execução
1. Na pasta `desafio3`:
   - docker compose up --build
2. Testes:
   - Acessar http://localhost:8080/ para saudação.
   - Adicionar nome: curl http://localhost:8080/add/Joao
   - Listar: curl http://localhost:8080/listar
   - Cache: curl http://localhost:8080/cache