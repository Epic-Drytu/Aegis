#!/usr/bin/env bash
set -e

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Setup completed. Copy .env.example to .env and configure the values."
