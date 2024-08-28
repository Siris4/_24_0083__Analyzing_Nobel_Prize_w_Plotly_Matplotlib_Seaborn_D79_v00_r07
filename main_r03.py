import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Check for duplicate rows
duplicates = df.duplicated()

# Number of duplicates
num_duplicates = duplicates.sum()

# Print number of duplicate rows
if num_duplicates > 0:
    print(f"There are {num_duplicates} duplicate rows in the dataset.")
    # Optionally, you can drop duplicates and save the clean dataset
    df_cleaned = df.drop_duplicates()
    print("Duplicates have been removed. The cleaned dataset is now in 'df_cleaned'.")
else:
    print("No duplicate rows found in the dataset.")
