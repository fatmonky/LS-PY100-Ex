numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
half_numbers = []
for number in numbers.values():
    value = int(number / 2) # model answer uses number // 2
    half_numbers.append(value)

print(half_numbers)
