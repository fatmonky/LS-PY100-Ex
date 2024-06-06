def starts_with(string, subst):
    return True if subst in string else False

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

# model answer: use str.startswith 

