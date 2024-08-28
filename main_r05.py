import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Convert the 'birth_date' column to datetime objects
df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')

# Verify the conversion
print(df['birth_date'].head())
