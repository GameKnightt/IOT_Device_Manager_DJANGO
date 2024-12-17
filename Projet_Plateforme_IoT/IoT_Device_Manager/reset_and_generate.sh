#!/bin/bash

# Exit on any error
set -e

# Check if tqdm is installed
if ! python3 -c "import tqdm" &> /dev/null; then
    echo "tqdm is not installed. Installing tqdm..."
    pip install tqdm
else
    echo "tqdm is already installed."
fi

echo "Removing the database..."
if [ -f db.sqlite3 ]; then
    rm db.sqlite3
    echo "Database removed."
else
    echo "Database file does not exist. Nothing to remove."
fi

echo "Deleting compiled migration files..."
find . -path "*/migrations/*.pyc" -delete

echo "Deleting migration Python files except for __init__.py..."
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

echo "Making new migrations..."
python3 manage.py makemigrations

echo "Applying migrations..."
python3 manage.py migrate

echo "Generating data..."
python3 manage.py shell < Data_generator.py

echo "All done!"
