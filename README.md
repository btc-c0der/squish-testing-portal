# Squish Testing Portal

A comprehensive Flask web application for students learning Qt Squish automated testing. This educational portal provides API references, code examples, study guides, learning roadmaps, and real-world testing scenarios.

## Features

### 🔧 Comprehensive API Reference
- Complete documentation of all Squish APIs
- Detailed function descriptions with parameters and return values
- Python-focused examples and usage patterns
- Interactive navigation with smooth scrolling

### 💻 Python Code Examples
- Basic to advanced Squish testing examples
- Categorized by difficulty level (Beginner, Intermediate, Advanced)
- Real-world testing scenarios
- Interactive code viewing with syntax highlighting
- Copy-to-clipboard functionality

### 📚 Study Guide & Learning Materials
- Structured learning path from basics to advanced topics
- Progress tracking with milestone completion
- Interactive lessons with hands-on exercises
- Best practices and troubleshooting guides

### 🗺️ Learning Roadmap
- 10-week structured learning program
- Phase-based progression with clear objectives
- Milestone tracking and achievement system
- Personalized progress monitoring

### 🏢 Real-World Examples
- Production-ready test scenarios
- E-commerce application testing
- Banking application security testing
- Healthcare compliance testing
- Enterprise-level testing patterns

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git (for cloning the repository)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/btc-c0der/squish-testing-portal.git
   cd squish-testing-portal
   ```

2. **Run the setup script:**
   ```bash
   ./setup.sh
   ```

3. **Or manually install:**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install requirements
   pip install -r requirements.txt
   
   # Initialize database
   python3 app.py
   ```

### Running the Application

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Start the Flask application:**
   ```bash
   python app.py
   ```

3. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Application Structure

```
squish-testing-portal/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── setup.sh              # Setup script
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── api_reference.html # API reference
│   ├── code_examples.html # Code examples listing
│   ├── code_example_detail.html # Individual example
│   ├── study_guide.html  # Study guide
│   ├── roadmap.html      # Learning roadmap
│   └── real_examples.html # Real-world examples
├── static/               # Static files (CSS, JS, images)
├── screenshots/          # Screenshot storage
└── venv/                # Virtual environment (created during setup)
```

## Key Features

### 🎯 Interactive Learning
- **Progress Tracking**: Track your learning progress through the study guide
- **Milestone System**: Complete milestones to advance through the roadmap
- **Achievement Badges**: Earn achievements as you progress
- **Search Functionality**: Quickly find specific topics or examples

### 🔍 Advanced Search
- Real-time search across all content
- Filter examples by category and difficulty
- Sort functionality for better organization
- Intelligent search suggestions

### 📱 Responsive Design
- Mobile-friendly interface
- Bootstrap-based responsive layout
- Touch-friendly navigation
- Optimized for all screen sizes

### 🛡️ Code Quality
- Syntax highlighting for Python code
- Copy-to-clipboard functionality
- Download examples as Python files
- Error handling and validation

## Learning Path

### Phase 1: Foundation (Weeks 1-2)
- Introduction to Squish and GUI testing
- Basic object identification
- Simple interaction scripts
- Environment setup

### Phase 2: Core Skills (Weeks 3-4)
- Advanced object identification
- User interaction simulation
- Verification techniques
- Error handling

### Phase 3: Intermediate (Weeks 5-6)
- Data-driven testing
- Test organization
- Image verification
- Complex scenarios

### Phase 4: Advanced (Weeks 7-8)
- Custom libraries
- Performance testing
- CI/CD integration
- Advanced debugging

### Phase 5: Expert (Weeks 9-10)
- Enterprise frameworks
- Test maintenance
- Performance optimization
- Mentoring others

## API Reference Coverage

The portal covers all major Squish APIs including:

- **Object Identification**: `findObject()`, `waitForObject()`, `findChildren()`
- **User Interactions**: `clickButton()`, `type()`, `mouseClick()`, `mouseDrag()`
- **Verification**: `test.verify()`, `test.compare()`, `test.imagePresent()`
- **Application Control**: `startApplication()`, `closeApplication()`
- **Data Handling**: `testData.dataset()`, CSV integration
- **Utility Functions**: `snooze()`, `test.log()`, screenshot capture

## Real-World Examples

### E-commerce Testing
- Complete purchase flow automation
- Cart management and checkout
- Payment processing validation
- Order confirmation verification

### Banking Application
- Secure login with 2FA
- Money transfer workflows
- Security validation
- Audit trail verification

### Healthcare Systems
- Patient management workflows
- HIPAA compliance testing
- Role-based access control
- Medical data validation

## Contributing

We welcome contributions to improve the learning experience:

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

### Areas for Contribution
- Additional code examples
- New real-world scenarios
- UI/UX improvements
- Documentation enhancements
- Bug fixes and optimizations

## Support

For questions and support:
- Check the study guide for comprehensive learning materials
- Review the API reference for specific function documentation
- Examine real-world examples for practical implementations
- Visit the [official Squish documentation](https://doc.qt.io/squish/)

## License

This project is for educational purposes. Please ensure you have proper Squish licensing for any production use.

## Acknowledgments

- Qt Squish team for the excellent testing framework
- Flask community for the robust web framework
- Bootstrap for responsive design components
- Prism.js for syntax highlighting

## Developer

**Developed by:** 0m3g4_k1ng@proton.me

---

**Start your Squish testing journey today!** 🚀

Visit the portal at `http://localhost:5000` after setup to begin learning.