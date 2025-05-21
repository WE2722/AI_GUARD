# System Architecture

This document provides a detailed overview of the AI-Guard system architecture, including component interactions, data flow, and design considerations.

## Architecture Overview

AI-Guard employs a modular architecture designed for flexibility, maintainability, and scalability. The current proof-of-concept implementation features a simpler architecture, while the planned production version will adopt a more distributed approach.

### Current Architecture

The current proof-of-concept implementation uses a monolithic architecture with the following components:

```
┌─────────────────────────────────────────────────────────┐
│                    Jupyter Notebooks                     │
├───────────────────┬─────────────────┬───────────────────┤
│  Enrollment UI    │  Recognition UI │  Management UI    │
└─────────┬─────────┴────────┬────────┴─────────┬─────────┘
          │                  │                  │
          ▼                  ▼                  ▼
┌─────────────────────────────────────────────────────────┐
│                      AI-Guard Core                       │
├───────────────┬─────────────────┬───────────────────────┤
│ Face Detection│ Face Recognition│ Data Management       │
└───────┬───────┴────────┬────────┴───────────┬───────────┘
        │                │                    │
        ▼                ▼                    ▼
┌───────────────┬─────────────────┬──────────────────────┐
│  Camera Feed  │ Face Embeddings │ User & System Data   │
└───────────────┴─────────────────┴──────────────────────┘
```

### Planned Production Architecture

The target architecture for the production version adopts a microservices approach:

```
┌───────────────────────────────────────────────────────┐
│                   Client Applications                  │
├───────────┬───────────────┬────────────┬──────────────┤
│ Admin UI  │ Enrollment UI │ Guard UI   │ Mobile App   │
└─────┬─────┴───────┬───────┴─────┬──────┴──────┬───────┘
      │             │             │             │
      └─────────────┼─────────────┼─────────────┘
                    │             │
                    ▼             ▼
┌────────────────────────────────────────────────────────┐
│                      API Gateway                        │
└──────────────────────────┬─────────────────────────────┘
                           │
     ┌─────────────────────┼─────────────────────┐
     │                     │                     │
     ▼                     ▼                     ▼
┌──────────────┐    ┌─────────────┐      ┌─────────────┐
│ Auth Service │    │ Core Service│      │ Alert Service│
└──────┬───────┘    └──────┬──────┘      └──────┬──────┘
       │                   │                    │
       │                   ▼                    │
       │            ┌─────────────┐             │
       └───────────▶│   Database  │◀────────────┘
                    └──────┬──────┘
                           │
                           ▼
                   ┌───────────────┐
                   │ ML Microservice│
                   └───────────────┘
```

## Core Components

### Face Detection Module

Responsible for locating faces within images or video frames:

- **Input**: Raw image or video frame
- **Process**: Apply face detection algorithm (MTCNN or Faster R-CNN)
- **Output**: Bounding box coordinates for each detected face

```python
# Component interface
class FaceDetector:
    def __init__(self, model_type="mtcnn", device="cpu"):
        """Initialize the face detector.
        
        Args:
            model_type: Type of detection model ("mtcnn", "faster_rcnn", or "retinaface")
            device: Computation device ("cpu" or "cuda")
        """
        pass
        
    def detect_faces(self, image):
        """Detect faces in an image.
        
        Args:
            image: Input image (numpy array)
            
        Returns:
            List of detected faces with bounding boxes and landmarks
        """
        pass
```

### Face Recognition Module

Identifies individuals by comparing face embeddings:

- **Input**: Cropped face image
- **Process**: Generate face embedding and compare with enrolled faces
- **Output**: Identity match with confidence score

```python
# Component interface
class FaceRecognizer:
    def __init__(self, model_type="facenet", threshold=0.7, device="cpu"):
        """Initialize the face recognizer.
        
        Args:
            model_type: Type of recognition model ("facenet", "arcface", or "resnet18")
            threshold: Confidence threshold for positive identification
            device: Computation device ("cpu" or "cuda")
        """
        pass
        
    def generate_embedding(self, face_image):
        """Generate embedding for a face image.
        
        Args:
            face_image: Cropped face image (numpy array)
            
        Returns:
            Face embedding vector (numpy array)
        """
        pass
        
    def compare_embeddings(self, embedding1, embedding2):
        """Compare two face embeddings.
        
        Args:
            embedding1: First face embedding
            embedding2: Second face embedding
            
        Returns:
            Similarity score between the two embeddings
        """
        pass
        
    def identify_face(self, face_image, enrolled_embeddings):
        """Identify a face against a database of enrolled embeddings.
        
        Args:
            face_image: Cropped face image
            enrolled_embeddings: Dict mapping identities to face embeddings
            
        Returns:
            Tuple of (identity, confidence_score)
        """
        pass
```

