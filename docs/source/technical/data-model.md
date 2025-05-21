# Data Models

This document describes the data structures and data flow used in the AI-Guard facial recognition security system.

## Overview

AI-Guard uses several data models to represent different entities within the system:

1. **User Data**: Information about system operators (administrators, enrollment operators, security guards)
2. **Enrolled Individuals**: Data about people registered in the face recognition database
3. **Face Embeddings**: Numerical representations of facial features used for recognition
4. **Recognition Events**: Records of face detection and recognition activities
5. **Security Alerts**: Notifications generated for unauthorized access attempts
6. **System Configuration**: Settings that control system behavior

## Current Implementation

In the current proof-of-concept implementation, data is stored in simple file-based formats:

### File Structure

```
ai-guard/
├── data/
│   ├── embeddings/           # Face embedding files
│   │   ├── 001_john_doe.pkl  # Individual embeddings
│   │   └── ...
│   ├── enrolled_individuals.json  # Enrolled person metadata
│   ├── system_users.json     # System user accounts
│   ├── recognition_logs.csv  # Recognition event logs
│   └── alerts.json           # Security alert records
├── config/
│   ├── .env                  # Environment configuration
│   └── model_config.json     # ML model configuration
└── logs/
    ├── app.log               # Application logs
    └── error.log             # Error logs
```

### Data Serialization

The current implementation uses:

- **JSON**: For structured data that needs to be human-readable
- **CSV**: For tabular data and logs
- **Pickle**: For binary data like face embeddings
- **Environment Variables**: For configuration settings

## Data Models in Detail

### System User Model

Represents operators who use the AI-Guard system:

```json
{
  "id": "usr_123456",
  "username": "guard1",
  "password_hash": "$2b$12$...",
  "full_name": "John Smith",
  "email": "john.smith@example.com",
  "role": "guard",
  "status": "active",
  "created_at": "2023-09-15T14:32:10Z",
  "last_login": "2023-09-16T08:15:22Z"
}
```

Key fields:
- **id**: Unique identifier for the user
- **username**: Login identifier
- **password_hash**: Securely hashed password (not stored in plaintext)
- **role**: User access level (admin, enroller, guard)
- **status**: Account status (active, inactive, suspended)

### Enrolled Individual Model

Represents a person registered in the face recognition database:

```json
{
  "id": "ind_789012",
  "full_name": "Jane Doe",
  "department": "IT",
  "access_level": "standard",
  "status": "active",
  "enrolled_by": "usr_123456",
  "enrollment_date": "2023-09-15T10:25:43Z",
  "last_updated": "2023-09-15T10:25:43Z",
  "embedding_files": {
    "front": "data/embeddings/789012_jane_doe_front.pkl",
    "left": "data/embeddings/789012_jane_doe_left.pkl",
    "right": "data/embeddings/789012_jane_doe_right.pkl"
  }
}
```

Key fields:
- **id**: Unique identifier for the individual
- **full_name**: Individual's name
- **access_level**: Authorized access permission level
- **status**: Enrollment status (active, inactive)
- **embedding_files**: Paths to stored face embeddings

### Face Embedding Model

Face embeddings are numerical vector representations of facial features:

```python
# Structure of a face embedding object
{
  "individual_id": "ind_789012",
  "model_version": "facenet_v1.0",
  "embedding_type": "front",
  "quality_score": 0.92,
  "creation_date": "2023-09-15T10:24:32Z",
  "embedding": numpy.ndarray(shape=(512,), dtype=float32)  # 512-dimensional vector
}
```

Key fields:
- **individual_id**: Reference to the enrolled individual
- **model_version**: Version of the model used to generate the embedding
- **embedding_type**: Angle/type of the face capture (front, left, right)
- **quality_score**: Quality assessment of the source image
- **embedding**: The actual numerical embedding vector (typically 512 dimensions)

### Recognition Event Model

Records a face detection and recognition attempt:

