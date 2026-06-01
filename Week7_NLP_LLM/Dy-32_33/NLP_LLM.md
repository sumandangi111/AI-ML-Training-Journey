# Week 7 — NLP + LLM Foundations

## Table of Contents

1. Natural Language Processing (NLP)
2. Text Preprocessing
3. Tokenization
4. Embeddings
5. Language Modeling
6. Large Language Models (LLMs)
7. LLM Architecture
8. Transformer Architecture
9. Transfer Learning
10. Pretraining
11. Fine-Tuning
12. Prompt Engineering
13. Hallucination
14. Alignment
15. Small Language Models (SLMs)
16. LLM vs SLM
17. Local Inference
18. Model Optimization
19. Quantization
20. Pruning
21. Distillation
22. Interview Quick Revision

---

# 1. Natural Language Processing (NLP)

## Definition

Natural Language Processing (NLP) is a branch of Artificial Intelligence that enables computers to understand, process, and generate human language.

## Applications

* Chatbots
* Language Translation
* Voice Assistants
* Text Summarization
* Sentiment Analysis

## NLP Workflow

```text
Human Text
     ↓
Preprocessing
     ↓
Tokenization
     ↓
Embeddings
     ↓
Model Training
     ↓
Prediction
```

---

# 2. Text Preprocessing

## Definition

Text preprocessing is the process of cleaning and preparing text before training a model.

## Common Steps

### Lowercasing

```text
HELLO → hello
```

### Remove Punctuation

```text
Hello!!! → Hello
```

### Remove Extra Spaces

```text
Hello     AI → Hello AI
```

### Remove Stop Words

```text
I am learning AI
```

↓

```text
learning AI
```

## Purpose

* Cleaner data
* Better model performance
* Reduced noise

---

# 3. Tokenization

## Definition

Tokenization is the process of splitting text into smaller units called tokens.

## Example

```text
I love AI
```

↓

```text
["I", "love", "AI"]
```

## Purpose

Computers process tokens instead of complete sentences.

---

# 4. Embeddings

## Definition

Embeddings are numerical representations of words.

## Example

```text
Dog → [0.25, 0.78, 0.12]
Cat → [0.22, 0.80, 0.15]
```

Words with similar meanings have similar embeddings.

## Purpose

Help models understand semantic meaning.

---

# 5. Language Modeling

## Definition

A language model predicts the next word in a sequence.

## Example

Input:

```text
I love machine ______
```

Output:

```text
learning
```

## Purpose

Foundation of modern AI chatbots and text generation systems.

---

# 6. Large Language Models (LLMs)

## Definition

LLMs are AI models trained on massive amounts of text data to understand and generate human language.

## Examples

* ChatGPT
* Gemini
* Claude

## Capabilities

* Question Answering
* Text Generation
* Coding Assistance
* Translation
* Summarization

---

# 7. LLM Architecture

## Workflow

```text
Input Text
      ↓
Tokenization
      ↓
Embeddings
      ↓
Transformer Layers
      ↓
Prediction
      ↓
Output
```

## Core Technology

Most modern LLMs are based on the Transformer architecture.

---

# 8. Transformer Architecture

## Definition

A Transformer is a Deep Learning architecture that helps AI understand relationships between words using an Attention Mechanism.

## Attention Mechanism

Focuses on important words in a sentence.

### Example

```text
Rahul scored good marks because he studied hard.
```

The model understands that "he" refers to "Rahul".

## Self-Attention

Every word looks at every other word to understand context.

## Advantages

* Understands long sentences
* Faster training
* Better accuracy
* Foundation of modern AI

## Interview Definition

A Transformer is a Deep Learning architecture that uses Attention Mechanisms to understand relationships between words and context.

---

# 9. Transfer Learning

## Definition

Transfer Learning means using a pre-trained model and adapting it for a new task.

## Example

A model trained on millions of images can be fine-tuned to identify cats and dogs.

## Benefits

* Less training time
* Less data required
* Better performance

## Interview Definition

Transfer Learning is the process of reusing knowledge from a pre-trained model for a new task.

---

# 10. Pretraining

## Definition

Pretraining is the first stage where an AI model learns from massive datasets.

## Data Sources

* Books
* Articles
* Websites
* Research Papers

## Purpose

Learn:

* Grammar
* Vocabulary
* Language Patterns
* General Knowledge

---

# 11. Fine-Tuning

## Definition

Fine-tuning is the process of adapting a pretrained model for a specific task.

## Example

```text
Pretrained Model
       ↓
Medical Dataset
       ↓
Medical Chatbot
```

