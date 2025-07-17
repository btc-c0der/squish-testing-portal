#!/bin/bash

# Squish Testing Portal Setup Script
echo "Setting up Squish Testing Portal..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Create database
echo "Initializing database..."
python3 -c "from app import app, db; 
with app.app_context(): 
    db.create_all(); 
    print('Database initialized successfully')"

# Create static directories
echo "Creating static directories..."
mkdir -p static/css
mkdir -p static/js
mkdir -p static/images
mkdir -p screenshots

echo "Setup complete!"
echo "To run the application:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Run the application: python app.py"
echo "3. Open your browser to: http://localhost:5000"