```json
{
  "id": "evt_456789",
  "timestamp": "2023-09-16T15:45:22Z",
  "camera_id": "cam_entrance_main",
  "location": "Main Entrance",
  "faces_detected": 1,
  "recognition_results": [
    {
      "face_id": "face_1",
      "bounding_box": [125, 80, 100, 100],
      "matched_individual": "ind_789012",
      "confidence_score": 0.92,
      "verdict": "authorized",
      "processing_time": 0.15
    }
  ],
  "image_path": "data/images/events/evt_456789.jpg"
}
```

Key fields:
- **timestamp**: When the event occurred
- **camera_id**: Identifier for the source camera
- **faces_detected**: Number of faces found in the frame
- **recognition_results**: Details for each detected face
  - **matched_individual**: ID of the recognized person (if any)
  - **confidence_score**: Match certainty (0-1)
  - **verdict**: Recognition decision (authorized, unauthorized, unknown)

### Alert Model

Represents a security alert triggered by the system:

```json
{
  "id": "alt_567890",
  "event_id": "evt_456789",
  "timestamp": "2023-09-16T15:45:23Z",
  "alert_type": "unauthorized_access",
  "severity": "high",
  "camera_id": "cam_entrance_main",
  "location": "Main Entrance",
  "description": "Unauthorized individual detected at Main Entrance",
  "face_image_path": "data/images/alerts/alt_567890.jpg",
  "status": "active",
  "resolved_by": null,
  "resolved_at": null,
  "resolution_notes": null
}
```

Key fields:
- **event_id**: Reference to the recognition event that triggered the alert
- **alert_type**: Category of alert (unauthorized_access, system_error, etc.)
- **severity**: Alert importance level (low, medium, high)
- **status**: Current status (active, acknowledged, resolved)
- **resolved_by**: Reference to the user who resolved the alert (if any)

### Configuration Model

Stores system settings and parameters:

```json
{
  "recognition": {
    "threshold": 0.7,
    "min_face_size": 80,
    "face_detection_model": "mtcnn",
    "face_recognition_model": "facenet",
    "use_gpu": true
  },
  "alerts": {
    "enable_notifications": true,
    "consecutive_frames_required": 3,
    "cooldown_period": 60,
    "email_notifications": false,
    "email_recipients": ["security@example.com"]
  },
  "cameras": {
    "cam_entrance_main": {
      "source": 0,
      "resolution": [640, 480],
      "frame_rate": 15,
      "location": "Main Entrance"
    }
  },
  "storage": {
    "max_log_size_mb": 100,
    "image_retention_days": 30,
    "alert_retention_days": 90
  }
}
```

Key sections:
- **recognition**: Parameters for face detection and recognition
- **alerts**: Settings for the alert system
- **cameras**: Configuration for connected cameras
- **storage**: Data retention and storage policies

## Database Schema (Planned)

The production version will use a relational database with the following schema:

### Users Table

| Column        | Type      | Description                   |
|---------------|-----------|-------------------------------|
| id            | UUID      | Primary key                   |
| username      | VARCHAR   | Login identifier              |
| password_hash | VARCHAR   | Hashed password               |
| full_name     | VARCHAR   | User's full name              |
| email         | VARCHAR   | User's email address          |
| role          | ENUM      | User role                     |
| status        | ENUM      | Account status                |
| created_at    | TIMESTAMP | Account creation timestamp    |
| updated_at    | TIMESTAMP | Last update timestamp         |

### Enrolled Individuals Table

| Column          | Type      | Description                   |
|-----------------|-----------|-------------------------------|
| id              | UUID      | Primary key                   |
| full_name       | VARCHAR   | Individual's full name        |
| department      | VARCHAR   | Department or category        |
| access_level    | ENUM      | Access permission level       |
| status          | ENUM      | Active/Inactive status        |
| enrolled_by     | UUID      | Reference to enrolling user   |
| enrollment_date | TIMESTAMP | Enrollment timestamp          |
| updated_at      | TIMESTAMP | Last update timestamp         |

### Face Embeddings Table

