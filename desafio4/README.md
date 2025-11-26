# Desafio 4 — Microsserviços Independentes

Descrição
- Dois microsserviços independentes:
  - `service_A` fornece lista de usuários 
  - `service_B` consome `service_A` e combina informações 

Arquitetura e decisões técnicas
- Comunicação HTTP direta entre serviços via nomes de container.
- Isolamento por Dockerfile separado e imagem dedicada para cada serviço.
- Decisão: manter serviços pequenos e fáceis de entender.

Instruções de execução
1. Recomendo criar um docker-compose simples com dois serviços e rede:
   - docker-compose build
   - docker-compose up
2. Testes:
   - Acessar `service_A` /users: `curl http://localhost:5000/users` (ou porta mapeada)
   - Acessar `service_B` /combine: `curl http://localhost:6000/combine` — que chama `service_A`.
