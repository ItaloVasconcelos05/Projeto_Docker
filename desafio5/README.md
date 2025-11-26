# Desafio 5 — Microsserviços com API Gateway

Descrição
- Arquitetura: API Gateway centraliza acesso a dois microsserviços:
  - Gateway com rotas `/users` e `/orders` — [desafio5/gateway/app.py](desafio5/gateway/app.py) (funções [`gateway.get_users`](desafio5/gateway/app.py), [`gateway.get_orders`](desafio5/gateway/app.py)).
  - Microsserviço `users` fornece `/users` — [desafio5/users/app.py](desafio5/users/app.py) (rota [`users.users`](desafio5/users/app.py)).
  - Microsserviço `orders` fornece `/orders` — [desafio5/orders/app.py](desafio5/orders/app.py) (rota [`orders.orders`](desafio5/orders/app.py)).
- Orquestração via [desafio5/docker-compose.yml](desafio5/docker-compose.yml).

Arquitetura e decisões técnicas
- Gateway faz chamadas HTTP internas para `http://users:5001/users` e `http://orders:5002/orders`.
- Cada serviço tem Dockerfile próprio: [desafio5/gateway/Dockerfile](desafio5/gateway/Dockerfile), [desafio5/users/Dockerfile](desafio5/users/Dockerfile), [desafio5/orders/Dockerfile](desafio5/orders/Dockerfile).
- Comunicação via rede interna criada pelo Docker Compose.

Funcionamento detalhado
- Start: `docker compose up --build` na pasta `desafio5`.
- Gateway expõe porta 8080 (mapeada no compose) — acesse:
  - `http://localhost:8080/users` (roteado para [`users.users`](desafio5/users/app.py))
  - `http://localhost:8080/orders` (roteado para [`orders.orders`](desafio5/orders/app.py))

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

Melhorias sugeridas
- Implementar timeouts e tratamento de erros no gateway (`requests.get(..., timeout=...)`) para evitar bloqueios.
- Adicionar circuit breaker simples ou retry com backoff.
- Expor healthchecks e readiness probes no gateway e serviços.
- Fixar versões de base image (usar 3.11 em vez de 3.14/3.11 misturado) e pinagem de dependências.
- Considerar usar um proxy leve (Traefik/nginx) para rotação, TLS e observabilidade.

Referências de arquivos
- [desafio5/docker-compose.yml](desafio5/docker-compose.yml)
- [desafio5/gateway/app.py](desafio5/gateway/app.py) (funções: [`gateway.get_users`](desafio5/gateway/app.py), [`gateway.get_orders`](desafio5/gateway/app.py))
- [desafio5/gateway/Dockerfile](desafio5/gateway/Dockerfile)
- [desafio5/gateway/requirements.txt](desafio5/gateway/requirements.txt)
- [desafio5/users/app.py](desafio5/users/app.py) (rota: [`users.users`](desafio5/users/app.py))
- [desafio5/users/Dockerfile](desafio5/users/Dockerfile)
- [desafio5/users/requirements.txt](desafio5/users/requirements.txt)
- [desafio5/orders/app.py](desafio5/orders/app.py) (rota: [`orders.orders`](desafio5/orders/app.py))
- [desafio5/orders/Dockerfile](desafio5/orders/Dockerfile)
- [desafio5/orders/requirements.txt](desafio5/orders/requirements.txt)