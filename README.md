# Store Server

The project for study Django.

View finished project:
   [Yaris-Store-Server](https://yaris-store-server.ru)

#### Stack:

- [Python](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python -m venv ../venv
   ```
   Linux or MacOs: ```source ../venv/bin/activate```

   Windows: ```../venv/Scripts/activate```


2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   ./manage.py migrate
   ./manage.py loaddata products/fixtures/goods.json
   ./manage.py loaddata products/fixtures/categories.json
   ./manage.py runserver 
   ```

4. Run [Redis Server](https://redis.io/docs/getting-started/installation/):
   ```bash
   redis-server
   ```

5. Run Celery:
   ```bash
   celery -A store worker --loglevel=INFO
   ```