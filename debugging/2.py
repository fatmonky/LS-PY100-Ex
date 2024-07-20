#Our predict_weather function should output a message indicating whether a sunny or cloudy day lies ahead. However, the output is the same every time the function is invoked. Why? Fix the code so that it behaves as expected.
'''
import random

def predict_weather():
    sunshine = random.choice(['True', 'False'])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")
'''
# tweaked code
# my answer: the initial code has 'True' and 'False' in line 6.
# these aren't Booleans by strings, so sunshine is always non-empty, and thus truthy.
# by changing the values to True and False, that solves the problem, validating the hypothesis above. 

import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()

