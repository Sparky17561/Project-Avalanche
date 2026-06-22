# Deep Learning - Introduction

> Project Avalanche - AI Foundations
>
> Goal: Build a strong conceptual understanding of Deep Learning before moving into Neural Networks, Transformers, LLMs, and AI Systems.

---

# What is Deep Learning?

Deep Learning (DL) is a subfield of Artificial Intelligence (AI) and Machine Learning (ML) inspired by the structure and functioning of the human brain.

It uses **Artificial Neural Networks (ANNs)** with multiple layers to learn patterns directly from data.

Instead of manually creating features, Deep Learning automatically learns useful representations from raw input data.

---

# AI vs ML vs DL

```text
Artificial Intelligence (AI)
│
├── Machine Learning (ML)
│   │
│   └── Deep Learning (DL)
│
└── Other AI Techniques
```

### Artificial Intelligence

Broad field focused on creating systems capable of intelligent behavior.

Examples:

- Chess Engines
- Expert Systems
- Self Driving Cars
- ChatGPT

---

### Machine Learning

Subset of AI where systems learn patterns from data.

Examples:

- Spam Detection
- House Price Prediction
- Recommendation Systems

---

### Deep Learning

Subset of ML that uses Neural Networks with many hidden layers.

Examples:

- GPT
- BERT
- ResNet
- YOLO

---

# Why is it called "Deep"?

The term **Deep** refers to the presence of multiple hidden layers in a Neural Network.

```text
Input Layer
     ↓
Hidden Layer 1
     ↓
Hidden Layer 2
     ↓
Hidden Layer 3
     ↓
Output Layer
```

More hidden layers allow the model to learn increasingly complex patterns.

---

# Why Deep Learning Became Popular

Deep Learning existed for decades but became practical because of:

### 1. More Data

Internet generated massive datasets.

Examples:

- Images
- Videos
- Text
- Audio

---

### 2. Better Hardware

GPUs made neural network training much faster.

Training that took months became possible in hours or days.

---

### 3. Improved Algorithms

Advancements such as:

- Better Activation Functions
- Better Optimizers
- Better Weight Initialization
- Batch Normalization

improved performance significantly.

---

### 4. Better Results

Deep Learning outperformed traditional ML in:

- Computer Vision
- NLP
- Speech Recognition
- Recommendation Systems

---

# Traditional Machine Learning vs Deep Learning

## Traditional ML

Feature engineering is performed manually.

Example:

Cat vs Dog Classification

Human manually extracts:

- Ear Shape
- Fur Color
- Tail Length

Then trains model.

```text
Raw Data
    ↓
Feature Engineering
    ↓
ML Algorithm
    ↓
Prediction
```

---

## Deep Learning

Feature engineering is automatic.

```text
Raw Data
    ↓
Neural Network
    ↓
Prediction
```

The network learns useful features by itself.

---

# How Deep Learning Learns

Deep Learning models learn hierarchical representations.

Example: Image Recognition

### Layer 1

Learns:

- Edges
- Corners

---

### Layer 2

Learns:

- Curves
- Shapes

---

### Layer 3

Learns:

- Eyes
- Nose
- Mouth

---

### Layer 4

Learns:

- Human Face

```text
Pixels
 ↓
Edges
 ↓
Shapes
 ↓
Parts
 ↓
Objects
```

---

# Famous Deep Learning Models

## Image Classification

### ResNet

Used for image recognition.

---

## Text Classification

### BERT

Used in:

- Search
- Question Answering
- NLP Tasks

---

## Image Segmentation

### U-Net

Used in:

- Medical Imaging
- Satellite Imaging

---

## Object Detection

### YOLO (You Only Look Once)

Used for:

- Real-time Detection
- Autonomous Vehicles
- Surveillance Systems

---

## Image Generation

### DALL-E

Text → Image Generation

---

## Speech Generation

### WaveNet

Text → Speech Generation

---

# Major Types of Neural Networks

---

## 1. MLP (Multi Layer Perceptron)

Simplest neural network architecture.

```text
Input
 ↓
Hidden Layers
 ↓
Output
```

Used for:

- Classification
- Regression

---

## 2. CNN (Convolutional Neural Network)

Designed for image data.

Learns:

- Edges
- Textures
- Objects

Applications:

- Face Recognition
- Medical Imaging
- Object Detection

---

## 3. RNN (Recurrent Neural Network)

Designed for sequential data.

Unlike standard feedforward networks, RNNs contain feedback loops.

Applications:

- Text Processing
- Speech Recognition
- Time Series Forecasting

---

## 4. LSTM (Long Short-Term Memory)

Improved version of RNN.

Solves long-term dependency problems.

Applications:

- NLP
- Language Modeling
- Machine Translation

---

## 5. Autoencoders

Used for learning compressed representations.

```text
Input
 ↓
Encoder
 ↓
Latent Space
 ↓
Decoder
 ↓
Output
```

Applications:

- Compression
- Denoising
- Feature Learning

---

## 6. GAN (Generative Adversarial Network)

Consists of:

### Generator

Creates fake data.

### Discriminator

Checks if data is real or fake.

Applications:

- Image Generation
- Deepfakes
- Synthetic Data

```text
Generator
    ↓
Fake Image
    ↓
Discriminator
```

---

# Applications of Deep Learning

## Computer Vision

- Image Classification
- Face Recognition
- Object Detection

---

## Natural Language Processing

- ChatGPT
- BERT
- Translation Systems

---

## Speech Processing

- Siri
- Alexa
- Voice Assistants

---

## Healthcare

- Disease Detection
- Medical Imaging
- Drug Discovery

---

## Finance

- Fraud Detection
- Risk Assessment
- Algorithmic Trading

---

## Autonomous Vehicles

- Lane Detection
- Object Detection
- Navigation

---

# Key Takeaways

1. Deep Learning is a subset of Machine Learning.
2. Deep Learning uses Neural Networks with multiple layers.
3. Deep Learning automatically learns features from raw data.
4. CNNs are mainly used for images.
5. RNNs and LSTMs are used for sequential data.
6. GANs generate new data.
7. Deep Learning became practical due to big data, GPUs, and better algorithms.
8. Modern AI systems such as GPT, BERT, YOLO, and DALL-E are built using Deep Learning concepts.

---

# Next Topic

➡️ Perceptron

Questions to answer before moving on:

- What is a neuron?
- What is a perceptron?
- Why can't a perceptron solve every problem?
- What is the XOR problem?