## Purpose

Improve performance in a specific domain.

---

# 12. Prompt Engineering

## Definition

Prompt Engineering is the art of writing effective instructions to get better AI responses.

## Example

### Weak Prompt

```text
Explain AI
```

### Better Prompt

```text
Explain AI in simple language with examples for beginners.
```

## Purpose

Produce more accurate and useful outputs.

---

# 13. Hallucination

## Definition

Hallucination occurs when an AI model generates incorrect or fabricated information confidently.

## Example

The model provides a fake fact that sounds correct.

## Cause

The model predicts likely text patterns instead of verifying facts.

---

# 14. Alignment

## Definition

Alignment ensures AI behaves according to human values, goals, and safety requirements.

## Goals

* Safe
* Helpful
* Honest
* Responsible

---

# 15. Small Language Models (SLMs)

## Definition

SLMs are smaller versions of Large Language Models.

## Characteristics

* Lower memory usage
* Faster execution
* Lower cost
* Can run on local devices

## Limitations

* Less knowledge
* Lower reasoning capability

---

# 16. LLM vs SLM

| Feature              | LLM    | SLM    |
| -------------------- | ------ | ------ |
| Size                 | Large  | Small  |
| Memory Usage         | High   | Low    |
| Cost                 | High   | Low    |
| Accuracy             | Higher | Lower  |
| Speed                | Slower | Faster |
| Hardware Requirement | High   | Low    |

---

# 17. Local Inference

## Definition

Local Inference means running an AI model directly on a local device instead of a cloud server.

## Examples

* Laptop
* Smartphone
* Edge Device

## Advantages

* Better Privacy
* Offline Usage
* Faster Response
* Full Control

## Interview Definition

Local Inference is the process of running a trained AI model on a local device to generate predictions or responses.

---

# 18. Model Optimization

## Definition

Model Optimization means improving a model's efficiency, speed, and performance.

## Goals

* Faster Inference
* Lower Memory Usage
* Smaller Models
* Better Performance

---

# 19. Quantization

## Definition

Reducing the numerical precision of model weights.

## Example

```text
32-bit → 16-bit → 8-bit
```

## Benefits

* Smaller models
* Faster inference
* Reduced memory usage

---

# 20. Pruning

## Definition

Removing unnecessary neurons or connections from a model.

## Example

```text
Large Model
     ↓
Remove Unused Parts
     ↓
Smaller Model
```

## Benefits

* Faster execution
* Smaller size

---

# 21. Distillation

## Definition

Knowledge Distillation transfers knowledge from a large model (Teacher) to a smaller model (Student).

## Workflow

```text
Teacher Model
       ↓
Knowledge Transfer
       ↓
Student Model
```

## Benefits

* Smaller model
* Faster inference
* Similar performance

---

# 22. Interview Quick Revision

## What is NLP?

NLP helps computers understand and generate human language.

## What is Tokenization?

Breaking text into smaller units called tokens.

## What are Embeddings?

Numerical representations of words.

## What is a Language Model?

A model that predicts the next word in a sequence.

## What is an LLM?

A large AI model trained on huge amounts of text data.

## What is a Transformer?

A Deep Learning architecture that uses Attention Mechanisms to understand context and relationships between words.

## What is Transfer Learning?

Using a pretrained model for a new task.

## What is Fine-Tuning?

Training a pretrained model on a specific dataset.

## What is Prompt Engineering?

Designing effective prompts to get better outputs.

## What is Hallucination?

When AI generates incorrect information confidently.

## What is Alignment?

Making AI safe, helpful, and aligned with human values.

## What is Local Inference?

Running AI models directly on local devices.

## What is Model Optimization?

Making models faster, smaller, and more efficient.

## What is Quantization?

Reducing numerical precision to improve efficiency.

## What is Pruning?

Removing unnecessary model components.

## What is Distillation?

Transferring knowledge from a large model to a smaller model.

---

# Memory Trick

```text
NLP
 ↓
Preprocessing
 ↓
Tokenization
 ↓
Embeddings
 ↓
Language Modeling
 ↓
Transformer
 ↓
LLM
 ↓
Pretraining
 ↓
Fine-Tuning
 ↓
Prompt Engineering
 ↓
Hallucination
 ↓
Alignment
 ↓
SLM
 ↓
Local Inference
 ↓
Optimization
```

**Remember:**

Transformer = Attention + Context Understanding

Transfer Learning = Reuse Knowledge

Optimization = Faster + Smaller + Better
