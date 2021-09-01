# TUPLES
city_state = [ ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA') ]
print(len(city_state))

first_city_state = city_state[0]
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1])

#Unpacking a tuple
city, state = first_city_state
print(city, state)

#Returning data from functions

def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km

distances = get_distance()
print(distances[0])

miles, km = get_distance()
print(km)

#Sets

cats = set() #Empty set created
cats.add('Lion')
cats.add('Tiger')
cats.add('Gibby')
print(cats)

birds = { 'owl', 'robin', 'swan'}
print(birds)

birds.add('robin') # Will not add duplicates to the set

birds.remove('owl')

for bird in birds: # Itterate over set
    print(bird)

# Convert a list to a set, then back to a list to get rid of duplicates. Does not keep order
bird_list = [ 'owl', 'robin', 'swan', 'owl', 'robin', 'swan']
bird_list_no_duplicates = list(set(bird_list))
print(bird_list_no_duplicates)

try:
    print(bird_list[9])
except:
    print('Opps, that does not exist.')