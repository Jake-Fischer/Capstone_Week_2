#List of data
classes_registered = ['ITEC 1150', 'ITEC 1300', 'ENGL 1340', 'Math 1100']

#Make a list of only ITEC classes unsing list comprehention 
only_itec = [c for c in classes_registered if c.startswith('ITEC')]
print(only_itec)

#Record temp everyday
high_temps = [-1, 78, 78, 56, 34, -1, 23, 43, -1, 89, -1]

#Make a list of only numbers that represent a valid temp
only_real_measurements = [temp for temp in high_temps if temp != -1]
print(only_real_measurements)

temp_celsius= [ temp_f - 32 * 5 / 9 for temp_f in only_real_measurements]
print(temp_celsius)

average = sum(temp_celsius) / len(temp_celsius)
print(f'The average is {average:.1f}')

numbers = [2,4,6]
plus_one = [n+1 for n in numbers]
print(plus_one)

numbers = [0, 2, 0, 3, 4, 0 ]
numbers_no_zeros = [n for n in numbers if n != 0]

numbers_doubled_no_zeros = [n * 2 for n in numbers if n !=0 ]
print(numbers_doubled_no_zeros)