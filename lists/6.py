vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

# Expected printout
# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...

for lst in vocabulary:
    for word in lst:
        print(word)
