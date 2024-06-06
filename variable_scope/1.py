# completed 6 June. wrong questions: 1, 4, 5.


#!1: my answer: error, as my_value is local within the if statement's scope, while the print statement is in global scope. 

# model answer: 20. In Python, variables initialized inside a block are accessible outside the block (TIL!)

#2
x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

#2: my answer, error thrown, because x is initialized by has no initial value. so my_function will not return any value nor print any value.
# model answer: if we want to modify the global x, we would need to use the global keyword:

def my_function():
    global x
    x = x + 5
    print(x)

#3:
def my_function():
    a = 1

    if True:
        print(a)

my_function()
# my answer: prints 1, since True is true, so print(a) will be called.


#!4:
a = 1

def my_function():
    print(a)

my_function()
#my answer: throw an error, as my_function doesn't have any arguments, so it can't access global scope variables.
#model answer: it will print 1. function bodies can access global variables. 

#!5:
a = 1

def my_function():
    print(a)
    a = 2

my_function()

# my answer: it will print 1, then assign a local variable a to the value of 2.
# model ans: it throws an error, as Python detects a i sbeing assigned within my_function, and therefore treats it as a local variable. and since we are trying to print it before it has been assigned, it throws an error.

#6:
a = 1

def my_function():
    a = 2

my_function()
print(a)

# my ans: prints 1. the a = 2 is local to my_function, and doesn't affect the global variable's value.

#7:
a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# my ans: prints 2. because global a causes my_function to manipulate the global a variable, which is re-assigned to value 2.

#8:
print(greeting)

greeting = 'Hello world!'
# my ans: error thrown, as greeting is printed before any assignment. 


#9:
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# my ans: it will print 7. while a is fed as an argument into my_function, my_function doesn't reassign the value of a to the return result of my_function.

#10:
b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# my ans: it will print [10, 2, 3]. calling my_function re-assigns b[0], which mutates the entire list b.
