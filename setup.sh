#!/bin/bash

if ! command -v python &> /dev/null; then
    echo "Python is not installed. Please install Python 3 or greater before continuing."
    exit 1
fi

echo "Creating virtual environment..."
python -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing project dependencies..."
pip install -r requirements.txt

echo "Setup completed successfully."