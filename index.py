python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "Distribution_of_Active_Members_2022.xlsx"
data = pd.read_excel(file_path)

# Data preprocessing
data['Quarter'] = data['Quarter'].astype('category')
data['Age Group'] = data['Age Group'].astype('category')
data['Employment Sector'] = data['Employment Sector'].astype('category')

# Plotting active member trends by quarter
plt.figure(figsize=(10, 6))
sns.barplot(x='Quarter', y='Active Members', hue='Employment Sector', data=data)
plt.title('Active Members by Quarter and Employment Sector in 2022')
plt.xlabel('Quarter')
plt.ylabel('Number of Active Members')
plt.legend(title='Employment Sector')
plt.show()

# Filtering and analyzing data
def filter_and_analyze(data, age_group=None, sector=None):
    filtered_data = data
    if age_group:
        filtered_data = filtered_data[filtered_data['Age Group'] == age_group]
    if sector:
        filtered_data = filtered_data[filtered_data['Employment Sector'] == sector]
    return filtered_data

# Example usage
age_group = '25-34'
sector = 'Private'
filtered = filter_and_analyze(data, age_group=age_group, sector=sector)
print(filtered)
