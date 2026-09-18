import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# --------------------------------------------------
# 1. LOAD DATASET
# --------------------------------------------------

data = pd.read_csv("credit_card_fraud_synthetic_dataset.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)


# --------------------------------------------------
# 2. SEPARATE FEATURES AND TARGET
# --------------------------------------------------

X = data.drop("Class", axis=1)
y = data["Class"]

print("\nFeatures:", X.shape)
print("Target:", y.shape)


# --------------------------------------------------
# 3. SPLIT DATASET
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)


# --------------------------------------------------
# 4. CREATE RANDOM FOREST MODEL
# --------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# --------------------------------------------------
# 5. TRAIN MODEL
# --------------------------------------------------

print("\nTraining model...")

model.fit(X_train, y_train)

print("Model training completed!")


# --------------------------------------------------
# 6. MAKE PREDICTIONS
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 7. EVALUATE MODEL
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\n-----------------------------")
print("MODEL RESULTS")
print("-----------------------------")

print("Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# --------------------------------------------------
# 8. SAVE MODEL
# --------------------------------------------------

with open("fraud_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")
print("File created: fraud_model.pkl")


# --------------------------------------------------
# 9. TEST SAVED MODEL
# --------------------------------------------------

with open("fraud_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

sample = X_test.iloc[[0]]

prediction = loaded_model.predict(sample)

print("\nSample Prediction:")

if prediction[0] == 1:
    print("Fraudulent Transaction")
else:
    print("Genuine Transaction")