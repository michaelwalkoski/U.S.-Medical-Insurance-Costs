import pandas as pd

file_path = 'insurance.csv'
df = pd.read_csv(file_path)

under_30 = df[df.age < 30]
over_60 = df[df.age > 60]
average_age = df['age'].mean()

print(under_30)
print(over_60)
print(average_age)
