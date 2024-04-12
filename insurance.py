import csv

patients = {}  # Dictionary of all patient data
count = 0  # Counter to track row index
with open("insurance.csv", 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    count += 1
    patients[count] = row

total_patients = len(patients)

def get_sum(column):
    sum = 0
    for patient in patients:
        row_data = float(patients[patient][column])
        sum += row_data
    return sum

print('There are {} patient records'.format(total_patients))

average_age = round(get_sum("age") / total_patients)
print('The average patient age is: {}'.format(average_age))

average_charges = round(get_sum("charges") / total_patients, 2)
print('The average charges are: ${}'.format(average_charges))
