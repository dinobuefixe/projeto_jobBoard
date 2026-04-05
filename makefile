# Makefile for Django Job Board Project
# Python 3.14.3 | Django 6.0.3

.PHONY: help setup install migrate makemigrations shell server prod-server test clean static superuser

# Variables
MANAGE = python manage.py
PORT = 8000
APP_NAME = projeto_jobBoard

# Default target
help:
	@echo " Available commands:"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make setup         - Create virtual environment and install dependencies"
	@echo "  make install       - Install dependencies from pyproject.toml"
	@echo ""
	@echo "Database:"
	@echo "  make migrate       - Run all database migrations"
	@echo "  make makemigrations - Create new migrations for all apps"
	@echo "  make reset-db      - Reset database (deletes db.sqlite3 and remigrates)"
	@echo ""
	@echo "Development:"
	@echo "  make server        - Run development server on port $(PORT)"
	@echo "  make prod-server   - Run production server with uvicorn"
	@echo "  make shell         - Open Django interactive shell"
	@echo "  make superuser     - Create admin superuser"
	@echo ""
	@echo "Testing & Quality:"
	@echo "  make test          - Run all tests"
	@echo "  make test-app APP  - Run tests for specific app (e.g., make test-app accounts)"
	@echo ""
	@echo "Maintenance:"
	@echo "  make static        - Collect static files"
	@echo "  make clean         - Remove __pycache__ and migration pycache"
	@echo "  make clean-all     - Remove __pycache__, db.sqlite3, and pycache folders"

# Setup virtual environment with uv
setup:
	@echo " Setting up virtual environment..."
	uv venv
	@echo " Installing dependencies..."
	uv pip install -e .
	@echo " Setup complete! Run 'make migrate' to setup database"

# Install/update dependencies
install:
	@echo " Installing dependencies from uv.lock..."
	uv pip sync uv.lock

# Database migrations
migrate:
	@echo " Running migrations..."
	$(MANAGE) migrate

# Create new migrations
makemigrations:
	@echo " Creating new migrations..."
	$(MANAGE) makemigrations

# Reset database (warning: deletes all data)
reset-db:
	@echo "  WARNING: This will delete all data in db.sqlite3"
	@read -p "Are you sure? (y/N): " confirm; \
	if [ "$$confirm" = "y" ]; then \
		rm -f db.sqlite3; \
		$(MANAGE) migrate; \
		echo " Database reset and migrations applied"; \
	else \
		echo " Cancelled"; \
	fi

# Run development server
server:
	@echo " Starting development server on http://localhost:$(PORT)"
	$(MANAGE) runserver $(PORT)

# Run production server with uvicorn
prod-server:
	@echo " Starting production server on http://localhost:$(PORT)"
	uvicorn $(APP_NAME).asgi:application --host 0.0.0.0 --port $(PORT) --reload

# Django shell
shell:
	@echo " Opening Django shell..."
	$(MANAGE) shell

# Create superuser
superuser:
	@echo " Creating superuser..."
	$(MANAGE) createsuperuser

# Run all tests
test:
	@echo " Running all tests..."
	$(MANAGE) test

# Run tests for specific app (usage: make test-app APP=accounts)
test-app:
	@if [ -z "$(APP)" ]; then \
		echo " Please specify an app: make test-app APP=accounts"; \
		exit 1; \
	fi
	@echo " Running tests for $(APP)..."
	$(MANAGE) test $(APP)

# Collect static files
static:
	@echo " Collecting static files..."
	$(MANAGE) collectstatic --noinput

# Clean pycache files only
clean:
	@echo " Cleaning __pycache__ directories..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo " Cleanup complete"

# Clean everything including database ( destructive)
clean-all: clean
	@echo "  WARNING: This will delete the database file"
	@read -p "Delete db.sqlite3? (y/N): " confirm; \
	if [ "$$confirm" = "y" ]; then \
		rm -f db.sqlite3; \
		echo " Database deleted"; \
	else \
		echo " Database preserved"; \
	fi