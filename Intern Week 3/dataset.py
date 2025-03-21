import pandas as pd
import numpy as np

# Define the dataset columns
disease_names = [
    "Diabetes", "Hypertension", "Influenza", "Tuberculosis", "Asthma", "Malaria", "Dengue", "COVID-19",
    "Hepatitis B", "Chronic Kidney Disease", "Heart Disease", "Cancer", "Pneumonia", "HIV/AIDS",
    "Stroke", "Alzheimer's Disease", "Arthritis", "Epilepsy", "Parkinson's Disease", "Obesity",
    "Depression", "Anxiety", "Migraine", "Liver Cirrhosis", "Bronchitis", "Cholera", "Typhoid Fever",
    "Ebola", "Zika Virus", "Meningitis", "Gonorrhea", "Syphilis", "Measles", "Rubella", "Chickenpox",
    "Leprosy", "Psoriasis", "Celiac Disease", "Multiple Sclerosis", "Osteoporosis", "Sickle Cell Anemia",
    "Hemophilia", "Polio", "Rabies", "Whooping Cough", "Gastritis", "Ulcerative Colitis", "Crohn’s Disease",
    "Hepatitis C", "Thyroid Disorders", "Sepsis"
]

num_diseases = len(disease_names)

# Generate realistic data
years_high = np.random.randint(1980, 2025, size=num_diseases)
years_low = np.random.randint(1950, 2020, size=num_diseases)
cases_2010 = np.random.randint(1000, 500000, size=num_diseases)
cases_2020 = np.random.randint(1000, 500000, size=num_diseases)
cases_2024 = np.random.randint(1000, 500000, size=num_diseases)
mortality_rate = np.round(np.random.uniform(0.1, 20.0, size=num_diseases), 2)

causes = ["Genetic", "Infection", "Lifestyle", "Environmental", "Viral", "Bacterial", "Autoimmune", "Deficiency", "Unknown"]
preventions = ["Vaccination", "Regular Checkups", "Healthy Diet", "Medication", "Physical Activity",
               "Avoid Risky Behavior", "Good Hygiene", "Early Detection", "Quarantine Measures", "Use of Mosquito Nets"]

causes_data = np.random.choice(causes, num_diseases, replace=True)
preventions_data = np.random.choice(preventions, num_diseases, replace=True)

# Create DataFrame
df_diseases = pd.DataFrame({
    "Disease": disease_names,
    "Year_High_Prevalence": years_high,
    "Year_Low_Prevalence": years_low,
    "Cases_Reported_2010": cases_2010,
    "Cases_Reported_2020": cases_2020,
    "Cases_Reported_2024": cases_2024,
    "Mortality_Rate (%)": mortality_rate,
    "Common_Cause": causes_data,
    "Prevention_Method": preventions_data
})

# Save dataset to Excel
file_name = "Diseases_Dataset.xlsx"
df_diseases.to_excel(file_name, index=False)

print(f"Dataset successfully saved as {file_name}")
