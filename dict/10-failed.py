numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

#my answeR: failed!
"""
for pairs in numbers.items():
    for key, value in pairs:
        print(f"A {key} number is {value}.")
"""
# model answer:
for key, value in numbers.items():
    print(f"A {key} number is {value}.")
