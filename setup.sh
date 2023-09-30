#!/bin/bash

echo "Step 1: Creating a Python virtual environment..."
python3 -m venv venv

echo "Step 2: Activating the virtual environment..."
source venv/bin/activate

echo "Step 3: Installing requirements..."
pip install -r requirements.txt

echo "All steps completed successfully."

exit 0