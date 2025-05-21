# API Documentation

This document provides technical reference for the AI-Guard system's internal and external APIs. While the current proof-of-concept implementation does not yet offer a complete API, this documentation outlines the planned interfaces for the production system.

## API Overview

The AI-Guard system will provide several APIs:

1. **Core API**: Internal interfaces between system components
2. **REST API**: External HTTP interface for integration with other systems
3. **Webhook API**: Event-based notifications to external systems
4. **Command-Line Interface**: Administrative tools for system management

## Core API

The Core API consists of internal Python interfaces used by different components of the AI-Guard system.

### Face Detection API

```python
class FaceDetector:
    def __init__(self, model_type="mtcnn", min_face_size=80, scale_factor=0.709, device="cpu"):
        """Initialize face detector.
        
        Args:
            model_type: Type of detector model ("mtcnn", "faster_rcnn", or "retinaface")
            min_face_size: Minimum face size in pixels to detect
            scale_factor: Scale factor for detection at multiple resolutions
            device: Computation device ("cpu" or "cuda")
        """
        pass
    
    def detect_faces(self, image):
        """Detect faces in an image.
        
        Args:
            image: Input image as numpy array (BGR format)
            
        Returns:
            List of dictionaries, each containing:
                - box: [x, y, width, height]
                - confidence: Detection confidence score
                - keypoints: Dictionary of facial landmarks
        """
        pass
    
    def align_face(self, image, face_box, face_landmarks):
        """Align face to standardized position based on landmarks.
        
        Args:
            image: Input image as numpy array
            face_box: Bounding box [x, y, width, height]
            face_landmarks: Dictionary of facial landmarks
            
        Returns:
            Aligned face image as numpy array
        """
        pass
```

### Face Recognition API

```python
class FaceRecognizer:
    def __init__(self, model_type="facenet", threshold=0.7, device="cpu"):
        """Initialize face recognizer.
        
        Args:
            model_type: Type of recognition model ("facenet", "arcface", or "resnet18")
            threshold: Similarity threshold for positive match
            device: Computation device ("cpu" or "cuda")
        """
        pass
    
    def generate_embedding(self, face_image):
        """Generate embedding for a face image.
        
        Args:
            face_image: Aligned face image as numpy array
            
        Returns:
            Face embedding as numpy array
        """
        pass
    
    def compare_embeddings(self, embedding1, embedding2):
        """Compare two face embeddings.
        
        Args:
            embedding1: First face embedding
            embedding2: Second face embedding
            
        Returns:
            Similarity score between 0 and 1
        """
        pass
    
    def identify_face(self, face_image, enrolled_embeddings):
        """Identify a face against enrolled embeddings.
        
        Args:
            face_image: Aligned face image
            enrolled_embeddings: Dictionary mapping IDs to embeddings
            
        Returns:
            Tuple of (identity, confidence_score) or (None, 0) if no match
        """
        pass
```

### Enrollment API

```python
class EnrollmentManager:
    def __init__(self, detector, recognizer, quality_check=True):
        """Initialize enrollment manager.
        
        Args:
            detector: FaceDetector instance
            recognizer: FaceRecognizer instance
            quality_check: Whether to perform quality validation
        """
        pass
    
    def process_enrollment_image(self, image, angle):
        """Process a single enrollment image.
        
        Args:
            image: Face image as numpy array
            angle: Capture angle ("front", "left", or "right")
            
        Returns:
            Tuple of (processed_image, quality_score, face_landmarks)
        """
        pass
    
    def generate_enrollment_embedding(self, images):
        """Generate embeddings from multiple enrollment images.
        
        Args:
            images: Dictionary mapping angles to face images
            
        Returns:
            Dictionary mapping angles to embeddings
        """
        pass
    
    def save_enrollment(self, individual_data, embeddings):
        """Save enrollment data and embeddings.
        
        Args:
            individual_data: Dictionary of individual metadata
            embeddings: Dictionary mapping angles to embeddings
            
        Returns:
            Individual ID if successful, None otherwise
        """
        pass
    
    def update_enrollment(self, individual_id, embeddings=None, metadata=None):
        """Update an existing enrollment.
        
        Args:
            individual_id: ID of the individual to update
            embeddings: New embeddings (optional)
            metadata: Updated metadata (optional)
            
        Returns:
            True if successful, False otherwise
        """
        pass
```

