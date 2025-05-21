# Installation Guide

Follow these steps to install AI-Guard on your system.

## Prerequisites

Before installing AI-Guard, ensure you have the following:

- Python 3.8+
- Git
- Webcam (for enrollment functionality)
- 4GB+ RAM
- GPU (recommended but not required)

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ai-guard.git
cd ai-guard
```

## Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes all necessary packages for AI-Guard:

```
numpy>=1.20.0
opencv-python>=4.5.1
torch>=1.8.0
torchvision>=0.9.0
mtcnn>=0.1.0
scikit-learn>=0.24.1
matplotlib>=3.3.4
jupyter>=1.0.0
pillow>=8.1.0
kagglehub>=0.2.0
```

## Step 4: Download the Pre-trained Models

```python
# Run this in Python or in a Jupyter notebook
import os
import requests

# Create models directory
os.makedirs("models", exist_ok=True)

# Download face detection model (MTCNN)
# This will be done automatically through the mtcnn package

# Download face recognition model (FaceNet)
# In a proper implementation, you would download the model weights
# For now, we'll use a placeholder
print("Model directory created. Models will be downloaded when needed.")
```

## Step 5: Download the Dataset

```python
import kagglehub
# Download latest version of dataset
path = kagglehub.dataset_download("wiameelhafid/aiguard-split-data")
print("Path to dataset files:", path)
```

## Step 6: Configure the System

Create a `.env` file in the project root with the following settings:

```
# AI-Guard Configuration

# Recognition settings
FACE_RECOGNITION_THRESHOLD=0.7
CAMERA_SOURCE=0
ENROLLMENT_QUALITY_CHECK=True

# Alert settings
ALERT_NOTIFICATION=True
EMAIL_NOTIFICATION=False
```

## Step 7: Test the Installation

Verify that your installation is working correctly:

```bash
python -c "import torch; import mtcnn; import cv2; print('Installation successful!')"
```

If you don't see any errors, the installation was successful.

## Step 8: Run the Application

For now, the main interface is through Jupyter notebooks:

```bash
jupyter notebook notebooks/NNNNNNNNN1111.ipynb
```

Follow the instructions in the notebook to register faces and test the recognition.

## Troubleshooting

### Common Issues

1. **GPU Not Detected**

   If you have an NVIDIA GPU but PyTorch isn't using it:

   ```bash
   pip uninstall torch
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

2. **OpenCV Camera Issues**

   If the camera isn't working:

   ```bash
   # Try a different camera index
   python -c "import cv2; cap = cv2.VideoCapture(1); print('Camera works!' if cap.isOpened() else 'Camera failed')"
   ```

3. **Missing Dependencies**

   If you encounter missing dependencies:

   ```bash
   pip install -r requirements.txt --upgrade
   ```

### Getting Help

If you encounter issues not covered here:

1. Check the [Troubleshooting Guide](../user-guide/troubleshooting.md)
2. Open an issue on the GitHub repository
3. Contact the project maintainers

## Next Steps

- [Configuration Guide](configuration.md) - Customize AI-Guard for your needs
- [Quick Start Guide](quick-start.md) - Learn how to use the system
- [Face Enrollment Guide](../user-guide/enrollment.md) - Register users in the system