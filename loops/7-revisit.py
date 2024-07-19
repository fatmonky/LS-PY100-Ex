cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

# Write a for loop that iterates over the elements of the list cities and prints the length of each string. If the element is None, use the continue statement to skip forward to the next iteration without printing anything.

# my answer 19 Jul 24 148pm

for city in cities:
    if city == None:
        continue
    else:
        print(city ) #error: didn't read question properly. it's length of string

# model answer:
cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city is None:
        continue

    print(len(city))