### Alert API

```python
class AlertManager:
    def __init__(self, config):
        """Initialize alert manager.
        
        Args:
            config: Alert configuration dictionary
        """
        pass
    
    def process_recognition_event(self, event):
        """Process a recognition event and generate alerts if needed.
        
        Args:
            event: Recognition event dictionary
            
        Returns:
            List of generated alert objects (if any)
        """
        pass
    
    def send_notification(self, alert, channels=None):
        """Send notification for an alert.
        
        Args:
            alert: Alert object
            channels: List of notification channels (default: all configured)
            
        Returns:
            Dictionary of notification statuses by channel
        """
        pass
    
    def get_active_alerts(self, location=None, since=None):
        """Get active alerts with optional filtering.
        
        Args:
            location: Filter by location (optional)
            since: Time threshold (optional)
            
        Returns:
            List of active alert objects
        """
        pass
    
    def resolve_alert(self, alert_id, resolved_by, resolution_notes=None):
        """Mark an alert as resolved.
        
        Args:
            alert_id: ID of the alert to resolve
            resolved_by: ID of the user resolving the alert
            resolution_notes: Optional notes about the resolution
            
        Returns:
            True if successful, False otherwise
        """
        pass
```

## REST API

The planned REST API will provide HTTP endpoints for external system integration. All endpoints will require authentication using JSON Web Tokens (JWT).

### Authentication Endpoints

```
POST /api/auth/login
- Request: { "username": "user", "password": "pass" }
- Response: { "token": "eyJhbGciOiJIUzI...", "expires_at": "2023-09-30T14:30:00Z" }

POST /api/auth/refresh
- Request: { "refresh_token": "eyJhbGciOiJIUzI..." }
- Response: { "token": "eyJhbGciOiJIUzI...", "expires_at": "2023-09-30T14:30:00Z" }

POST /api/auth/logout
- Request: {}
- Response: { "success": true }
```

### User Management Endpoints

```
GET /api/users
- Response: List of system users

POST /api/users
- Request: { "username": "new_user", "full_name": "New User", "email": "user@example.com", "role": "guard" }
- Response: Created user object

GET /api/users/{id}
- Response: User object

PUT /api/users/{id}
- Request: { "email": "updated@example.com", "role": "admin" }
- Response: Updated user object

DELETE /api/users/{id}
- Response: { "success": true }
```

### Enrollment Endpoints

```
GET /api/individuals
- Response: List of enrolled individuals

POST /api/individuals
- Request: 
  {
    "full_name": "Jane Doe",
    "department": "IT",
    "access_level": "standard",
    "images": {
      "front": "base64-encoded-image",
      "left": "base64-encoded-image",
      "right": "base64-encoded-image"
    }
  }
- Response: Created individual object

GET /api/individuals/{id}
- Response: Individual object with enrollment details

PUT /api/individuals/{id}
- Request: { "department": "HR", "access_level": "restricted" }
- Response: Updated individual object

DELETE /api/individuals/{id}
- Response: { "success": true }
```

### Recognition Endpoints

```
POST /api/recognition/identify
- Request: { "image": "base64-encoded-image" }
- Response: 
  {
    "faces_detected": 1,
    "results": [
      {
        "box": [125, 80, 100, 100],
        "individual_id": "ind_789012",
        "full_name": "Jane Doe",
        "confidence": 0.92,
        "verdict": "authorized"
      }
    ]
  }

GET /api/recognition/events
- Response: List of recent recognition events

GET /api/recognition/events/{id}
- Response: Details of specific recognition event
```

### Alert Endpoints

```
GET /api/alerts
- Response: List of alerts

GET /api/alerts/{id}
- Response: Alert details

PUT /api/alerts/{id}/resolve
- Request: { "resolution_notes": "False alarm" }
- Response: Updated alert object

GET /api/alerts/statistics
- Response: Alert statistics and trends
```

