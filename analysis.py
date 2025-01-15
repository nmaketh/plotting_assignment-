# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\HP\OneDrive\Desktop\transport_analysis\fuel_econ.csv"
data = pd.read_csv(file_path)

# Display a preview of the data
print("Preview of the data:")
print(data.head(10))

# Check for numerical columns
print("\nColumns in the dataset:")
print(data.columns)

# Histogram for combined fuel efficiency (comb08)
plt.figure(figsize=(10, 6))
plt.hist(data['comb'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of Combined Fuel Efficiency (mpg)')
plt.xlabel('Combined Fuel Efficiency (mpg)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('hist_comb08.png')  # Save the plot as PNG
plt.show()

# Correlation heatmap for numerical columns
numerical_cols = ['cylinders', 'city', 'UCity', 'highway', 'UHighway', 'comb08', 'UComb', 'displ']
correlation_matrix = data[numerical_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap of Numerical Features')
plt.tight_layout()
plt.savefig('heatmap.png')  # Save the plot as PNG
plt.show()

# Interpretation of the diagrams
"""
Interpretations:
1. Histogram:
   - The histogram shows the distribution of combined fuel efficiency (comb08) across vehicles.
   - Peaks indicate ranges where most vehicles fall in terms of fuel efficiency.
   - This can help identify typical fuel efficiency for vehicles in the dataset.

2. Heatmap:
   - The heatmap displays correlations between numerical features.
   - Strong correlations (close to 1 or -1) are highlighted.
   - For example, 'UCity' and 'UComb' might show a strong positive correlation because both represent adjusted mpg values.
"""
