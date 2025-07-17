from flask import Flask, render_template, request, jsonify, send_file
import os
import json
import markdown
from datetime import datetime
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///squish_portal.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    progress = db.Column(db.Text, default='{}')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class CodeExample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    code = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class StudyMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    order_index = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api-reference')
def api_reference():
    return render_template('api_reference.html')

@app.route('/code-examples')
def code_examples():
    examples = CodeExample.query.all()
    return render_template('code_examples.html', examples=examples)

@app.route('/code-examples/<int:example_id>')
def code_example_detail(example_id):
    example = CodeExample.query.get_or_404(example_id)
    return render_template('code_example_detail.html', example=example)

@app.route('/study-guide')
def study_guide():
    materials = StudyMaterial.query.filter_by(category='guide').order_by(StudyMaterial.order_index).all()
    return render_template('study_guide.html', materials=materials)

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')

@app.route('/real-examples')
def real_examples():
    examples = CodeExample.query.filter_by(category='real-world').all()
    return render_template('real_examples.html', examples=examples)

@app.route('/api/search')
def search_api():
    query = request.args.get('q', '')
    results = []
    
    # Search in code examples
    examples = CodeExample.query.filter(
        CodeExample.title.contains(query) | 
        CodeExample.description.contains(query)
    ).all()
    
    for example in examples:
        results.append({
            'type': 'code_example',
            'title': example.title,
            'description': example.description,
            'url': f'/code-examples/{example.id}'
        })
    
    return jsonify(results)

@app.route('/api/progress', methods=['POST'])
def update_progress():
    # This would handle user progress tracking
    return jsonify({'success': True})

def init_db():
    """Initialize the database with sample data"""
    with app.app_context():
        db.create_all()
        
        # Add sample code examples
        if not CodeExample.query.first():
            examples = [
                {
                    'title': 'Basic Object Interaction',
                    'description': 'Learn how to interact with basic UI objects in Squish',
                    'code': '''import squish
import test

def test_basic_button_click():
    # Start the application
    startApplication("myapp")
    
    # Find and click a button
    button = findObject(":Push Button_QPushButton")
    clickButton(button)
    
    # Verify the result
    test.verify(findObject(":Result_QLabel").text == "Button clicked!")
    
    # Close the application
    closeApplication()''',
                    'category': 'basic',
                    'difficulty': 'beginner'
                },
                {
                    'title': 'Text Input and Validation',
                    'description': 'How to input text and validate form fields',
                    'code': '''import squish
import test

def test_text_input():
    startApplication("myapp")
    
    # Find text input field
    text_field = findObject(":Name_QLineEdit")
    
    # Clear existing text and type new text
    text_field.clear()
    type(text_field, "John Doe")
    
    # Verify the text was entered correctly
    test.compare(text_field.text, "John Doe")
    
    # Submit the form
    submit_button = findObject(":Submit_QPushButton")
    clickButton(submit_button)
    
    closeApplication()''',
                    'category': 'basic',
                    'difficulty': 'beginner'
                },
                {
                    'title': 'Table Data Verification',
                    'description': 'Advanced table testing with data validation',
                    'code': '''import squish
import test

def test_table_data():
    startApplication("myapp")
    
    # Get reference to the table
    table = findObject(":Data_QTableWidget")
    
    # Get table dimensions
    row_count = table.rowCount
    column_count = table.columnCount
    
    # Verify specific cell content
    cell_content = table.item(0, 1).text()
    test.verify(cell_content == "Expected Value")
    
    # Iterate through table rows
    for row in range(row_count):
        for col in range(column_count):
            cell = table.item(row, col)
            if cell:
                test.log(f"Row {row}, Col {col}: {cell.text()}")
    
    # Select a row
    table.selectRow(1)
    
    # Verify selection
    selected_items = table.selectedItems()
    test.verify(len(selected_items) > 0)
    
    closeApplication()''',
                    'category': 'advanced',
                    'difficulty': 'intermediate'
                },
                {
                    'title': 'Real-World Login Test',
                    'description': 'Complete login functionality test with error handling',
                    'code': '''import squish
import test
import time

def test_user_login():
    """Test user login functionality with various scenarios"""
    startApplication("myapp")
    
    # Test successful login
    test_successful_login()
    
    # Test failed login
    test_failed_login()
    
    closeApplication()

def test_successful_login():
    """Test successful login scenario"""
    try:
        # Navigate to login screen
        login_button = findObject(":Login_QPushButton")
        clickButton(login_button)
        
        # Enter valid credentials
        username_field = findObject(":Username_QLineEdit")
        password_field = findObject(":Password_QLineEdit")
        
        type(username_field, "admin")
        type(password_field, "password123")
        
        # Submit login
        submit_button = findObject(":Submit_QPushButton")
        clickButton(submit_button)
        
        # Wait for navigation
        time.sleep(2)
        
        # Verify successful login
        welcome_label = findObject(":Welcome_QLabel")
        test.verify(welcome_label.visible)
        test.compare(welcome_label.text, "Welcome, admin!")
        
        # Logout
        logout_button = findObject(":Logout_QPushButton")
        clickButton(logout_button)
        
    except Exception as e:
        test.fail(f"Login test failed: {str(e)}")

def test_failed_login():
    """Test failed login scenario"""
    try:
        # Navigate to login screen
        login_button = findObject(":Login_QPushButton")
        clickButton(login_button)
        
        # Enter invalid credentials
        username_field = findObject(":Username_QLineEdit")
        password_field = findObject(":Password_QLineEdit")
        
        username_field.clear()
        password_field.clear()
        
        type(username_field, "invalid_user")
        type(password_field, "wrong_password")
        
        # Submit login
        submit_button = findObject(":Submit_QPushButton")
        clickButton(submit_button)
        
        # Wait for error message
        time.sleep(1)
        
        # Verify error message appears
        error_label = findObject(":Error_QLabel")
        test.verify(error_label.visible)
        test.verify("Invalid credentials" in error_label.text)
        
    except Exception as e:
        test.fail(f"Failed login test failed: {str(e)}")''',
                    'category': 'real-world',
                    'difficulty': 'advanced'
                }
            ]
            
            for example_data in examples:
                example = CodeExample(**example_data)
                db.session.add(example)
            
            db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Only populate with sample data if tables are empty
        if not CodeExample.query.first():
            init_db()
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
