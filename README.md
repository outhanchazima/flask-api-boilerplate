# flask-api-boilerplate
Flask API starter project

## Requirements

- Python 3.8.5 and above
- Postgres 13 and above
- Redis Server

## Usage
### Part One
Intiallizing postgres database
```
CREATE USER boilerplate WITH PASSWORD 'boilerplate';
CREATE DATABASE boilerplate;
GRANT ALL PRIVILEGES ON DATABASE boilerplate TO boilerplate;
```
### Part Two: Termial commands
Clone the repo:

```bash
git clone 
```
Change directory
```
cd flask-api-boilerplate
```

#### Alternative 1
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests
`
    To run application: make run

    To run all commands at once : make all

Make sure to run the initial migration commands to update the database.
    
    > python3 manage.py db init

    > python3 manage.py db migrate --message 'initial database migration'

    > python3 manage.py db upgrade

#### Alternative 2
Create virtualenv:
```
python3 -m venv .venv
```
Activate the virtual environment
```
source .venv/bin/activate
```
Install the requirements
```
pip3 install -r requirements.txt
```
Run the application
```
python3 manage.py run
```
Run the application: PRODUCTION Mode
```
gunicorn manage:app --worker-class gevent --bind 127.0.0.1:5000 --log-level info
```
### Part Three: Terminal commands
Start Celery Background task on a new terminal session
```
celery -A app.tasks.celery worker -l INFO -B

```

Start Flower Tool to monitor Celery Task on a new terminal session
```
flower -A app.tasks.celery --port=5555 -E

```
## Calling API using CURL
### Register
```
curl -X POST -H "Content-Type: application/json" -d '{"email": "test@example.com","username":"username", "password": "password"}' http://127.0.0.1:5550/v1/register
```
