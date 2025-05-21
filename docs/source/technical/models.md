# Machine Learning Models

This document provides detailed information about the machine learning models used in the AI-Guard system for face detection and recognition.

## Model Architecture Overview

AI-Guard employs a two-stage approach to facial recognition:

1. **Face Detection**: Locating and extracting faces from images or video frames
2. **Face Recognition**: Converting face images to embeddings and matching against known identities

Each stage uses specialized neural network architectures optimized for their specific tasks.

## Face Detection Models

### MTCNN (Multi-task Cascaded Convolutional Networks)

MTCNN is the primary face detection model used in AI-Guard due to its good balance of speed and accuracy.

#### Architecture

MTCNN consists of three stages of convolutional neural networks:

1. **Proposal Network (P-Net)**: A shallow CNN that quickly generates candidate facial regions
2. **Refinement Network (R-Net)**: A more complex CNN that filters candidate regions
3. **Output Network (O-Net)**: The final network that outputs facial landmarks and refined bounding boxes

#### Key Features

- **Cascade Structure**: Progressive refinement of detection results
- **Multi-task Learning**: Simultaneous bounding box regression and facial landmark localization
- **Scale Invariance**: Detection across multiple scales through image pyramid

#### Implementation Details

```python
from mtcnn import MTCNN

# Initialize the detector
detector = MTCNN(min_face_size=80, scale_factor=0.709)

# Detect faces in an image
faces = detector.detect_faces(image)

# Each face contains:
# - 'box': [x, y, width, height]
# - 'confidence': Detection confidence score
# - 'keypoints': Facial landmarks (eyes, nose, mouth)
```

#### Performance Metrics

| Metric | Value |
|--------|-------|
| Average Precision | 95.4% |
| Recall | 93.2% |
| Inference Time (CPU) | ~0.8s per 640x480 image |
| Inference Time (GPU) | ~0.1s per 640x480 image |

### Faster R-CNN

Faster R-CNN is an alternative detection model that provides higher accuracy at the cost of increased computational requirements.

#### Architecture

Faster R-CNN consists of:

1. **Backbone Network**: A pre-trained convolutional network (e.g., ResNet50) that extracts features
2. **Region Proposal Network (RPN)**: Generates region proposals for potential face locations
3. **RoI Pooling**: Extracts fixed-size feature maps from proposals
4. **Classification and Bounding Box Regression**: Final layers for object classification and localization

#### Key Features

- **Two-stage Detection**: Separate region proposal and classification stages
- **Shared Features**: Feature computation is shared between stages for efficiency
- **High Accuracy**: More precise bounding boxes compared to single-stage detectors

#### Implementation Details

```python
import torchvision
from torchvision.models.detection import fasterrcnn_resnet50_fpn

# Initialize the model
detector = fasterrcnn_resnet50_fpn(pretrained=True)
detector.eval()

# Convert to desired device
detector.to(device)

# Inference
with torch.no_grad():
    predictions = detector([transformed_image])

# Extract face detections
boxes = predictions[0]['boxes'].cpu().numpy()
scores = predictions[0]['scores'].cpu().numpy()
```

#### Performance Metrics

| Metric | Value |
|--------|-------|
| Average Precision | 98.7% |
| Recall | 97.5% |
| Inference Time (CPU) | ~1.2s per 640x480 image |
| Inference Time (GPU) | ~0.15s per 640x480 image |

## Face Recognition Models

### FaceNet

FaceNet is the primary face recognition model used in AI-Guard, generating fixed-length embeddings that represent facial features.

#### Architecture

FaceNet uses a deep convolutional neural network architecture:

1. **Base Network**: Inception-ResNet-v1 architecture
2. **Feature Extraction**: Deep feature hierarchy leading to 512-dimensional embedding
3. **L2 Normalization**: Normalization of embeddings to unit length

#### Training Methodology

FaceNet is trained using triplet loss, which optimizes the embedding space to have the following properties:

- Small distances between embeddings of the same identity
- Large distances between embeddings of different identities

#### Implementation Details

```python
from facenet_pytorch import InceptionResnetV1

# Initialize the model
model = InceptionResnetV1(pretrained='vggface2').eval()

# Convert to desired device
model.to(device)

# Generate embedding
with torch.no_grad():
    embedding = model(aligned_face)

# Embedding is a 512-dimensional vector
```

#### Performance Metrics

| Metric | Value |
|--------|-------|
| Verification Accuracy (LFW) | 99.63% |
| False Acceptance Rate @ 0.1% FRR | 0.087% |
| Embedding Dimension | 512 |
| Inference Time (CPU) | ~0.1s per face |
| Inference Time (GPU) | ~0.01s per face |

