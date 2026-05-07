import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# --- Load the dataset ---
user_data = pd.read_csv("ai_doctor_users.csv")
print("=== Dataset Preview ===")
print(user_data.head())

# --- Encode the data ---
le_gender    = LabelEncoder()
le_age_group = LabelEncoder()
le_diet      = LabelEncoder()

user_data["Gender"]    = le_gender.fit_transform(user_data["Gender"])
user_data["Age_Group"] = le_age_group.fit_transform(user_data["Age_Group"])
user_data["Diet"]      = le_diet.fit_transform(user_data["Diet"])

# --- Set input and output ---
X = user_data[["Age", "Gender", "Age_Group"]]
y = user_data["Diet"]

# --- Train and test split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Train the model ---
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print("\n=== Model Trained Successfully ===")

# --- Evaluate the model ---
y_pred   = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {round(accuracy * 100, 2)}%")

# --- Make a sample prediction ---
sample_gender    = le_gender.transform(["Female"])[0]
sample_age_group = le_age_group.transform(["Adult"])[0]
sample_input     = [[35, sample_gender, sample_age_group]]
prediction       = model.predict(sample_input)
recommended_diet = le_diet.inverse_transform(prediction)[0]

print(f"\nSample Prediction:")
print(f"Input  -> Age: 35, Gender: Female, Age Group: Adult")
print(f"Output -> Recommended Diet: {recommended_diet}")