# Desafio 5 — Microsserviços com API Gateway

Descrição
- Arquitetura: API Gateway centraliza acesso a dois microsserviços:
  - Gateway com rotas `/users` e `/orders`.
  - Microsserviço `users` fornece `/users`.
  - Microsserviço `orders` fornece `/orders`.
- Orquestração via [desafio5/docker-compose.yml](desafio5/docker-compose.yml).

Arquitetura e decisões técnicas
- Gateway faz chamadas HTTP internas para `http://users:5001/users` e `http://orders:5002/orders`.
- Cada serviço tem Dockerfile próprio
- Comunicação via rede interna criada pelo Docker Compose.

Funcionamento detalhado
- Start: `docker compose up --build` na pasta `desafio5`.
- Gateway expõe porta 8080 (mapeada no compose) — acesse:
  - `http://localhost:8080/users`
  - `http://localhost:8080/orders`

Instruções de execução
1. Na pasta `desafio5`:
   - docker compose up --build
2. Testes:
   - curl http://localhost:8080/users
   - curl http://localhost:8080/orders
3. Logs:
   - docker compose logs gateway
   - docker compose logs users
   - docker compose logs orders

