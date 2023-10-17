import pandas as pd

# Load the CSV file
# Assume the file name is 'data.csv' and it's located in the same folder as your script
file_path = 'Construction_Data_PM_Tasks_All_Projects.csv'

# Read the data
data = pd.read_csv(file_path)

# Define the filtering criteria
# For instance, we'll filter rows where the column 'ColumnName' is equal to 'DesiredValue'
desired_value = True
filtered_data = data[data['OverDue'] == desired_value]

# Display the filtered data
print(filtered_data.head())
print(data.columns)
print(data['OverDue'].unique())
print(data.dtypes)


