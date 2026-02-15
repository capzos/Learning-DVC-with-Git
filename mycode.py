import pandas as pd
import os


# create sample data with column names

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Raj'],
    'Age': [25, 30, 35, 40, 21],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Mumbai']
}


df = pd.DataFrame(data)


# add new row
new_row = {'Name': 'Eve', 'Age': 28, 'City': 'San Francisco'}
df.loc[len(df)] = new_row

# ensure the directory exists
output_dir = 'data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# save the DataFrame to a CSV file
output_path = os.path.join(output_dir, 'sample_data.csv')
df.to_csv(output_path, index=False)

print(f"DataFrame saved to {output_path}")

