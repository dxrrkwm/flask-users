PYTHON = python
POETRY = poetry
PROJECT_NAME = flask-users
CONTAINER_NAME = ${PROJECT_NAME}_container
DOCKER_COMPOSE = docker-compose

.PHONY: help
help:
	@echo "Usage: make [target] [path=<path>]"
	@echo ""
	@echo "Targets:"
	@echo "  deps         Install dependencies with Poetry"
	@echo "  up           Start the application"
	@echo "  down         Stop the application"
	@echo "  init-db-docker      Initialize database in docker"
	@echo "  test         Run tests"
	@echo "  lint      		Run isort and Ruff on a specific path"
	@echo "  clean        Remove cache files"
	@echo "  build        Build the application"
	@echo "  up-build     Start the application with build"
	@echo "  run          Run the application locally"

.PHONY: deps
deps:
	${POETRY} install

.PHONY: build
build:
	${DOCKER_COMPOSE} build

.PHONY: up-build
up-build:
	${DOCKER_COMPOSE} up --build

.PHONY: up
up:
	${DOCKER_COMPOSE} up

.PHONY: down
down:
	${DOCKER_COMPOSE} down

.PHONY: init-db-docker
init-db-docker:
	${DOCKER_COMPOSE} exec api flask init-db

.PHONY: test
test:
	${POETRY} run pytest

.PHONY: test-docker
test-docker:
	${DOCKER_COMPOSE} exec api pytest

.PHONY: lint
lint:
	@echo "Running isort and Ruff on: $(path)"
	${POETRY} run isort $(path)
	${POETRY} run ruff check --fix $(path)

.PHONY: clean
clean:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name ".pytest_cache" -exec rm -rf {} +
	find . -name ".coverage" -delete
	find . -name ".ruff_cache" -exec rm -rf {} +

.PHONY: run
run:
	${POETRY} run flask run
