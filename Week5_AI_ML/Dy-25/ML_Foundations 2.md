# Supervised Learning Notes

---

# 1. Supervised Learning

Supervised Learning is a type of Machine Learning where the model learns using **labeled data**.

- **Input (X)** → Independent Variable / Features
- **Output (Y)** → Dependent Variable / Target

The model learns the relationship between X and Y.

## Example

| Input (X) | Output (Y) |
|---|---|
| House Size | House Price |
| Study Hours | Exam Marks |
| Temperature | Ice Cream Sales |

---

# 2. Types of Supervised Learning

Supervised Learning is mainly divided into:

1. Classification
2. Regression

---

# 3. Classification

Classification is used when the output belongs to a **category or class**.

## Examples

- Spam or Not Spam
- Cat or Dog
- Pass or Fail

---

## Types of Classification

### A. Binary Classification

Only two classes are present.

## Examples

- Yes / No
- True / False
- Spam / Not Spam

---

### B. Multi-Class Classification

More than two classes.

## Examples

- Red, Blue, Green
- Apple, Banana, Mango

---

### C. Multi-Label Classification

One data point can belong to multiple labels at the same time.

## Example

A movie can be:
- Action
- Comedy
- Thriller

simultaneously.

---

# 4. Regression

Regression is used when the output is a **continuous numerical value**.

## Examples

- House Price Prediction
- Temperature Prediction
- Salary Prediction

---

# 5. Linear Regression

Linear Regression is used to predict numerical values using a straight-line relationship.

## Formula

y = mx + b

Where:

- y = Predicted value
- x = Input feature
- m = Slope
- b = Intercept

## Example

Predicting house prices based on house size.

---

# 6. Logistic Regression

Logistic Regression is used for **classification problems**.

## Examples

- Spam Detection
- Disease Prediction
- Pass or Fail

It predicts probability values between 0 and 1.

## Sigmoid Function

σ(z) = 1 / (1 + e^(-z))

### Output Interpretation

- Output > 0.5 → Class 1
- Output < 0.5 → Class 0

---

# 7. Difference Between Linear Regression and Logistic Regression

| Linear Regression | Logistic Regression |
|---|---|
| Used for Regression | Used for Classification |
| Predicts numerical values | Predicts categories |
| Output can be any number | Output between 0 and 1 |
| Example: House Price | Example: Spam Detection |

---

# 8. Train-Test Split

Dataset is divided into two parts:

## Training Data

Used to train the model.

## Testing Data

Used to test model performance.

---

## Common Split Ratios

- 70% Training + 30% Testing
- 80% Training + 20% Testing

---

# 9. Independent and Dependent Variables

## Independent Variable (X)

Input or feature used for prediction.

## Dependent Variable (Y)

Target/output that depends on X.

---

# 10. Decision Tree

Decision Tree is a Machine Learning algorithm used for both:

- Classification
- Regression

It works in a tree-like hierarchical structure.

---

## Structure of Decision Tree

### Root Node

Starting node of the tree.

### Internal Node

Represents conditions or decisions.

### Leaf Node

Final output/result.

---

## Example Structure

```text
                Root Node
                    |
             Stream = ?
              /         \
         Science      Commerce
         /      \          \
      BCA      Engg       BCom

 ---