| Column         | Type      | Description                   |
|----------------|-----------|-------------------------------|
| id             | UUID      | Primary key                   |
| individual_id  | UUID      | Reference to individual       |
| embedding_data | BYTEA     | Face embedding vector         |
| angle          | ENUM      | Capture angle                 |
| model_version  | VARCHAR   | Model used for embedding      |
| quality_score  | FLOAT     | Image quality score           |
| created_at     | TIMESTAMP | Creation timestamp            |

### Recognition Events Table

| Column         | Type      | Description                   |
|----------------|-----------|-------------------------------|
| id             | UUID      | Primary key                   |
| timestamp      | TIMESTAMP | Event timestamp               |
| camera_id      | VARCHAR   | Source camera identifier      |
| individual_id  | UUID      | Matched individual (if any)   |
| confidence     | FLOAT     | Match confidence score        |
| verdict        | ENUM      | Recognition result            |
| image_ref      | VARCHAR   | Reference to captured image   |

### Alerts Table

| Column          | Type      | Description                   |
|-----------------|-----------|-------------------------------|
| id              | UUID      | Primary key                   |
| event_id        | UUID      | Reference to recognition event|
| alert_type      | ENUM      | Type of alert                 |
| severity        | ENUM      | Alert severity level          |
| status          | ENUM      | Alert status                  |
| resolved_by     | UUID      | User who resolved the alert   |
| resolved_at     | TIMESTAMP | Resolution timestamp          |
| notes           | TEXT      | Resolution notes              |

## Data Flow

### Enrollment Data Flow

1. **Data Collection**
   - Face images captured from webcam
   - User metadata provided by enrollment operator
   - Quality check performed on images

2. **Data Processing**
   - Face detection on captured images
   - Face alignment and normalization
   - Embedding generation for each angle

3. **Data Storage**
   - Embeddings saved as pickle files
   - Individual metadata saved to JSON file
   - Enrollment event logged

### Recognition Data Flow

1. **Input Acquisition**
   - Frame captured from video feed
   - Frame metadata recorded (timestamp, camera)

2. **Detection Processing**
   - Face detection on frame
   - Bounding box and landmark extraction
   - Face alignment

3. **Recognition Processing**
   - Embedding generation for detected faces
   - Loading of enrolled embeddings
   - Similarity calculation
   - Threshold-based decision

4. **Result Handling**
   - Recognition event record created
   - Alert triggered if unauthorized
   - Event logged to CSV file

## Data Security Considerations

### Data Protection

In the current implementation:
- Face embeddings are stored as local files
- Simple file permissions provide basic protection

In the planned production implementation:
- **Encryption**: All face embeddings will be encrypted at rest
- **Secure Transit**: TLS for all data in transit
- **Access Control**: Fine-grained permissions for data access
- **Auditing**: Complete logs of all data access

### Privacy Considerations

The system implements the following privacy protections:

1. **Data Minimization**
   - Only essential personal data is stored
   - Raw face images are not retained after processing
   - Recognition events retain minimal necessary data

2. **Retention Policies**
   - Configurable retention periods for different data types
   - Automatic purging of outdated data
   - Option to retain only anonymized statistics

3. **User Consent**
   - Explicit consent required before enrollment
   - Clear documentation of data usage
   - Process for removing enrolled data

## Data Model Extension

The data models are designed to be extensible for future requirements:

### Multi-Site Support

Additional fields for multi-location deployments:
- **site_id**: Identifier for physical location
- **zone_id**: Sub-area within a site
- **access_policy**: Site-specific access rules

### Integration with Access Control

Fields for integration with physical access systems:
- **credential_id**: Reference to physical access credential
- **access_points**: List of authorized entry points
- **access_schedule**: Time-based access restrictions

### Advanced Analytics

Fields for security analytics:
- **movement_patterns**: Historical access locations and times
- **verification_history**: Success/failure statistics
- **anomaly_scores**: Deviation from normal behavior patterns

## Next Steps

- [System Architecture](architecture.md) - Learn how these data models fit into the overall system design
- [ML Models](models.md) - Understand how the machine learning models process this data
- [API Documentation](api.md) - Explore the interfaces for data access and manipulation