def is_empty_or_blank(str):
    if (str == '  ' or str == '  '):
        return True
    elif str == '':
        return True
    else:
        return False

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# real answer:
# use str.strip()
"""
def is_empty_or_blank(s):
    return not s.strip(' ')
"""