### Enrollment Module

Manages the process of registering new individuals:

- **Input**: Multiple face images from different angles
- **Process**: Quality checks, face alignment, and embedding generation
- **Output**: Face embedding and user metadata

```python
# Component interface
class EnrollmentManager:
    def __init__(self, detector, recognizer, quality_check=True):
        """Initialize the enrollment manager.
        
        Args:
            detector: FaceDetector instance
            recognizer: FaceRecognizer instance
            quality_check: Whether to perform quality validation
        """
        pass
        
    def process_enrollment_image(self, image, angle):
        """Process a single enrollment image.
        
        Args:
            image: Face image
            angle: Capture angle ("front", "left", or "right")
            
        Returns:
            Processed face image and quality score
        """
        pass
        
    def generate_enrollment_embedding(self, images):
        """Generate a composite embedding from multiple face images.
        
        Args:
            images: Dict mapping angles to face images
            
        Returns:
            Final face embedding
        """
        pass
        
    def save_enrollment(self, embedding, user_data):
        """Save enrollment data.
        
        Args:
            embedding: Face embedding
            user_data: User metadata
            
        Returns:
            Success status
        """
        pass
```

### Alert Module

Generates and manages security alerts:

- **Input**: Recognition results
- **Process**: Evaluate against security rules
- **Output**: Alert notifications

```python
# Component interface
class AlertManager:
    def __init__(self, config):
        """Initialize the alert manager.
        
        Args:
            config: Alert configuration
        """
        pass
        
    def evaluate_recognition(self, recognition_result):
        """Evaluate recognition result for potential alerts.
        
        Args:
            recognition_result: Result from face recognition
            
        Returns:
            Alert object if triggered, None otherwise
        """
        pass
        
    def send_alert(self, alert):
        """Send an alert through configured channels.
        
        Args:
            alert: Alert object
            
        Returns:
            Delivery status
        """
        pass
        
    def get_active_alerts(self):
        """Get list of currently active alerts.
        
        Returns:
            List of active alerts
        """
        pass
```

## Data Flow

The AI-Guard system processes data through the following sequence:

### Enrollment Flow

1. **Image Capture**: User provides multiple angle face images
2. **Face Detection**: System locates faces in each image
3. **Quality Verification**: Images are checked for quality
4. **Alignment**: Faces are aligned based on landmarks
5. **Embedding Generation**: Face embeddings are created
6. **Data Storage**: Embeddings and metadata are stored

### Recognition Flow

1. **Frame Acquisition**: System acquires video frame
2. **Face Detection**: Faces are located in the frame
3. **Face Alignment**: Detected faces are aligned
4. **Embedding Generation**: System creates embeddings for each face
5. **Identity Matching**: Embeddings are compared with enrolled faces
6. **Decision Making**: Match results are evaluated against thresholds
7. **Alert Generation**: Alerts are triggered for unauthorized individuals

## Database Design

### Current Implementation

The current proof-of-concept uses a simple file-based storage system:

- **Embeddings**: Stored as serialized numpy arrays in individual files
- **User Data**: Stored in JSON files
- **Configuration**: Stored in environment variables and config files
- **Logs**: Written to text log files

### Planned Database Schema

The production system will use a proper database with the following schema:

**Users Table**
```
+----------------+--------------+-------------------------------+
| Column         | Type         | Description                   |
+----------------+--------------+-------------------------------+
| id             | UUID         | Primary key                   |
| username       | VARCHAR      | Username for system users     |
| password_hash  | VARCHAR      | Hashed password               |
| full_name      | VARCHAR      | User's full name              |
| email          | VARCHAR      | User's email address          |
| role           | ENUM         | User role                     |
| status         | ENUM         | Account status                |
| created_at     | TIMESTAMP    | Account creation timestamp    |
| updated_at     | TIMESTAMP    | Last update timestamp         |
+----------------+--------------+-------------------------------+
```

**Enrolled Individuals Table**
```
+----------------+--------------+-------------------------------+
| Column         | Type         | Description                   |
+----------------+--------------+-------------------------------+
| id             | UUID         | Primary key                   |
| full_name      | VARCHAR      | Individual's full name        |
| department     | VARCHAR      | Department or category        |
| access_level   | ENUM         | Access permission level       |
| status         | ENUM         | Active/Inactive status        |
| enrolled_by    | UUID         | Reference to enrolling user   |
| enrollment_date| TIMESTAMP    | Enrollment timestamp          |
| updated_at     | TIMESTAMP    | Last update timestamp         |
+----------------+--------------+-------------------------------+
```

