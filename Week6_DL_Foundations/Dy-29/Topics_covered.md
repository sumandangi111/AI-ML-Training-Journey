# Deep Learning & Transformers

---

# 1. Neural Networks

## What is a Neural Network?

A Neural Network is a computer system inspired by the human brain.

It contains many small processing units called:

- Neurons

These neurons work together to learn patterns from data.

---

## Simple Understanding

Example:

Suppose we want AI to identify cats.

The neural network learns:

```text
Edges → Shapes → Eyes → Face → Cat
```

---

## Neural Network Structure

```text
Input Layer
     ↓
Hidden Layer
     ↓
Hidden Layer
     ↓
Output Layer
```

---

## Layers Meaning

| Layer | Purpose |
|---|---|
| Input Layer | Receives input data |
| Hidden Layer | Learns patterns |
| Output Layer | Gives final prediction |

---

## Example

### Input:
- study_hours
- attendance

### Output:
- pass/fail

---

## Basic Neural Network Code

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(8, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])
```

---

## Code Explanation

### Sequential

Creates a layer-by-layer neural network.

### Dense

A fully connected neural layer.

Each neuron connects to all neurons in next layer.

### Dense(8)

Means:

- Hidden layer contains 8 neurons.

### activation='relu'

Activation function used for learning.

ReLU formula:

```math
f(x) = max(0, x)
```

If value is negative → output becomes 0.

### input_shape=(2,)

Neural network expects:

- 2 input features

Example:
- study_hours
- attendance

### Dense(1)

Output layer with:

- 1 neuron

Used for:
- binary prediction
- pass/fail
- yes/no

### activation='sigmoid'

Converts output into probability between 0 and 1.

Sigmoid formula:

```math
σ(x) = 1 / (1 + e^-x)
```

---

# 2. Weight and Bias

## Weight

### Definition

Weight means:

- importance of input

### Example

| Feature | Weight |
|---|---|
| study_hours | 10 |
| attendance | 1 |

This means:

- study_hours is more important.

---

## Bias

### Definition

Bias is:

- extra adjustment value

### Example

```text
salary = 5000x + 20000
```

| Part | Meaning |
|---|---|
| 5000 | weight |
| 20000 | bias |

---

## Neural Network Formula

```math
z = wx + b
```

Where:

| Symbol | Meaning |
|---|---|
| x | input |
| w | weight |
| b | bias |
| z | neuron output |

---

# 3. Forward Pass

## Definition

Forward Pass means:

- data moves FORWARD through neural network.

---

## Flow

```text
Input
  ↓
Hidden Layer
  ↓
Output Layer
  ↓
Prediction
```

---

## Example

Input:

- study_hours = 5
- attendance = 80

Network processes values layer-by-layer.

Final prediction:

- marks = 75

---

# 4. Backpropagation

## Definition

Backpropagation means:

- learning from mistakes

---

## Process

```text
Prediction
    ↓
Calculate Error
    ↓
Adjust Weights
    ↓
Improve Prediction
```

---

## Important Idea

Neural networks learn by repeatedly:

- predicting
- checking error
- updating weights
- updating bias

---

## Weight Update Formula

```math
w = w - α(dL/dw)
```

Where:

| Symbol | Meaning |
|---|---|
| w | weight |
| α | learning rate |
| L | loss/error |

---

# 5. CNN (Convolutional Neural Network)

## Purpose

CNN is used for:

- images
- video
- computer vision

---

## Real Applications

- Face recognition
- Self-driving cars
- Medical image diagnosis
- Instagram filters

---

## CNN Learning Flow

```text
Edges
 ↓
Shapes
 ↓
Objects
 ↓
Full Image Understanding
```

---

## CNN Architecture

```text
Image
 ↓
Convolution Layer
 ↓
Pooling Layer
 ↓
Dense Layer
 ↓
Prediction
```

---

## Convolution Layer

Detects features like:

- edges
- textures
- eyes
- shapes

---

## Pooling Layer

Reduces image size.

Keeps important information.

---

## Simple CNN Code

```python
from tensorflow.keras.layers import Conv2D

Conv2D(32, (3,3), activation='relu')
```

---

## Meaning

| Part | Meaning |
|---|---|
| 32 | number of filters |
| (3,3) | filter size |
| relu | activation function |

---

# 6. RNN (Recurrent Neural Network)

## Purpose

RNN is used for:

- text
- speech
- time series
- sequence data

---

## Why RNN?

Normal neural networks forget previous information.

RNN remembers previous inputs.

---

## Example

Sentence:

```text
I went to the bank to deposit money.
```

Meaning of:

- bank

depends on previous words.

---

## RNN Flow

```text
Word 1 → Memory
       ↓
