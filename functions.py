# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))

'''
Calling show_plus_ten...
15
Done calling
This function returned: None

Calling add_ten...
Done calling
This function returned: 15
'''
================================================================================
# write your function here
def readable_timedelta(days):
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

# test your function
print(readable_timedelta(10))


'''
expected result: 10, actual result: 10.0
expected result: 7123.6902801..., actual result: 7123.690280065897
'''

================================================================================
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]
def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))

print(averages)

'''
[57.0, 58.2, 50.6, 27.2]
'''
================================================================================
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(city):
    return len(city) < 10

short_cities = list(filter(is_short, cities))

print(short_cities)

'''
['Chicago', 'Denver', 'Boston']
'''

================================================================================
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda city: len(city) < 10, cities))
print(short_cities)

'''
['Chicago', 'Denver', 'Boston']
'''

===============================================================================

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

'''
Lesson 1: Why Python Programming
Lesson 2: Data Types and Operators
Lesson 3: Control Flow
Lesson 4: Functions
Lesson 5: Scripting
'''

================================================================================
def chunker(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))

'''
[0, 1, 2, 3]
[4, 5, 6, 7]
[8, 9, 10, 11]
[12, 13, 14, 15]
[16, 17, 18, 19]
[20, 21, 22, 23]
[24]
'''

================================================================================
