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
