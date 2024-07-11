def first(any_list):
    if any_list != []:
        return any_list[0]
    else:
        print("Empty list: please key in a non-empty list!")
        return None

#test
print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))  # Please key in a non-empty list!

"""
# model answer uses truthiness 
def first(lst):
    if lst:
        return lst[0]
    else:
       return None
"""