### ArcFace

ArcFace is an alternative recognition model that provides improved accuracy, especially across diverse demographics.

#### Architecture

ArcFace uses ResNet architectures (50 or 100 layers) with a modified final layer:

1. **Backbone Network**: Deep ResNet architecture
2. **Feature Normalization**: L2 normalization of feature vectors
3. **Angular Margin Penalty**: Modified softmax loss with additive angular margin

#### Key Innovations

- **Additive Angular Margin Loss**: Enhances intra-class compactness and inter-class discrepancy
- **Feature Normalization**: Constrains features to a hypersphere for improved discrimination
- **Distributed Training**: Efficient learning from large-scale datasets

#### Implementation Details

```python
# Using a pre-trained ArcFace model
import torch
from backbones import get_model

# Initialize the model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = get_model('r50', fp16=False)
model.load_state_dict(torch.load('model_weights.pth'))
model.to(device).eval()

# Generate embedding
with torch.no_grad():
    embedding = model(aligned_face)
```

#### Performance Metrics

| Metric | Value |
|--------|-------|
| Verification Accuracy (LFW) | 99.82% |
| Verification Accuracy (CPLFW) | 92.08% |
| Verification Accuracy (CALFW) | 95.45% |
| Embedding Dimension | 512 |
| Inference Time (CPU) | ~0.12s per face |
| Inference Time (GPU) | ~0.015s per face |

### ResNet18

ResNet18 is a lighter-weight model used in scenarios with limited computational resources.

#### Architecture

ResNet18 is a lightweight residual network:

1. **Residual Blocks**: Contains 18 layers with skip connections
2. **Global Average Pooling**: Reduces spatial dimensions to produce feature vector
3. **Modified Final Layer**: Customized for face recognition task

#### Advantages

- **Computational Efficiency**: Lower resource requirements compared to deeper models
- **Fast Inference**: Suitable for edge deployments and real-time applications
- **Acceptable Accuracy**: Reasonable performance for most use cases

#### Implementation Details

```python
import torch
import torchvision.models as models

# Initialize model
model = models.resnet18(pretrained=True)
model.fc = torch.nn.Linear(512, 512)  # Modify for face embeddings
model.eval()

# Generate embedding
with torch.no_grad():
    embedding = model(aligned_face)
```

#### Performance Metrics

| Metric | Value |
|--------|-------|
| Verification Accuracy (LFW) | 98.65% |
| Embedding Dimension | 512 |
| Inference Time (CPU) | ~0.05s per face |
| Inference Time (GPU) | ~0.005s per face |

## Fine-Tuning and Adaptation

### Dataset Augmentation

To improve model robustness, AI-Guard applies the following augmentation techniques:

- **Geometric Transformations**: Rotation, scaling, and translation
- **Photometric Transformations**: Brightness, contrast, and color adjustments
- **Noise Addition**: Gaussian and salt-and-pepper noise
- **Occlusion Simulation**: Random patches to simulate partial face covering

### Transfer Learning

AI-Guard adapts pre-trained models to its specific requirements:

1. **Base Model**: Use pre-trained weights from public datasets
2. **Fine-Tuning**: Update model weights using the custom ENSAM dataset
3. **Layer Freezing**: Keep early layers fixed, train only later layers

### Knowledge Distillation

For deployment on resource-constrained environments:

1. **Teacher Model**: Full-size ArcFace or FaceNet model
2. **Student Model**: Lightweight ResNet18 model
3. **Distillation Loss**: Student trained to mimic teacher's embedding space

## Recognition Process

### Face Preprocessing

Before recognition, faces undergo several preprocessing steps:

1. **Alignment**: Rotation based on eye coordinates
2. **Cropping**: Extraction of face region with margin
3. **Resizing**: Standardization to model input dimensions
4. **Normalization**: Pixel value scaling and standardization

### Embedding Generation

Face embeddings are generated as follows:

1. **Forward Pass**: Preprocessed face is passed through the model
2. **Feature Extraction**: Last fully connected layer output is captured
3. **Normalization**: L2 normalization to create unit vector

### Similarity Computation

Identity matching uses cosine similarity between embeddings:

```python
def cosine_similarity(embedding1, embedding2):
    """Compute cosine similarity between two embeddings."""
    return np.dot(embedding1, embedding2) / (
        np.linalg.norm(embedding1) * np.linalg.norm(embedding2)
    )
```

### Multi-Angle Fusion

AI-Guard leverages multiple face angles for improved recognition:

1. **Separate Embeddings**: Generate embeddings for front, left, and right angles
2. **Weighted Fusion**: Combine embeddings with angle-specific weights
3. **Template Matching**: Compare against similarly constructed templates

