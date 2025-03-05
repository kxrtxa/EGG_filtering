import os
import pandas as pd

# Folder where all 30 files are stored
folder_path = "C:\\Users\\91944\\Desktop\\gitti"  

# List to store each column
columns = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):  # Adjust if files are .xlsx or other formats
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)  # Read the file
        columns.append(df.iloc[:, 0])  # Extract the first column

# Combine all columns side by side
final_df = pd.concat(columns, axis=1)

# Save to a new file
final_df.to_csv("combined_columns.csv", index=False)
print("File saved as combined_columns.csv")
