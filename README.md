# Projeto S4 Suprimentos - CRUD Application

### Este projeto consiste em um Software de gestão de produtos, onde o usuário pode cadastrar e gerir produtos.

> O software está em português e o código fonte em inglês.

## Introdução:
O projeto foi desenvolvido utilizando o framework Flask com banco de dados MySQL, o banco foi criado utilizando Docker. Nesta documentação será abordado tanto a criação do software quanto como utilizá-lo.

## Requisitos:
Para poder rodar o programa em seu computador devemos ter algumas bibliotecas Python instaladas. Para instalar as bibliotecas necessárias, deve rodar o comando:
```bash
$ git clone ...
$ cd ProjetoS4Suprimentos
$ pip install -r requirements.txt
```
Para o banco de dados, devemos instalar o docker, no meu caso instalei para WSL seguindo a [Documentação do Docker][link-docker]

Além do Docker, também instalei o [DBeaver][link-dbeaver] para poder visualizar o banco de dados.

## Etapas de desenvolvimento:

### 1° Etapa: Planejamento do Software
...

### 2° Etapa: Login e Autenticação
Nesta primeira fase, o foco foi na criação de uma página de login e as páginas de usuários (os usuários e como cada um funciona será explicado mais a frente).

Como só temos dois tipos de usuários, foi criado um arquivo `users.json` para armazenar os usuários e suas senhas.

Para autenticar, foi criado um arquivo `login_autentication.py` que é chamado na `main.py` e é responssável por autenticar e validar o login do usuário.

### 3° Etapa: Criação do Banco MySQL em um Docker Container
Para a criação do banco, foi escolhido o Docker...

Após a instalação do Docker, foi criado o banco com o nome `photo_app`, que é o nome padrão do banco.

O DBeaver foi utilizado para testar conexão com o banco e ter uma melhor visualização das tabelas.

### 4° Etapa: SQLAlchemy...
...

### 5° Etapa: CRUD...
...

### 6° Etapa: Finalização das interfaces...
...

### 7° Etapa: API...
...

### 8° Etapa: Refatoração e Documentação
...

[link-docker]: https://docs.docker.com/desktop/wsl/
[link-dbeaver]: https://dbeaver.io/download/