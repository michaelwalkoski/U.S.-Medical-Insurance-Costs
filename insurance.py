import csv

patients = {}  # Dictionary of all patient data
count = 0  # Counter to track row index
with open('insurance.csv', 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    count += 1
    patients[count] = row

total_patients = len(patients)

def get_sum(column): # Sum all numeric entries
    sum = 0
    for patient in patients:
        row_data = float(patients[patient][column])
        sum += row_data
    return sum

def get_values(column, str): # Sum all string entries
    sum = 0
    for patient in patients:
        if patients[patient][column] == str:
            sum += 1
    return sum

print('There are {} patient records'.format(total_patients))
total_males = get_values('sex', 'male') # Total number of male patients
print('There are {} males and {} females.'.format(total_males, (total_patients - total_males)))

average_age = round(get_sum('age') / total_patients)
print('The average patient age is: {}'.format(average_age))

total_northwest = get_values('region', 'northwest')
total_southwest = get_values('region', 'southwest')
total_northeast = get_values('region', 'northeast')
total_southeast = get_values('region', 'southeast')
print('\nThe regional breakdown is\nNorthwest: {}\n''Southwest: {}\nNortheast: {}\nSoutheast: {}\n'.format(total_northwest, total_southwest, total_northeast, total_southeast))

average_charges = round(get_sum('charges') / total_patients, 2)
print('The average charges are: ${}'.format(average_charges))
