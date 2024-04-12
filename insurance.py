import csv

patients = {}
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []
with open("insurance.csv", 'r') as csvfile:
    insurance_data = csv.reader(csvfile)
    # Rows: age, sex, bmi, children, smoker, region, charges
    for row in insurance_data:
        age.append(row[0])
        sex.append(row[1])
        bmi.append(row[2])
        children.append(row[3])
        smoker.append(row[4])
        region.append(row[5])
        charges.append(row[6])

total_entries = len(age[1:])
for i in range(1, total_entries):
    patients[i] = {'Age': age[i],
                   'Sex': sex[i],
                   'BMI': bmi[i],
                   'Children': children[i],
                   'Smoker': smoker[i],
                   'Region': region[i],
                   'Charges': charges[i]}

print(patients)
