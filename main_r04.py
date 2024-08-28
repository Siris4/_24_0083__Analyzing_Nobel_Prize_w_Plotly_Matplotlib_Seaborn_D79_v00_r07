import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Check for NaN values
nan_values = df.isna().sum()

# Print the count of NaN values for each column
print("NaN values in each column:")
print(nan_values)

# Check if there are any NaN values in the entire dataset
total_nan = nan_values.sum()

if total_nan > 0:
    print(f"\nThere are {total_nan} missing values in the dataset.")
else:
    print("\nThere are no missing values in the dataset.")
