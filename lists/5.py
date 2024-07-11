def countif100plus(lst):
    tracker = 0
    for element in lst:
        if element >= 100:
            tracker += 1
    return tracker

# test
scores = [96, 47, 113, 89, 100, 102]
print(countif100plus(scores))
