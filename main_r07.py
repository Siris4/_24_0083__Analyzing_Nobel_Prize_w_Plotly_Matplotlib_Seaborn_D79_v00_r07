import pandas as pd
import plotly.graph_objects as go

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Count the number of prizes awarded to men and women
gender_counts = df['sex'].value_counts()

# Calculate the percentage of prizes awarded to women
total_prizes = gender_counts.sum()
women_prizes = gender_counts.get('Female', 0)  # 'Female' is the label used for women in the 'sex' column
women_percentage = (women_prizes / total_prizes) * 100

# Create a donut chart
fig = go.Figure(data=[go.Pie(labels=gender_counts.index,
                             values=gender_counts.values,
                             hole=0.4)])  # hole creates the donut shape

# Update the layout to include the percentage of prizes to women in the title
fig.update_layout(title_text=f"Nobel Prizes Distribution by Gender (Women: {women_percentage:.2f}%)")

# Show the figure
fig.show()
