# Development Environment Setup

This guide provides detailed instructions for setting up a development environment for the AI-Guard project.

## System Requirements

### Minimum Requirements

- **Operating System**: Windows 10, macOS 10.14+, or Linux (Ubuntu 18.04+ recommended)
- **Processor**: Intel Core i5 or equivalent
- **Memory**: 8GB RAM
- **Storage**: 10GB free disk space
- **Python**: 3.8 or newer
- **Camera**: Basic webcam for testing

### Recommended Specifications

- **Processor**: Intel Core i7/i9 or AMD Ryzen 7/9
- **Memory**: 16GB+ RAM
- **GPU**: NVIDIA GPU with CUDA support (at least 4GB VRAM)
- **Storage**: SSD with 20GB+ free space
- **Camera**: HD webcam (1080p)

## Step 1: Install Python

### Windows

1. Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. Check "Add Python to PATH" during installation
4. Verify installation with `python --version` in a command prompt

### macOS

1. Install Homebrew if not already installed:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install Python:
   ```bash
   brew install python
   ```

3. Verify installation:
   ```bash
   python3 --version
   ```

### Linux (Ubuntu)

1. Update package lists:
   ```bash
   sudo apt update
   ```

2. Install Python and development tools:
   ```bash
   sudo apt install python3 python3-pip python3-dev python3-venv
   ```

3. Verify installation:
   ```bash
   python3 --version
   ```

## Step 2: Install Git

### Windows

1. Download Git from [git-scm.com](https://git-scm.com/downloads)
2. Run the installer with default options
3. Verify installation with `git --version` in a command prompt

### macOS

```bash
brew install git
git --version
```

### Linux (Ubuntu)

```bash
sudo apt install git
git --version
```

## Step 3: Clone the Repository

```bash
git clone https://github.com/your-username/ai-guard.git
cd ai-guard
```

## Step 4: Set Up Virtual Environment

### Create a Virtual Environment

```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### Activate the Virtual Environment

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

You should see the environment name in your command prompt.

## Step 5: Install Dependencies

### Core Dependencies

```bash
pip install -r requirements.txt
```

### Development Dependencies

```bash
pip install -r requirements-dev.txt
```

### Jupyter Lab/Notebook

```bash
pip install jupyterlab
```

## Step 6: CUDA Setup (GPU Support - Optional)

For GPU-accelerated model training and inference:

### Windows

1. Download and install the [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
2. Download and install [cuDNN](https://developer.nvidia.com/cudnn) (requires NVIDIA Developer account)
3. Install PyTorch with CUDA support:
   ```bash
   pip uninstall torch
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

### Linux

1. Follow the [CUDA installation guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
2. Install cuDNN following [NVIDIA's instructions](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)
3. Install PyTorch with CUDA support:
   ```bash
   pip uninstall torch
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

### Verify GPU Support

```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
print(f"GPU count: {torch.cuda.device_count()}")
print(f"GPU name: {torch.cuda.get_device_name(0)}")
```

## Step 7: Download Dataset and Models

```python
import kagglehub
import os

# Create data directories
os.makedirs("data/embeddings", exist_ok=True)
os.makedirs("data/models", exist_ok=True)

# Download the enhanced LFW dataset
path = kagglehub.dataset_download("wiameelhafid/aiguard-split-data")
print("Path to dataset files:", path)

# Download pre-trained models will be handled automatically when first used
```

## Step 8: Configure Environment Variables

Create a `.env` file in the project root:

```
# Development settings
DEBUG=True
LOG_LEVEL=DEBUG

# Recognition settings
FACE_RECOGNITION_THRESHOLD=0.7
CAMERA_SOURCE=0
ENROLLMENT_QUALITY_CHECK=True

# Model settings
FACE_DETECTION_MODEL=mtcnn
FACE_RECOGNITION_MODEL=facenet
USE_GPU=True

# Testing settings
TEST_DATA_DIR=tests/data
```

## Step 9: Configure Git Hooks (Optional)

Set up pre-commit hooks for code quality:

```bash
pip install pre-commit
pre-commit install
```

Create a `.pre-commit-config.yaml` file:

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files

-   repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
    -   id: black

-   repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
    -   id: isort

-   repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-docstrings]
```

## Step 10: Run Tests

Verify your setup by running the test suite:

```bash
pytest
```

## Step 11: Start Jupyter Notebook

To work with the enrollment and recognition notebooks:

```bash
jupyter notebook
```

Navigate to `notebooks/` directory and open `NNNNNNNNN1111.ipynb` for the enrollment workflow.

## IDE Setup

### Visual Studio Code

1. Install [VS Code](https://code.visualstudio.com/)
2. Install the following extensions:
   - Python
   - Jupyter
   - GitLens
   - PyLance
   - Python Docstring Generator
   - Python Test Explorer

3. Configure Python interpreter:
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
   - Type "Python: Select Interpreter"
   - Select the virtual environment you created

### PyCharm

1. Install [PyCharm](https://www.jetbrains.com/pycharm/) (Community or Professional)
2. Open the AI-Guard project folder
3. Configure the Python interpreter:
   - Go to Settings/Preferences → Project → Python Interpreter
   - Add the virtual environment you created

## Common Setup Issues

### Missing Dependencies

**Issue**: Import errors when running notebooks or tests.
**Solution**: Ensure all dependencies are installed and the virtual environment is activated.

```bash
pip install -r requirements.txt
pip list  # Verify installations
```

### CUDA/GPU Issues

**Issue**: Cannot use GPU acceleration.
**Solution**: Verify CUDA compatibility with PyTorch version.

```bash
# Check CUDA availability
python -c "import torch; print(torch.cuda.is_available())"

# If false, reinstall with correct CUDA version
pip uninstall torch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Camera Access

**Issue**: Cannot access webcam in notebooks.
**Solution**: Verify camera permissions and connections.

```python
# Test camera
import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print("Camera working:", ret)
if ret:
    cv2.imshow('Test', frame)
    cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
```

### Virtual Environment Not Activating

**Issue**: Virtual environment commands not found.
**Solution**: Check your activation command and path.

```bash
# Windows alternative
venv\Scripts\activate.bat

# macOS/Linux if facing issues
source ./venv/bin/activate
```

## Next Steps

Once your development environment is set up:

1. Explore the [Project Structure](../technical/architecture.md) to understand the codebase
2. Check the [Development Workflow](index.md#development-workflow) section
3. Review the [Contributing Guidelines](contributing.md) before making changes