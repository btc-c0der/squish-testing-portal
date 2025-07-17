#!/bin/bash

# Squish Testing Portal Launcher
echo "Starting Squish Testing Portal..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running setup first..."
    ./setup.sh
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if database exists, create if not
if [ ! -f "squish_portal.db" ]; then
    echo "Initializing database..."
    python3 -c "from app import app, db; 
    with app.app_context(): 
        db.create_all(); 
        print('Database initialized successfully')"
fi

# Start the application
echo "Starting Flask application..."
echo "Open your browser to: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
python3 app.py
