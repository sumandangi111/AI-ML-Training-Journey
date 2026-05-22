import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    ConfusionMatrixDisplay,
    RocCurveDisplay,
)
 
# 1. Generate data and split into Train (80%) and Test (20%) sets
X, y = make_blobs(n_samples=200, centers=2, random_state=42, cluster_std=1.5)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# 2. Train the model
model = LogisticRegression()
model.fit(X_train, y_train)
 
# 3. Make predictions on the test data
y_pred = model.predict(X_test)
 
# 4. Print text-based performance metrics
print("--- Text Evaluation Metrics ---")
print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.2%}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))
 
# 5. Create visual plots (Confusion Matrix & ROC Curve side-by-side)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
 
# Plot 1: Confusion Matrix
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, cmap='Blues', ax=ax[0])
ax[0].set_title("Confusion Matrix")
 
# Plot 2: ROC Curve
RocCurveDisplay.from_estimator(model, X_test, y_test, ax=ax[1])
ax[1].set_title("ROC Curve")
ax[1].grid(True)
 
plt.tight_layout()
plt.show()