## Model Evaluation

### Evaluation Metrics

AI-Guard evaluates recognition performance using:

- **True Acceptance Rate (TAR)**: Correct acceptance of authorized individuals
- **False Acceptance Rate (FAR)**: Incorrect acceptance of unauthorized individuals
- **True Rejection Rate (TRR)**: Correct rejection of unauthorized individuals
- **False Rejection Rate (FRR)**: Incorrect rejection of authorized individuals
- **Equal Error Rate (EER)**: Operating point where FAR equals FRR

### Performance Analysis

Based on internal testing with the ENSAM dataset:

| Model Combination | TAR @ 0.1% FAR | EER | Inference Time |
|-------------------|----------------|-----|----------------|
| MTCNN + FaceNet   | 98.7%          | 1.3% | 0.15s         |
| MTCNN + ArcFace   | 99.1%          | 0.9% | 0.17s         |
| Faster R-CNN + FaceNet | 99.3%     | 0.7% | 0.25s         |
| Faster R-CNN + ArcFace | 99.5%     | 0.5% | 0.27s         |
| MTCNN + ResNet18  | 97.8%          | 2.2% | 0.09s         |

### Cross-Dataset Evaluation

To assess generalization capability, models were evaluated on external datasets:

| Dataset | MTCNN + FaceNet | MTCNN + ArcFace | Faster R-CNN + ArcFace |
|---------|-----------------|-----------------|------------------------|
| LFW     | 99.5%           | 99.7%           | 99.8%                  |
| CPLFW   | 92.1%           | 94.3%           | 95.2%                  |
| CALFW   | 95.3%           | 96.8%           | 97.3%                  |

## Model Selection Guidelines

### Use Case: Standard Security

For typical security monitoring with balanced requirements:

- **Detection Model**: MTCNN
- **Recognition Model**: FaceNet
- **Threshold**: 0.7 (70% similarity)

### Use Case: High Security

For areas requiring stricter access control:

- **Detection Model**: Faster R-CNN
- **Recognition Model**: ArcFace
- **Threshold**: 0.8 (80% similarity)

### Use Case: Resource-Constrained

For deployment on systems with limited computational power:

- **Detection Model**: MTCNN (with reduced minimum face size)
- **Recognition Model**: ResNet18
- **Threshold**: 0.65 (65% similarity)

## Model Limitations

### Known Challenges

- **Extreme Pose Variations**: Performance degrades with head poses beyond ±45°
- **Poor Lighting Conditions**: Recognition accuracy drops in very low light
- **Occlusions**: Masks, glasses, and other face coverings reduce accuracy
- **Identical Twins**: May have difficulty distinguishing between identical twins
- **Age Progression**: Recognition accuracy may decrease as individuals age

### Mitigation Strategies

- **Multi-Angle Enrollment**: Capture faces from multiple viewpoints
- **Regular Re-enrollment**: Update embeddings periodically
- **Adaptive Thresholds**: Adjust confidence thresholds based on conditions
- **Preprocessing Enhancement**: Apply histogram equalization for poor lighting
- **Ensemble Methods**: Combine results from multiple models

## Future Model Improvements

### Planned Enhancements

- **Attention Mechanisms**: Incorporate attention layers for better feature extraction
- **Anti-Spoofing**: Add liveness detection to prevent presentation attacks
- **Demographic Fairness**: Further reduce bias across different demographic groups
- **Model Quantization**: Optimize models for edge deployment
- **Transformer Architectures**: Evaluate Vision Transformer (ViT) based approaches

### Research Directions

- **Self-supervised Learning**: Reduce reliance on labeled data
- **Continuous Learning**: Update models with new data without full retraining
- **Explainable AI**: Enhance model interpretability for security applications
- **Privacy-Preserving Recognition**: Develop methods that maintain privacy guarantees

## Integration with Other Components

### Data Pipeline

See the [System Architecture](architecture.md) document for details on how these models integrate with:

- **Camera Feed Processing**: Video frame acquisition and preprocessing
- **Alert System**: Generation of security alerts based on recognition results
- **User Interface**: Visualization of detection and recognition results

### Model Deployment

Models are deployed using the following approach:

1. **Model Export**: Conversion to optimized formats (ONNX, TorchScript)
2. **Runtime Optimization**: Application of quantization and pruning
3. **Containerization**: Packaging in Docker containers for consistent deployment
4. **Versioning**: Strict version control of deployed models

## Next Steps

- [Data Model](data-model.md) - Learn about the system's data structures
- [System Architecture](architecture.md) - Understand the overall system design
- [API Documentation](api.md) - Explore the system's interfaces