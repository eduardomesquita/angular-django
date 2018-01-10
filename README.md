# angular-django

Um simples exemplo de uma aplicação [Django](https://www.djangoproject.com/) utilizando [angularJS](https://angularjs.org/) como framework front-end.

## Versões

- Python (>= 3.4.2)
- PIP (>= 9.0.1)
- MySQL (>= 14.14)
- Docker (>= 1.11.2)
- Docker Compose (>= 1.8.0)

## Ambiente Virtual Pyenv (Recomendado)

Instale o [pyenv](https://github.com/pyenv/pyenv) de acordo com sistema operacional utilizado

Para criação de um novo ambiente virtual (caso o python 3.4.2 não esteja instalado na máquina, ele irá ser baixado)
```bash
pyenv virtualenv 3.4.2 project
```

Ativando o ambiente virtual
```bash
pyenv activate project
```

## Banco de dados (MySQL)

Utilizando o docker e docker-compose:

Entre na pasta do 'docker' dentro do projeto
```bash
cd docker
```
Subindo o container do mysql
```bash
docker-compose up --build
```

## Instalando as dependências 

Na raiz do projeto execute o seguinte comando 

```bash
pip install -r requirements.txt
```

## Atualizando banco de dados (Migrate)

```bash
cd project
```
Criando as atualizações
```bash
python manage.py makemigrations core
```
Rodando as migrações no bando de dados
```bash
python manage.py migrate core
```

## Subindo servidor

Execute: 

```bash
python manage.py runserver
```

Teste:
```bash
http://127.0.0.1:8000/
```




