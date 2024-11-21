.PHONY: all
all: install run

# Install dependencies
.PHONY: install
install:
	python3 -m pip install -r requirements.txt

# Run the application
.PHONY: run
run:
	python3 api.py

