#!/bin/bash

pip install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Setup complete. Runing the app..."
unvicorn app:app --reload