Word 2 → Updated Memory
       ↓
Word 3 → Prediction
```

---

## Simple RNN Code

```python
from tensorflow.keras.layers import SimpleRNN
```

---

## Problem of RNN

RNN struggles with long-term memory.

This problem led to:

- LSTM

---

# 7. Transformers Architecture

## Most Important Modern AI Architecture

Transformers power:

- ChatGPT
- Gemini
- Claude
- Modern LLMs

---

## Big Idea of Transformers

Instead of reading words one-by-one:

Transformers process:

- ALL words together

---

## Core Concept = Attention

Attention means:

- focus on important words

### Example

Sentence:

```text
I love playing cricket on weekends
```

For understanding:

- playing

Transformer focuses on:

- cricket

---

## Transformer Architecture Flow

```text
Input Text
    ↓
Tokenization
    ↓
Embeddings
    ↓
Positional Encoding
    ↓
Self Attention
    ↓
Multi-Head Attention
    ↓
Feed Forward Network (MLP)
    ↓
Many Transformer Layers
    ↓
Output Probabilities
    ↓
Next Word Prediction
```

---

## Tokenization

Breaks sentence into small parts called:

- tokens

### Example

```text
"I love AI"
```

becomes:

```text
["I", "love", "AI"]
```

---

## Embeddings

Converts words into numbers/vectors.

Example:

```text
cat → [0.21, 0.88, 0.45]
```

Words with similar meanings get similar vectors.

---

## Positional Encoding

Adds word order information.

Important because:

```text
Dog bites man
```

is different from:

```text
Man bites dog
```

---

## Self Attention

Each word asks:

- Which other words are important for me?

---

## Query, Key, Value

| Term | Meaning |
|---|---|
| Query | What am I looking for? |
| Key | What information do I contain? |
| Value | Actual information |

---

## Attention Formula

```math
Attention(Q,K,V)=softmax((QK^T)/√d_k)V
```

---

## Multi-Head Attention

Multiple attention heads learn:

- grammar
- relationships
- meaning
- context

from different perspectives.

---

## MLP (Feed Forward Network)

MLP = Multi Layer Perceptron

Used to further process attention output.

---

## Transformer Blocks

Many transformer layers are stacked together.

### Early layers learn:

- grammar
- simple relationships

### Deep layers learn:

- reasoning
- context
- knowledge

---

## Output Probabilities

Transformer predicts:

- next most likely word

### Example

Input:

```text
Machine learning is
```

Predictions:

| Word | Probability |
|---|---|
| powerful | 60% |
| amazing | 20% |
| difficult | 10% |

---

## How ChatGPT Works

```text
Input Words
      ↓
Transformer predicts next word
      ↓
Add predicted word
      ↓
Repeat again
```

---

## Why Transformers Are Powerful

Transformers:

- understand context better
- train faster
- process huge text
- support parallel processing

---

# 8. Transfer Learning

## Definition

Transfer Learning means:

- using already-trained AI models for new tasks.

---

## Human Analogy

If you know:

- how to ride bicycle

learning motorcycle becomes easier.

AI works similarly.

---

## Why Transfer Learning?

Training large models from scratch:

- requires huge data
- expensive
- time consuming

Transfer learning solves this problem.

---

## Example

Using pretrained image model:

```python
from tensorflow.keras.applications import MobileNetV2
```

---

## Real Applications

- image classification
- face recognition
- medical diagnosis
- chatbot systems

---

# Important AI/ML Terms

| Term | Meaning |
|---|---|
| Neuron | Small processing unit |
| Layer | Group of neurons |
| Weight | Importance of input |
| Bias | Extra adjustment value |
| Activation Function | Decides neuron activation |
| Forward Pass | Data moving forward |
| Backpropagation | Learning from mistakes |
| CNN | Neural network for images |
| RNN | Neural network with memory |
| Transformer | Attention-based architecture |
| Transfer Learning | Reusing trained models |

---

# Final Beginner Understanding

## Deep Learning Workflow

```text
Input Data
    ↓
Forward Pass
    ↓
Prediction
    ↓
Calculate Error
    ↓
Backpropagation
    ↓
Update Weights & Biases
    ↓
Better Prediction
```

---
