# 20 Jul 24

'''
You come across the following code. What errors does it raise for the given examples and what exactly do the error messages mean?
'''

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

#find_first_nonzero_among(0, 0, 1, 0, 2, 0)
# my tweak
find_first_nonzero_among([0, 0, 1, 0, 2, 0])
#find_first_nonzero_among(1)
# my tweak
find_first_nonzero_among([1])



# my answer before running:
# first line throws an error, because n is == 0, but the function doesn't define what to do when this happens. 
# second line doesn't return an error, because the function defines a return value when n != 0, which n isn't. 

# my answer after running:
#1. the actual error is a type error due to the different number of arguments that the function uses when invoked. This means that 6 arguments were keyed in when only 1 parameter is defined. 
# => the solution is to change input args as list.

# 2. type error thrown, because an int is not an iterable. 
# => solution is to turn into a list
