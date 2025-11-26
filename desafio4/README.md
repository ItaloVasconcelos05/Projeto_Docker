# Desafio 4 — Microsserviços Independentes

Observação: o diretório no workspace está nomeado como `deasfio4` (provável typo). Recomenda-se renomear para `desafio4`.

Descrição
- Dois microsserviços independentes:
  - `service_A` fornece lista de usuários (rota [`service_A.users`](deasfio4/service_A/app.py)) — [deasfio4/service_A/app.py](deasfio4/service_A/app.py)
  - `service_B` consome `service_A` e combina informações (rota [`service_B.combine`](deasfio4/service_B/app.py)) — [deasfio4/service_B/app.py](deasfio4/service_B/app.py)
- Cada serviço tem Dockerfile ([deasfio4/service_A/Dockerfile](deasfio4/service_A/Dockerfile), [deasfio4/service_B/Dockerfile](deasfio4/service_B/Dockerfile)).

Arquitetura e decisões técnicas
- Comunicação HTTP direta entre serviços via nomes de container (ex: `http://servico_a:5000/users` usado em [deasfio4/service_B/app.py](deasfio4/service_B/app.py)).
- Isolamento por Dockerfile separado e imagem dedicada para cada serviço.
- Decisão: manter serviços pequenos e fáceis de entender.

Instruções de execução
1. Recomendo criar um docker-compose simples com dois serviços e rede:
   - docker-compose build
   - docker-compose up
2. Testes:
   - Acessar `service_A` /users: `curl http://localhost:5000/users` (ou porta mapeada)
   - Acessar `service_B` /combine: `curl http://localhost:6000/combine` — que chama `service_A`.

Melhorias sugeridas
- Corrigir nome do diretório para `desafio4`.
- Usar docker-compose para facilitar execução e linkagem de nomes (service discovery).
- Tratar erros de conexão em `service_B` e adicionar timeouts nas requisições `requests.get`.
- Pinagem de dependências e inclusão de healthchecks.

Referências de arquivos
- [deasfio4/service_A/app.py](deasfio4/service_A/app.py) (rota: [`service_A.users`](deasfio4/service_A/app.py))
- [deasfio4/service_A/Dockerfile](deasfio4/service_A/Dockerfile)
- [deasfio4/service_A/requirements.txt](deasfio4/service_A/requirements.txt)
- [deasfio4/service_B/app.py](deasfio4/service_B/app.py) (rota: [`service_B.combine`](deasfio4/service_B/app.py))
- [deasfio4/service_B/Dockerfile](deasfio4/service_B/Dockerfile)
- [deasfio4/service_B/requirements.txt](deasfio4/service_B/requirements.txt)