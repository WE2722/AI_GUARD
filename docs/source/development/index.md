# Development Guide

This guide provides information for developers who want to contribute to the AI-Guard project or set up a development environment.

## Development Overview

AI-Guard is a Python-based facial recognition security system that uses deep learning models for face detection and recognition. The current implementation is a proof-of-concept with the core functionality implemented as Jupyter notebooks, while the production version will feature a more comprehensive architecture.

## Development Environment Setup

### Prerequisites

To set up a development environment for AI-Guard, you'll need:

- Python 3.8+
- Git
- A webcam (for testing enrollment and recognition features)
- GPU with CUDA support (recommended but not required)

### Setting Up Your Environment

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/ai-guard.git
   cd ai-guard
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Development Dependencies**

   ```bash
   pip install -r requirements-dev.txt
   ```

5. **Download the Dataset**

   ```python
   import kagglehub
   # Download the enhanced LFW dataset
   path = kagglehub.dataset_download("wiameelhafid/aiguard-split-data")
   print("Path to dataset files:", path)
   ```

6. **Configure Environment Variables**

   Create a `.env` file in the project root:

   ```
   # Development settings
   DEBUG=True
   LOG_LEVEL=DEBUG
   
   # Recognition settings
   FACE_RECOGNITION_THRESHOLD=0.7
   CAMERA_SOURCE=0
   
   # Testing settings
   TEST_DATA_DIR=tests/data
   ```

## Project Structure

The development version of AI-Guard follows this structure:

```
ai-guard/
├── notebooks/             # Jupyter notebooks for demos and experiments
│   ├── NNNNNNNNN1111.ipynb    # Face enrollment notebook
│   └── recognition_demo.ipynb # Recognition demo notebook
├── ai_guard/              # Core Python package (planned)
│   ├── __init__.py
│   ├── detection/         # Face detection algorithms
│   ├── recognition/       # Face recognition models
│   ├── enrollment/        # Enrollment workflow
│   ├── alerts/            # Alert system
│   └── utils/             # Utility functions
├── data/                  # Data directory
│   ├── embeddings/        # Enrolled face data
│   └── models/            # Pre-trained model weights
├── tests/                 # Unit and integration tests
├── docs/                  # Documentation
├── scripts/               # Utility scripts
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
└── README.md              # Project overview
```

## Development Workflow

### Running the Notebooks

The current implementation is based on Jupyter notebooks:

```bash
jupyter notebook notebooks/
```

The core notebooks include:

- `NNNNNNNNN1111.ipynb`: Face enrollment workflow
- `recognition_demo.ipynb`: Face recognition demonstration

### Running Tests

We use pytest for automated testing:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_detection.py

# Run with coverage report
pytest --cov=ai_guard
```

### Code Style

We follow the PEP 8 style guide for Python code. We use the following tools to enforce code quality:

- **Black**: For code formatting
- **isort**: For import sorting
- **flake8**: For style guide enforcement
- **mypy**: For static type checking

Run the following commands before committing changes:

```bash
# Format code
black ai_guard tests

# Sort imports
isort ai_guard tests

# Check for style issues
flake8 ai_guard tests

# Check types
mypy ai_guard
```

## Development Roadmap

The future development of AI-Guard is focused on transforming the current proof-of-concept into a production-ready system:

### Phase 1: Code Restructuring

- Refactor notebook code into a proper Python package structure
- Implement proper error handling and logging
- Add comprehensive unit tests

### Phase 2: Core Feature Enhancement

- Improve face detection and recognition algorithms
- Enhance the multi-angle enrollment process
- Develop a proper database backend for embeddings and user data

### Phase 3: Interface Development

- Create a web-based user interface
- Implement a RESTful API
- Develop real-time video processing capabilities

### Phase 4: Production Readiness

- Add authentication and authorization
- Implement security best practices
- Optimize performance for production environments
- Create deployment documentation

## Contributing

We welcome contributions to the AI-Guard project! Here's how you can contribute:

### Reporting Issues

- Use the GitHub issue tracker to report bugs or suggest features
- Provide a clear description of the issue
- Include steps to reproduce bugs
- Suggest a solution if possible

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure they pass
5. Update documentation as needed
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to your branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Coding Standards

- Follow the existing code style and naming conventions
- Write meaningful commit messages
- Add comments for complex logic
- Update documentation for any user-facing changes
- Write tests for new functionality

## Development Resources

### Machine Learning Resources

- [FaceNet Paper](https://arxiv.org/abs/1503.03832)
- [ArcFace Paper](https://arxiv.org/abs/1801.07698)
- [MTCNN Paper](https://arxiv.org/abs/1604.02878)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [OpenCV Documentation](https://docs.opencv.org/master/)

### Python Tools

- [Jupyter Notebooks](https://jupyter.org/documentation)
- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [Black Documentation](https://black.readthedocs.io/en/stable/)
- [mypy Documentation](https://mypy.readthedocs.io/en/stable/)

### Project-Specific Resources

- [LFW Dataset](http://vis-www.cs.umass.edu/lfw/)
- [FDDB Dataset](http://vis-www.cs.umass.edu/fddb/)

## Next Steps

- [Setup Guide](setup.md) - Set up your development environment
- [Contributing Guide](contributing.md) - Learn how to contribute to the project
- [Roadmap](roadmap.md) - View the detailed development roadmap