# Desafio 2 — Volumes e Persistência

Descrição
- Solução: script Python que usa SQLite e armazena banco em volume persistente.

Arquitetura e decisões técnicas
- SQLite como banco leve para demonstrar persistência.
- O container cria `/data/banco.db` (via script [desafio2/app.py](desafio2/app.py)).
- Persistência via volume Docker montado em `/data`.

Funcionamento detalhado
- Script [desafio2/app.py](desafio2/app.py) cria tabela e insere registro.
- Dockerfile simples em [desafio2/Dockerfile](desafio2/Dockerfile).

Instruções de execução
1. Build:
   - docker build -t desafio2-app desafio2
2. Rodar com volume:
   - docker run --name desafio2 -v desafio2-data:/data desafio2-app
3. Remover container e recriar para provar persistência:
   - docker rm -f desafio2
   - docker run --name desafio2 -v desafio2-data:/data desafio2-app
4. Verificar `/data/banco.db` no volume (via container debug ou mount local).

