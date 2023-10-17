import pandas as pd

# Load the CSV file
file_path = 'Construction_Data_PM_Forms_All_Projects.csv'

# Read the data
try:
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

# Ensure columns are available in the data
if 'Created' not in data.columns or 'Project' not in data.columns:
    print("\n'Created' or 'Project' column not found in the data.")
    exit()

# Convert 'Start Date' and 'End Date' columns to datetime format
data['Created'] = pd.to_datetime(data['Created'])
data['Status Changed'] = pd.to_datetime(data['Status Changed'])

# Calculate elapsed days for each row
data['Elapsed Days'] = (data['Status Changed'] - data['Created']).dt.days

# Calculate mean elapsed time for each category
mean_elapsed_per_category = data.groupby('Project')['Elapsed Days'].mean().reset_index()

# Display the result
print(mean_elapsed_per_category)
