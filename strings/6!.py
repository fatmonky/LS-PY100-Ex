def is_empty(str):
    if str:
        return False
    else:
        return True

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True


# model answer:
"""
A string is empty if it does not contain any characters. The easiest way is to simply check for an empty string, and nearly as easily, you can check the length of the string.

A more Pythonic approach would be to leverage the fact that an empty string is falsy. By returning the negation of the string using the not keyword, we can obtain a solution that looks like this:

def is_empty(s):
    return not s


"""
