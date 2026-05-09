# ============================================================
# MEDCARE - AI DISEASE PREDICTION SYSTEM
# File: generate_dataset.py
# Description: Generates a synthetic medical dataset of 6,000
#              patient records with symptoms and disease labels.
#              Saves the result to disease_dataset.csv
# Queens Hospital Akure - AI Engineering Team
# ============================================================

import csv
import random

# --- Sample Space ---
# Total patients: 6,000
total_patients = 6000

# --- Possible Values ---
genders   = ["Male", "Female"]
yes_no    = ["Yes", "No"]


# ============================================================
# HELPER FUNCTION - Assign Disease Based on Symptoms
# This encodes real medical logic into the dataset
# ============================================================

def get_disease(age, gender, fever, cough, headache, body_pain):
    """
    Assigns a disease label based on patient symptoms.
    Logic is based on common symptom patterns for each disease.

    Malaria   - Fever + Headache + Body Pain (common in all ages)
    Typhoid   - Fever + Headache + Body Pain (older patients, no cough)
    Flu       - Fever + Cough + Body Pain
    Cold      - Cough + No Fever or mild symptoms
    """

    if fever == "Yes" and headache == "Yes" and body_pain == "Yes" and cough == "No":
        if age >= 15:
            return "Typhoid"
        else:
            return "Malaria"

    elif fever == "Yes" and headache == "Yes" and body_pain == "Yes" and cough == "Yes":
        return "Malaria"

    elif fever == "Yes" and cough == "Yes" and body_pain == "Yes" and headache == "No":
        return "Flu"

    elif fever == "Yes" and cough == "Yes" and headache == "No" and body_pain == "No":
        return "Flu"

    elif cough == "Yes" and fever == "No":
        return "Common Cold"

    elif fever == "No" and headache == "Yes" and body_pain == "No":
        return "Common Cold"

    elif fever == "Yes" and body_pain == "No" and cough == "No" and headache == "No":
        return "Malaria"

    else:
        # Default for any remaining combination
        return random.choice(["Malaria", "Flu", "Typhoid", "Common Cold"])


# ============================================================
# GENERATE DATASET
# ============================================================

patients = []

for _ in range(total_patients):
    age        = random.randint(1, 90)
    gender     = random.choice(genders)
    fever      = random.choice(yes_no)
    cough      = random.choice(yes_no)
    headache   = random.choice(yes_no)
    body_pain  = random.choice(yes_no)
    disease    = get_disease(age, gender, fever, cough, headache, body_pain)

    patients.append([age, gender, fever, cough, headache, body_pain, disease])

# Shuffle to mix all records randomly
random.shuffle(patients)


# ============================================================
# SAVE TO CSV
# ============================================================

with open("disease_dataset.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Age", "Gender", "Fever", "Cough", "Headache", "Body_Pain", "Disease"])
    writer.writerows(patients)

print("Dataset created successfully!")
print(f"Total records : {len(patients)}")
print("File saved as : disease_dataset.csv")
