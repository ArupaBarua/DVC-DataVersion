import pandas as pd
import os

data = {'Name': ['Alice', 'Bob', 'Jack', 'Jill'],
        'Age': [23, 24, 25, 28],
        'City': ['New York', 'Chicago', 'Washington', 'Maryland']}

df = pd.DataFrame(data)

new_row = {'Name': 'Kate', 'Age': '29', 'City': 'New Jersey'}
df.loc[len(df.index)] = new_row

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=False)
print(f"csv file saved to {file_path}")