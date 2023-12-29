<<<<<<< HEAD
# projeto_tw

projeto_tw APP from Backend Python course from EBAC
=======
# Projeto_tw

Projeto_tw APP from Backend Python course from EBAC
>>>>>>> 03473aa0deed7daa6853c4de53ca22bd8bfca512

## Prerequisites

```
Python 3.5>
Poetry
Docker && docker-compose

```

## Quickstart

1. Clone this project

   ```shell
   git clone https://github.com/KellyMY/projeto_tw.git
   ```

2. Install dependencies:

   ```shell
<<<<<<< HEAD
   cd projeto_tw
=======
   cd bookstore
>>>>>>> 03473aa0deed7daa6853c4de53ca22bd8bfca512
   poetry install
   ```

3. Run local dev server:

   ```shell
   poetry run manage.py migrate
   poetry run python manage.py runserver
   ```
   
4. Run docker dev server environment:

   ```shell
   docker-compose up -d --build 
   docker-compose exec web python manage.py migrate
   ```

5. Run tests inside of docker:

   ```shell
   docker-compose exec web python manage.py test
   ```


