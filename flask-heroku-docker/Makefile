update:
	@pip install --upgrade pip

install:
	@pip install -r requirements.txt

install-dev:
	@pip install -r requirements-dev.txt

run:
	@python main.py

test:
	@python -m pytest

build:
	@docker build -t ${imagename}:latest .

run-docker:
	@docker run -p 5000:5000 ${imagename}:latest

start-db-containers:
	@sudo docker compose -f services/database/database-compose.yml up --build -d

stop-db-containers:
	@sudo docker compose -f services/database/database-compose.yml down -v

create-db:
	@python manage.py create_db

seed-db:
	@python manage.py seed_db

test-local:
	@curl localhost:5000/
	@curl localhost:5000/users