### System Configuration Endpoints

```
GET /api/config
- Response: System configuration

PUT /api/config
- Request: Updated configuration values
- Response: New configuration

GET /api/status
- Response: System status information
```

## Webhook API

The Webhook API allows external systems to receive event notifications from AI-Guard:

### Webhook Registration

```
POST /api/webhooks
- Request:
  {
    "url": "https://example.com/webhook",
    "events": ["alert.created", "recognition.unauthorized"],
    "secret": "shared_secret_for_signature"
  }
- Response: { "id": "webhook_123", "status": "active" }
```

### Webhook Payload Format

```json
{
  "event_type": "alert.created",
  "timestamp": "2023-09-16T15:45:23Z",
  "data": {
    "alert_id": "alt_567890",
    "alert_type": "unauthorized_access",
    "location": "Main Entrance",
    "severity": "high"
  },
  "signature": "HMAC-SHA256 signature"
}
```

### Available Event Types

- `recognition.authorized`: Triggered when an authorized individual is recognized
- `recognition.unauthorized`: Triggered when an unauthorized individual is detected
- `alert.created`: Triggered when a new alert is generated
- `alert.resolved`: Triggered when an alert is resolved
- `enrollment.completed`: Triggered when a new enrollment is completed
- `system.status_change`: Triggered when system status changes

## Command-Line Interface

The planned command-line interface will provide administrative tools:

```bash
# User management
ai-guard-admin user list
ai-guard-admin user create --username admin2 --role admin
ai-guard-admin user update --id usr_123456 --role guard
ai-guard-admin user delete --id usr_123456

# Enrollment management
ai-guard-admin enrollment list
ai-guard-admin enrollment update --id ind_789012 --status inactive
ai-guard-admin enrollment delete --id ind_789012

# System management
ai-guard-admin config show
ai-guard-admin config update --recognition.threshold 0.75
ai-guard-admin backup create
ai-guard-admin restore --file backup-20230916.zip
ai-guard-admin logs show --service recognition --lines 100
```

## API Implementation Status

The current proof-of-concept implementation includes:

- ✅ Core Face Detection API: Basic implementation
- ✅ Core Face Recognition API: Basic implementation
- ✅ Core Enrollment API: Basic implementation
- ⚠️ Core Alert API: Partial implementation
- ❌ REST API: Planned for future release
- ❌ Webhook API: Planned for future release
- ❌ Command-Line Interface: Planned for future release

## Error Handling

All API endpoints follow consistent error handling patterns:

### REST API Error Responses

```json
{
  "error": {
    "code": "invalid_request",
    "message": "Invalid request format",
    "details": {
      "field": "images.front",
      "issue": "Required field missing"
    }
  }
}
```

Common error codes:
- `authentication_failed`: Invalid credentials
- `authorization_failed`: Insufficient permissions
- `invalid_request`: Malformed request
- `resource_not_found`: Requested resource doesn't exist
- `validation_failed`: Input validation failed
- `rate_limit_exceeded`: Too many requests
- `server_error`: Internal server error

### Core API Exceptions

```python
# Example exception hierarchy
class AIGuardError(Exception):
    """Base exception for all AI-Guard errors."""
    pass

class DetectionError(AIGuardError):
    """Raised when face detection fails."""
    pass

class RecognitionError(AIGuardError):
    """Raised when face recognition fails."""
    pass

class EnrollmentError(AIGuardError):
    """Raised when enrollment operations fail."""
    pass

class ConfigurationError(AIGuardError):
    """Raised for configuration issues."""
    pass
```

## API Usage Examples

### Face Detection Example

```python
from ai_guard.detection import FaceDetector
import cv2

# Initialize the detector
detector = FaceDetector(model_type="mtcnn", min_face_size=80)

# Load image
image = cv2.imread("test_image.jpg")

# Detect faces
faces = detector.detect_faces(image)

# Process detection results
for face in faces:
    x, y, w, h = face["box"]
    confidence = face["confidence"]
    landmarks = face["keypoints"]
    
    # Draw bounding box
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display confidence score
    cv2.putText(image, f"{confidence:.2f}", (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Extract and align face
    aligned_face = detector.align_face(image, face["box"], face["keypoints"])
    
    # Save aligned face
    cv2.imwrite(f"aligned_face_{x}_{y}.jpg", aligned_face)

# Save output image
cv2.imwrite("output.jpg", image)
```

