def last(lst):
    if lst:
        return lst[-1]
    else:
        return None

#test
print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))
