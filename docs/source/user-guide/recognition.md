# Face Recognition Guide

This guide explains how the AI-Guard face recognition system works and how to use it effectively for security monitoring.

## Recognition Process

The AI-Guard face recognition system follows a multi-step process:

1. **Face Detection**: Identify and locate all faces in the video feed
2. **Face Alignment**: Normalize the detected faces for consistent processing
3. **Feature Extraction**: Generate embeddings that represent the unique facial features
4. **Identity Matching**: Compare these embeddings against the database of enrolled users
5. **Verification**: Determine if the match confidence exceeds the recognition threshold

![Recognition Process Diagram](../assets/images/recognition-process.png)

## System Components

### Detection Models

AI-Guard uses multiple detection models depending on the scenario:

- **MTCNN (Multi-task Cascaded Convolutional Networks)**: Primary detection model offering good balance of speed and accuracy
- **Faster R-CNN**: More accurate but slower detection model, used in high-security scenarios
- **RetinaFace**: Alternative model with good performance in challenging conditions

### Recognition Models

The system supports several recognition models:

- **FaceNet**: Primary recognition model generating 512-dimensional face embeddings
- **ArcFace**: Higher accuracy model with improved performance across demographics
- **ResNet18**: Lighter model for deployments with limited computational resources

## Monitoring Interface

Currently, the recognition interface is accessible through Jupyter notebooks. A dedicated web interface is planned for future releases.

### Running Recognition

To start the recognition system:

1. Activate your Python environment:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Launch the recognition notebook:
   ```bash
   jupyter notebook notebooks/recognition_demo.ipynb
   ```

3. Run the initialization cells to:
   - Load face detection and recognition models
   - Connect to the specified camera
   - Load the database of enrolled faces

4. Run the recognition cell to start monitoring:
   - The system will display a live feed with bounding boxes around detected faces
   - Recognized individuals will have green boxes with their names
   - Unknown individuals will have red boxes labeled "Unknown"
   - The confidence score will be displayed for each detection

### Understanding the Display

The recognition display includes several visual elements:

- **Bounding Box**: Rectangular outline around each detected face
- **Name Label**: Displayed above the bounding box for recognized individuals
- **Confidence Score**: Number between 0 and 1 indicating match certainty
- **Status Indicator**: Color-coded box (green for authorized, red for unauthorized)
- **Frame Rate**: FPS counter in the corner showing system performance

![Recognition Display Elements](../assets/images/recognition-display.png)

## Recognition Parameters

### Confidence Threshold

The confidence threshold determines how strict the system is when matching faces:

- **Default threshold**: 0.7 (70%)
- **High security setting**: 0.8 (80%)
- **Low security setting**: 0.6 (60%)

Adjust this in the configuration file based on your security requirements:

```python
# In the recognition notebook
recognition_threshold = 0.7  # Adjust as needed

# Or in the .env configuration file
FACE_RECOGNITION_THRESHOLD=0.7
```

### Multiple Face Handling

The system can handle multiple faces simultaneously in the video feed:

- Each face is processed independently
- Recognition is performed on all detected faces
- Alert thresholds can be configured based on the number of unauthorized individuals

## Recognition Scenarios

### Standard Monitoring

For day-to-day security monitoring:

- Run the `recognition_demo.ipynb` notebook
- Position the camera at entry points
- Monitor the live feed for unauthorized access attempts

### Batch Recognition

For processing recorded video:

- Use the `batch_recognition.ipynb` notebook
- Specify the path to the video file
- Run the analysis on the entire file
- Review the results summary and timeline

### High Security Mode

For increased security in critical areas:

- Enable high security mode in the configuration
- This activates stricter matching thresholds
- Uses the more accurate (but slower) detection models
- Logs all recognition events with higher detail

## Performance Optimization

To improve recognition performance:

### Hardware Recommendations

- **GPU Acceleration**: NVIDIA GPU with CUDA support significantly improves performance
- **Camera Quality**: Higher resolution cameras improve detection accuracy
- **Lighting**: Ensure consistent, adequate lighting in monitored areas

### Software Optimizations

- **Resolution Scaling**: Reduce processing resolution for faster performance
- **Frame Rate Limiting**: Process fewer frames per second to reduce CPU/GPU load
- **Batch Processing**: Enable batch processing if multiple cameras are being monitored

## Troubleshooting

### Common Issues

1. **Low Recognition Accuracy**
   - Check lighting conditions
   - Verify camera positioning and focus
   - Consider re-enrolling users with better quality images
   - Adjust the confidence threshold

2. **Slow Performance**
   - Reduce processing resolution
   - Lower the frame rate
   - Switch to a lighter-weight model
   - Ensure GPU acceleration is enabled if available

3. **False Positives/Negatives**
   - Adjust the confidence threshold
   - Improve lighting conditions
   - Update face embeddings for problematic users
   - Consider using a more accurate model

## Future Enhancements

The recognition system will be enhanced in future releases with:

- Web-based monitoring interface
- Multi-camera support
- Real-time analytics dashboard
- Mobile monitoring application
- Integration with access control systems

## Next Steps

- [Alert System](alerts.md) - Learn how to respond to security alerts
- [User Management](management.md) - Manage enrolled users and their access levels
- [System Configuration](../getting-started/configuration.md) - Adjust recognition parameters