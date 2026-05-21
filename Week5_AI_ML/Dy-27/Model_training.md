# AI/ML Training Notes

---

# 1. Model Training

Model training is the process of teaching a machine learning model using data.

During training:
- The model learns patterns from data.
- It improves predictions step by step.
- The goal is to reduce errors and increase accuracy.

---

# 2. Data Split

Before training, data is divided into different parts:

| Dataset | Purpose |
|---|---|
| Train Data | Used to train the model |
| Validation Data | Used to tune the model |
| Test Data | Used to check final performance |

This process helps evaluate whether the model performs well on new unseen data.

---

# 3. Loss Function

A **Loss Function** measures how wrong the model predictions are.

- Higher loss = poor predictions
- Lower loss = better predictions

The main goal during training is to reduce the loss.

Example:
If the model predicts incorrect outputs, the loss value increases.

---

# 4. Backpropagation

Backpropagation is a method used to improve the model.

Steps:
1. Model makes predictions
2. Loss is calculated
3. Error is sent backward through the network
4. Weights are updated to reduce error

This helps the model learn from mistakes.

---

# 5. Weights

Weights are important values inside a neural network.

- They control the importance of input features.
- During training, weights keep changing.
- Better weights lead to better predictions.

---

# 6. Epochs

An **Epoch** means the model has seen the complete training dataset one time.

Example:
- 1 Epoch = entire dataset processed once
- 10 Epochs = dataset processed 10 times

More epochs usually improve learning, but too many can cause overfitting.

---

# 7. Batch Size

Batch Size is the amount of data processed at one time before updating the model.

Example:
If batch size = 32,
the model processes 32 samples together.

Small batch size:
- Slower training
- Less memory needed

Large batch size:
- Faster training
- More memory needed

---

# 8. Learning Rate

Learning Rate controls how much the model updates weights during training.

- Small learning rate → slow learning
- Large learning rate → unstable learning

Choosing the correct learning rate is very important.

---

# 9. Training in AI

Training means teaching the AI model using data so it can learn patterns and make predictions.

Example:
- Chatbots learn language patterns
- Image models learn visual patterns

---

# 10. Inference

Inference means using a trained model to make predictions on new data.

Example:
- Using ChatGPT after training
- Image classification after model training

Training = Learning  
Inference = Using learned knowledge

---

# 11. GPU

GPU stands for **Graphics Processing Unit**.

GPUs are used in AI because they can process many calculations in parallel.

Benefits:
- Faster training
- Handles large models
- Useful for Deep Learning

Popular AI GPUs:
- NVIDIA GPUs
- Google TPU
- AMD GPUs

---

# 12. Why GPUs are Important in AI

AI models require huge mathematical computations.

GPUs help by:
- Speeding up matrix calculations
- Training large neural networks faster
- Handling massive datasets efficiently

Without GPUs, training modern AI models would take much longer.

---

# 13. Data Augmentation

Data Augmentation means creating modified versions of existing data to increase dataset size.

Examples:
- Rotating images
- Flipping images
- Cropping images
- Changing brightness

Benefits:
- Prevents overfitting
- Improves accuracy
- Helps models generalize better

Mostly used in Computer Vision tasks.

---

# 14. Fine-Tuning

Fine-Tuning means taking a pre-trained model and training it on custom data.

Formula:

Pre-trained Model + New Data = Fine-Tuned Model

Benefits:
- Saves time
- Requires less data
- Improves task-specific performance

Example:
Using an existing language model and training it for medical chatbot tasks.

---

# 15. Pre-Trained Model

A Pre-Trained Model is already trained on large datasets.

Instead of training from scratch, we reuse the model.

Advantages:
- Faster development
- Lower computational cost
- Better performance with smaller datasets

Examples:
- BERT
- GPT
- ResNet

---

# 16. RLHF

RLHF stands for:

**Reinforcement Learning from Human Feedback**

In RLHF:
- Humans give feedback to AI responses
- AI learns which responses are better
- The model improves based on human preferences

Used in:
- Chatbots
- Large Language Models (LLMs)

---

# 17. CNN

CNN stands for:

**Convolutional Neural Network**

CNNs are mainly used for image-related tasks.

Applications:
- Image classification
- Face detection
- Medical image analysis

CNNs automatically detect important image features.

---

# 18. LLM

LLM stands for:

**Large Language Model**

LLMs are AI models trained on huge amounts of text data.

Capabilities:
- Text generation
- Translation
- Question answering
- Coding assistance

Examples:
- GPT
- Gemini
- Llama

---

# 19. Model Training Time

Training time depends on:
- Dataset size
- Model complexity
- GPU power
- Batch size

Approximate examples:

| Model Type | Training Time |
|---|---|
| Small Model | 30–40 minutes |
| CNN Model | Hours to Days |
| Large LLM | Weeks to Months |

---

# 20. Common Reasons Why Models Fail

## 1. Small Dataset
Not enough data for learning.

## 2. Bad Data Quality
Incorrect, noisy, or missing data reduces accuracy.

## 3. Poor Labeling
Wrong or missing labels confuse the model.

## 4. Overfitting
Model memorizes training data instead of learning patterns.

## 5. Underfitting
Model fails to learn enough from data.

---

# 21. Important AI Terms Summary

| Term | Meaning |
|---|---|
| Loss | Error made by model |
| Epoch | One full pass through dataset |
| Batch Size | Number of samples processed together |
| Learning Rate | Speed of learning |
| GPU | Hardware for faster AI training |
| CNN | Neural network for images |
| LLM | Large language model |
| RLHF | Learning from human feedback |
| Fine-Tuning | Custom training on existing model |

---

# Quick Revision

- Training teaches the model.
- Loss measures errors.
- Backpropagation improves weights.
- Epochs repeat learning cycles.
- GPUs speed up AI training.
- Fine-tuning customizes pre-trained models.
- CNNs work best for images.
- LLMs work with language and text.

---