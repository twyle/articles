update:
	@pip install --upgrade pip

install:
	@pip install -r requirements.txt

install-dev:
	@pip install -r requirements-dev.txt

test:
	@python -m pytest

pre-commit:
	@pre-commit install

initial-tag:
	@git tag -a -m "Initial tag." v0.0.1

init-cz:
	@cz init

bump-tag:
	@cz bump --check-consistency --changelog

start-db-containers:
	@sudo docker-compose -f services/database/database-compose.yml up --build -d

stop-db-containers:
	@sudo docker-compose -f services/database/database-compose.yml down -v

create-db:
	@python manage.py create_db

seed-db:
	@python manage.py seed_db

test-local:
	@curl localhost:5000/
	@curl localhost:5000/users

build:
	@docker build -t repo-template-ebs-containerized .

run:
	@docker run -p5000:5000 --env-file=./.env repo-template-ebs-containerized:latest
