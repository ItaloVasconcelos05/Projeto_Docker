# Projeto Docker

Este repositório contém uma série de desafios implementados utilizando Docker. Cada desafio é organizado em sua própria pasta, contendo a documentação, o Dockerfile e o código-fonte necessário para a execução do serviço. Abaixo está uma descrição de cada desafio.

## Estrutura do Projeto

```
projeto-docker
├── desafio1
│   ├── README.md
│   ├── Dockerfile
│   └── app
│       └── app.py
├── desafio2
│   ├── README.md
│   ├── Dockerfile
│   └── app
│       └── app.py
├── desafio3
│   ├── README.md
│   ├── Dockerfile
│   └── app
│       └── app.py
├── desafio4
│   ├── README.md
│   ├── Dockerfile
│   └── app
│       └── app.py
├── desafio5
│   ├── README.md
│   ├── gateway
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── users
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── orders
│       ├── app.py
│       ├── Dockerfile
│       └── requirements.txt
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Desafios

### Desafio 1
- **Descrição**: Este desafio implementa uma aplicação que [detalhes da funcionalidade].
- **Documentação**: Consulte [desafio1/README.md](desafio1/README.md) para mais informações.
- **Dockerfile**: Veja [desafio1/Dockerfile](desafio1/Dockerfile) para as instruções de construção da imagem.
- **Código**: O código principal está localizado em [desafio1/app/app.py](desafio1/app/app.py).

### Desafio 2
- **Descrição**: Este desafio foca em [detalhes da funcionalidade].
- **Documentação**: Consulte [desafio2/README.md](desafio2/README.md) para mais informações.
- **Dockerfile**: Veja [desafio2/Dockerfile](desafio2/Dockerfile) para as instruções de construção da imagem.
- **Código**: O código principal está localizado em [desafio2/app/app.py](desafio2/app/app.py).

### Desafio 3
- **Descrição**: Este desafio aborda [detalhes da funcionalidade].
- **Documentação**: Consulte [desafio3/README.md](desafio3/README.md) para mais informações.
- **Dockerfile**: Veja [desafio3/Dockerfile](desafio3/Dockerfile) para as instruções de construção da imagem.
- **Código**: O código principal está localizado em [desafio3/app/app.py](desafio3/app/app.py).

### Desafio 4
- **Descrição**: Este desafio implementa [detalhes da funcionalidade].
- **Documentação**: Consulte [desafio4/README.md](desafio4/README.md) para mais informações.
- **Dockerfile**: Veja [desafio4/Dockerfile](desafio4/Dockerfile) para as instruções de construção da imagem.
- **Código**: O código principal está localizado em [desafio4/app/app.py](desafio4/app/app.py).

### Desafio 5
- **Descrição**: Este desafio consiste em uma arquitetura de microsserviços com um API Gateway, centralizando o acesso a serviços de usuários e pedidos.
- **Documentação**: Consulte [desafio5/README.md](desafio5/README.md) para mais informações.
- **Gateway**: O código do gateway está em [desafio5/gateway/app.py](desafio5/gateway/app.py).
- **Serviço de Usuários**: O código do serviço de usuários está em [desafio5/users/app.py](desafio5/users/app.py).
- **Serviço de Pedidos**: O código do serviço de pedidos está em [desafio5/orders/app.py](desafio5/orders/app.py).

## Orquestração
- O arquivo [docker-compose.yml](docker-compose.yml) orquestra a execução de todos os serviços, definindo como eles interagem e se conectam dentro da rede Docker.

## Ignorar Arquivos
- O arquivo [.gitignore](.gitignore) especifica quais arquivos e diretórios devem ser ignorados pelo Git.

## Conclusão
Este projeto demonstra a utilização de Docker para implementar e orquestrar múltiplos serviços, cada um com sua própria funcionalidade e documentação. Para mais detalhes sobre cada desafio, consulte os respectivos arquivos README.