**Face Embeddings Table**
```
+----------------+--------------+-------------------------------+
| Column         | Type         | Description                   |
+----------------+--------------+-------------------------------+
| id             | UUID         | Primary key                   |
| individual_id  | UUID         | Reference to individual       |
| embedding_data | BYTEA        | Face embedding vector         |
| angle          | ENUM         | Capture angle                 |
| model_version  | VARCHAR      | Model used for embedding      |
| quality_score  | FLOAT        | Image quality score           |
| created_at     | TIMESTAMP    | Creation timestamp            |
+----------------+--------------+-------------------------------+
```

**Recognition Events Table**
```
+----------------+--------------+-------------------------------+
| Column         | Type         | Description                   |
+----------------+--------------+-------------------------------+
| id             | UUID         | Primary key                   |
| timestamp      | TIMESTAMP    | Event timestamp               |
| camera_id      | VARCHAR      | Source camera identifier      |
| individual_id  | UUID         | Matched individual (if any)   |
| confidence     | FLOAT        | Match confidence score        |
| verdict        | ENUM         | Recognition result            |
| image_ref      | VARCHAR      | Reference to captured image   |
+----------------+--------------+-------------------------------+
```

**Alerts Table**
```
+----------------+--------------+-------------------------------+
| Column         | Type         | Description                   |
+----------------+--------------+-------------------------------+
| id             | UUID         | Primary key                   |
| event_id       | UUID         | Reference to recognition event|
| alert_type     | ENUM         | Type of alert                 |
| severity       | ENUM         | Alert severity level          |
| status         | ENUM         | Alert status                  |
| resolved_by    | UUID         | User who resolved the alert   |
| resolved_at    | TIMESTAMP    | Resolution timestamp          |
| notes          | TEXT         | Resolution notes              |
+----------------+--------------+-------------------------------+
```

## Scalability Considerations

The AI-Guard architecture is designed to scale in the following ways:

### Horizontal Scaling

- **Camera Integration**: Support for multiple camera feeds
- **Recognition Workers**: Parallel processing of video streams
- **API Instances**: Multiple API servers behind a load balancer

### Vertical Scaling

- **GPU Acceleration**: Utilization of GPU resources for ML workloads
- **Memory Optimization**: Efficient handling of face embeddings
- **Model Quantization**: Reduced precision for faster inference

### Performance Optimization

- **Batch Processing**: Processing multiple frames simultaneously
- **Resolution Scaling**: Adaptive resolution based on hardware capabilities
- **Caching**: Frequently accessed embeddings stored in memory

## Security Architecture

### Data Protection

- **Embedding Encryption**: Face embeddings stored in encrypted form
- **Secure Communication**: TLS for all network communications
- **Authentication**: JWT-based authentication for API access

### Privacy Considerations

- **Data Minimization**: Storing only necessary personal information
- **Consent Management**: Tracking user consent for biometric data
- **Retention Policies**: Automatic purging of outdated data

### Access Control

- **Role-Based Access**: Permissions based on user roles
- **Audit Logging**: All system actions are logged
- **IP Restrictions**: Access limited to authorized networks

## Integration Interfaces

The planned production system will provide the following integration points:

### RESTful API

```
POST   /api/auth/login             # User authentication
GET    /api/users                  # List system users
POST   /api/users                  # Create system user
GET    /api/individuals            # List enrolled individuals
POST   /api/individuals            # Enroll new individual
GET    /api/recognition/status     # Get recognition service status
POST   /api/recognition/identify   # Identify an individual from image
GET    /api/alerts                 # List active alerts
PUT    /api/alerts/{id}/resolve    # Resolve an alert
```

### Webhook Notifications

External systems can receive notifications through webhooks:

- Alert triggers
- Recognition events
- System status changes

### File System Integration

Exported data available in standard formats:

- CSV exports of recognition logs
- Image exports of alert events
- Backup/restore functionality for embeddings

## Deployment Architecture

### Development Environment

- Local development using Docker containers
- Integration testing with mock cameras

### Testing Environment

- Isolated testing environment
- Synthetic data for performance testing
- Automated test suite

### Production Environment

- Kubernetes cluster for container orchestration
- High-availability configuration
- Automated scaling based on load
- Geographic distribution for multi-site deployments

## Next Steps

- [Data Models](data-model.md) - Learn about the system's data structures
- [ML Models](models.md) - Understand the machine learning components
- [API Documentation](api.md) - Explore the system's interfaces