# Makefile for Python project

# Define the Python version to use (you can adjust this if you have a specific version of Python)
PYTHON = python3

# Define the path to your virtual environment (if you're using one)
VENV_DIR = .venv

# Define the path to the requirements file
REQUIREMENTS_FILE = requirements-dev.txt

PIANO_MAC_ADDR = "F0:71:E9:51:50:1C"

# Define the main target for installing dependencies
.PHONY: install
install: ## Install the development dependencies
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS_FILE)
	$(VENV_DIR)/bin/pip install -r requirements.txt
	sudo apt install bluez alsa-utils qjackctl jackd a2jmidid -y

# Run Black code formatter
.PHONY: black
black: ## Format the code using Black
	$(VENV_DIR)/bin/black .

# Run Flake8 linter
.PHONY: lint
lint: ## Lint the code with Flake8
	$(VENV_DIR)/bin/flake8 .

# Run tests with pytest
.PHONY: test
test: ## Run tests with pytest
	$(VENV_DIR)/bin/pytest

# Run Black and Flake8 together
.PHONY: check
check: lint black ## Run both linters and formatter

# Clean all Python bytecode and other temporary files
.PHONY: clean
clean: ## Clean Python bytecode and other temporary files
	rm -rf __pycache__
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf *.egg-info

# Remove the virtual environment
.PHONY: clean-env
clean-env: ## Remove the virtual environment
	rm -rf $(VENV_DIR)

# Run all checks (formatting, linting, and tests)
.PHONY: all
all: check test ## Run both checks (Black + Flake8) and tests (pytest)

# Run app
.PHONY: run
run: ## Run the app
	$(VENV_DIR)/bin/python main.py
