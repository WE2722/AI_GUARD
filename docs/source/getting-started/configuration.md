# Configuration Guide

This guide explains how to configure AI-Guard to customize its behavior according to your security requirements.

## Configuration File

AI-Guard uses a `.env` file for configuration. Create this file in the project root directory with the following parameters:

```bash
# AI-Guard Configuration File (.env)

# Recognition Settings
FACE_RECOGNITION_THRESHOLD=0.7
CAMERA_SOURCE=0
ENROLLMENT_QUALITY_CHECK=True
RECOGNITION_BATCH_SIZE=1

# Alert Settings
ALERT_NOTIFICATION=True
EMAIL_NOTIFICATION=False
EMAIL_SENDER=security@example.com
EMAIL_RECIPIENTS=admin@example.com,guard@example.com

# System Settings
LOG_LEVEL=INFO
DATA_DIRECTORY=data
MODEL_DIRECTORY=models
```

## Recognition Parameters

### Face Recognition Threshold

The `FACE_RECOGNITION_THRESHOLD` (default: 0.7) determines how strict the face matching is:

- **Lower values** (e.g., 0.6): More permissive matching, fewer false negatives but more false positives
- **Higher values** (e.g., 0.8): Stricter matching, more false negatives but fewer false positives

```bash
# For high-security areas
FACE_RECOGNITION_THRESHOLD=0.8

# For less critical areas
FACE_RECOGNITION_THRESHOLD=0.65
```

### Camera Source

The `CAMERA_SOURCE` parameter selects which camera to use:

```bash
# Default webcam (usually built-in camera)
CAMERA_SOURCE=0

# External webcam
CAMERA_SOURCE=1

# Network camera using RTSP
CAMERA_SOURCE=rtsp://admin:password@192.168.1.100:554/stream
```

### Enrollment Quality Check

The `ENROLLMENT_QUALITY_CHECK` parameter (default: True) enables quality validation during face enrollment:

```bash
# Enable quality checks (recommended)
ENROLLMENT_QUALITY_CHECK=True

# Disable quality checks (faster enrollment but may reduce recognition accuracy)
ENROLLMENT_QUALITY_CHECK=False
```

## Alert Configuration

### Alert Notifications

Control whether the system generates alerts for unauthorized access:

```bash
# Enable alerts (recommended)
ALERT_NOTIFICATION=True

# Disable alerts (for testing or development)
ALERT_NOTIFICATION=False
```

### Email Notifications

Configure email alerts for security incidents:

```bash
# Enable email alerts
EMAIL_NOTIFICATION=True
EMAIL_SENDER=security@example.com
EMAIL_RECIPIENTS=admin@example.com,guard@example.com
EMAIL_SERVER=smtp.example.com
EMAIL_PORT=587
EMAIL_USERNAME=security@example.com
EMAIL_PASSWORD=your_secure_password
```

## Advanced Configuration

### Model Selection

AI-Guard supports multiple face detection and recognition models:

```bash
# Face detection model options: "mtcnn" (default), "faster_rcnn", "retinaface"
FACE_DETECTION_MODEL=mtcnn

# Face recognition model options: "facenet" (default), "arcface", "resnet18"
FACE_RECOGNITION_MODEL=facenet
```

### Performance Tuning

Adjust these parameters to balance accuracy and performance:

```bash
# GPU acceleration (True/False)
USE_GPU=True

# Detection batch size (higher values use more memory but may be faster)
DETECTION_BATCH_SIZE=4

# Recognition batch size
RECOGNITION_BATCH_SIZE=8

# Image resolution for processing (lower values increase speed)
IMAGE_WIDTH=640
IMAGE_HEIGHT=480
```

## Directory Structure

Configure the locations where AI-Guard stores its data:

```bash
# Main data directory
DATA_DIRECTORY=data

# Model weights directory
MODEL_DIRECTORY=models

# Directory for enrolled face data
ENROLLMENT_DIRECTORY=data/enrollments

# Log file location
LOG_FILE=logs/ai_guard.log
```

## Example Configurations

### High-Security Configuration

```bash
FACE_RECOGNITION_THRESHOLD=0.85
ENROLLMENT_QUALITY_CHECK=True
ALERT_NOTIFICATION=True
EMAIL_NOTIFICATION=True
FACE_DETECTION_MODEL=retinaface
FACE_RECOGNITION_MODEL=arcface
```

### Testing Configuration

```bash
FACE_RECOGNITION_THRESHOLD=0.6
ENROLLMENT_QUALITY_CHECK=False
ALERT_NOTIFICATION=False
EMAIL_NOTIFICATION=False
USE_GPU=False
```

### Performance-Optimized Configuration

```bash
FACE_RECOGNITION_THRESHOLD=0.7
ENROLLMENT_QUALITY_CHECK=True
FACE_DETECTION_MODEL=mtcnn
FACE_RECOGNITION_MODEL=resnet18
DETECTION_BATCH_SIZE=8
RECOGNITION_BATCH_SIZE=16
IMAGE_WIDTH=320
IMAGE_HEIGHT=240
```

## Applying Configuration Changes

After modifying the `.env` file, restart the AI-Guard application for the changes to take effect:

```bash
# Stop current process (if running)
# Then start again
jupyter notebook notebooks/NNNNNNNNN1111.ipynb
```

## Verifying Configuration

To verify that your configuration changes are applied correctly, check the console output when starting the system. The first few log lines should display the current configuration values.

## Next Steps

- [User Management](../user-guide/management.md) - Configure user access and permissions
- [Alert System Configuration](../user-guide/alerts.md) - Customize the alert system
- [Troubleshooting](../user-guide/troubleshooting.md) - Solve common configuration issues