### Face Recognition Example

```python
from ai_guard.detection import FaceDetector
from ai_guard.recognition import FaceRecognizer
import cv2
import pickle
import os

# Initialize components
detector = FaceDetector(model_type="mtcnn")
recognizer = FaceRecognizer(model_type="facenet", threshold=0.7)

# Load enrolled embeddings
enrolled_embeddings = {}
embeddings_dir = "data/embeddings"
for filename in os.listdir(embeddings_dir):
    if filename.endswith(".pkl"):
        individual_id = filename.split("_")[0]
        with open(os.path.join(embeddings_dir, filename), "rb") as f:
            embedding = pickle.load(f)
            enrolled_embeddings[individual_id] = embedding

# Process image
image = cv2.imread("test_image.jpg")
faces = detector.detect_faces(image)

# Recognize each face
for face in faces:
    x, y, w, h = face["box"]
    
    # Align face
    aligned_face = detector.align_face(image, face["box"], face["keypoints"])
    
    # Identify face
    identity, confidence = recognizer.identify_face(aligned_face, enrolled_embeddings)
    
    # Draw results
    color = (0, 255, 0) if identity else (0, 0, 255)
    label = f"{identity}: {confidence:.2f}" if identity else "Unknown"
    
    cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)
    cv2.putText(image, label, (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Save output image
cv2.imwrite("recognition_output.jpg", image)
```

### Enrollment Example

```python
from ai_guard.detection import FaceDetector
from ai_guard.recognition import FaceRecognizer
from ai_guard.enrollment import EnrollmentManager
import cv2

# Initialize components
detector = FaceDetector(model_type="mtcnn")
recognizer = FaceRecognizer(model_type="facenet")
enrollment_manager = EnrollmentManager(detector, recognizer, quality_check=True)

# Capture or load enrollment images
front_image = cv2.imread("front.jpg")
left_image = cv2.imread("left.jpg")
right_image = cv2.imread("right.jpg")

# Process enrollment images
front_processed, front_quality, _ = enrollment_manager.process_enrollment_image(front_image, "front")
left_processed, left_quality, _ = enrollment_manager.process_enrollment_image(left_image, "left")
right_processed, right_quality, _ = enrollment_manager.process_enrollment_image(right_image, "right")

# Check quality scores
if min(front_quality, left_quality, right_quality) < 0.7:
    print("Image quality too low. Please recapture.")
else:
    # Generate embeddings
    images = {
        "front": front_processed,
        "left": left_processed,
        "right": right_processed
    }
    embeddings = enrollment_manager.generate_enrollment_embedding(images)
    
    # Save enrollment
    individual_data = {
        "full_name": "Jane Doe",
        "department": "IT",
        "access_level": "standard"
    }
    individual_id = enrollment_manager.save_enrollment(individual_data, embeddings)
    
    if individual_id:
        print(f"Enrollment successful. ID: {individual_id}")
    else:
        print("Enrollment failed.")
```

## API Security

The AI-Guard API implements several security measures:

### Authentication

- REST API uses JWT (JSON Web Tokens) for authentication
- Tokens expire after a configurable period
- Refresh tokens allow extended sessions without re-authentication

### Authorization

- Role-based access control restricts API endpoint access
- Permission checks on all sensitive operations
- Resource ownership validation

### Data Protection

- HTTPS required for all API communications
- Sensitive data encrypted in transit and at rest
- Input validation to prevent injection attacks
- Rate limiting to prevent abuse

## Next Steps

- [System Architecture](architecture.md) - Learn how these APIs fit into the overall system design
- [Data Models](data-model.md) - Understand the data structures used by these APIs
- [ML Models](models.md) - Learn about the machine learning models behind the face detection and recognition APIs