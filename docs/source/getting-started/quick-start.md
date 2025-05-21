# Quick Start Guide

This guide will help you get up and running with AI-Guard quickly, focusing on the core functionality: face enrollment and recognition.

## Prerequisites

- AI-Guard installed ([see Installation Guide](installation.md))
- Webcam connected
- Python environment activated

## 1. Start the Enrollment Notebook

The face enrollment process is handled through a Jupyter notebook:

```bash
jupyter notebook notebooks/NNNNNNNNN1111.ipynb
```

This will open the notebook in your default web browser.

## 2. Enroll a Face

Follow these steps in the notebook to enroll a face:

1. Run the first cell to import dependencies
2. Run the second cell to initialize the webcam
3. Follow the prompts to capture three angles of the face:
   - Front-facing view
   - Left profile view (approximately 45°)
   - Right profile view (approximately 45°)
4. Enter the name of the person being enrolled when prompted
5. Run the final cell to process and save the face embeddings

![Face Enrollment Process](../assets/images/enrollment-process.png)

## 3. Test Recognition

After enrolling at least one face, you can test the recognition:

1. Navigate to the "Test Recognition" section in the notebook
2. Run the cell to initialize the webcam and recognition model
3. Position the enrolled person in front of the camera
4. The system will display a bounding box around the face with the person's name if recognized

```python
# Example recognition code
import cv2
from models import load_recognition_model, recognize_face

# Load model and enrolled faces
model = load_recognition_model()
known_faces = load_known_faces()

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Detect and recognize faces
    results = recognize_face(frame, model, known_faces)
    
    # Display results
    for name, bbox, score in results:
        x, y, w, h = bbox
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, f"{name} ({score:.2f})", 
                   (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    cv2.imshow('AI-Guard Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## 4. Understanding Results

The recognition results display:

- **Green rectangle**: Recognized person (authorized)
- **Red rectangle**: Unknown person (unauthorized)
- **Name and confidence score**: Identification and match certainty

A confidence score above 0.7 (default threshold) indicates a reliable match.

## 5. Adding Multiple Users

To enroll additional users, return to the enrollment section and repeat the process for each person.

## 6. Next Steps

After completing this quick start guide, you can:

- [Configure the system](configuration.md) to adjust threshold values and other settings
- Explore the [User Guide](../user-guide/index.md) for more detailed instructions
- Check out the [Technical Documentation](../technical/index.md) to understand how AI-Guard works
- Set up the [Alert System](../user-guide/alerts.md) for security notifications

## Quick Reference Commands

```bash
# Activate environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Start the enrollment notebook
jupyter notebook notebooks/NNNNNNNNN1111.ipynb

# Run example recognition script (if available)
python scripts/recognition_demo.py
```

## Video Tutorial

For a visual walkthrough of the enrollment and recognition process, watch our tutorial video:

[AI-Guard Quick Start Video](https://www.youtube.com/watch?v=example)

If you encounter any issues, refer to the [Troubleshooting Guide](../user-guide/troubleshooting.md) or open an issue on our GitHub repository.