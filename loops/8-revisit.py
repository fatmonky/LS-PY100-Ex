'''
The following code keeps looping forever. (You can hit Ctrl-C to stop it.) Why does the loop keep running? Modify it so that it stops after the first iteration.

while True:
    print("and on")
'''
'''
#my answer 1:
print_var = print("and on")

while print_var != None:
    print_var
'''
# my answer 2: 
print_var = print("and on")

while print_var:
    print_var

# model answer:
while True:
    print("and on")
    break
