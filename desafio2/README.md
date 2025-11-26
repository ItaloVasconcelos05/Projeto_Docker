# Desafio 2 — Volumes e Persistência

Descrição
- Solução: script Python que usa SQLite e armazena banco em volume persistente.
- Arquivos: [`app` script](desafio2/app.py) ([desafio2/app.py](desafio2/app.py)), [desafio2/Dockerfile](desafio2/Dockerfile).

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

Melhorias sugeridas
- Usar um entrypoint que rode o app e exponha logs.
- Adicionar testes automáticos que verificam presença de registros após recriação.
- Para produção, usar PostgreSQL em vez de SQLite quando houver concorrência.
- Incluir instruções com comando `docker run -v $(pwd)/data:/data ...` para testes locais.

Referências de arquivos
- [desafio2/app.py](desafio2/app.py)
- [desafio2/Dockerfile](desafio2/Dockerfile)