# Getting Started with AI-Guard

This section will help you set up and start using the AI-Guard facial recognition security system.

## Overview

AI-Guard is a comprehensive facial recognition security system with the following components:

1. **Face Detection and Recognition Models**: Deep learning models for detecting and identifying individuals
2. **User Enrollment System**: Multi-angle face registration workflow
3. **Recognition and Alert Interface**: Real-time monitoring and notification system
4. **User Management Dashboard**: Administration of authorized personnel

![AI-Guard System Overview](../assets/images/system-overview.png)

## System Requirements

To run AI-Guard, you'll need:

- **Hardware Requirements**:
  - Computer with Python 3.8+
  - Webcam for face enrollment
  - GPU recommended for optimal performance (NVIDIA preferred)
  - 4GB+ RAM
  
- **Software Requirements**:
  - Python 3.8+
  - Jupyter Notebook
  - PyTorch
  - OpenCV
  - NumPy
  - Modern web browser

## Installation Options

There are several ways to install and use AI-Guard:

1. [Full Installation](installation.md) - Complete setup for production use
2. [Quick Start](quick-start.md) - Get started quickly with minimal setup
3. [Development Setup](../development/setup.md) - For contributors and developers

## Components Guide

AI-Guard consists of several integrated components:

- **Face Detection**: Uses MTCNN and Faster R-CNN to locate faces in images
- **Face Recognition**: Employs FaceNet/ArcFace to generate face embeddings and verify identities
- **Enrollment System**: Captures multiple face angles to create robust face signatures
- **Alert System**: Notifies security personnel of unauthorized access attempts
- **Management Interface**: Provides administrative controls for system configuration

## Next Steps

- [Installation Guide](installation.md) - Full setup instructions
- [Quick Start Guide](quick-start.md) - Get up and running quickly
- [Configuration Guide](configuration.md) - Customize AI-Guard for your environment
- [User Guide](../user-guide/index.md) - Learn how to use the system