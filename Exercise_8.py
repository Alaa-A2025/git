import pandas as pd

patients = pd.DataFrame({ 
    "patient_id": ["P01", "P02", "P03", "P04"], 
    "age": [34, 52, 47, 61], 
    "sex": ["F", "M", "F", "M"] })

labs = pd.DataFrame({ 
    "patient_id": ["P01", "P02", "P03", "P04"], 
    "hemoglobin": [13.4, 14.8, 12.9, 13.7],
    "crp": [1.2, 4.5, 2.1, 8.3] 
})
