#!/bin/bash
# Setup script for SmallChat development environment
set -e

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

echo "Environment setup complete."
