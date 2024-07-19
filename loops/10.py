'''
Modify the following code so the loop continues iterating until the user inputs 'yes'.

while True:
    print('Should I stop looping?')
    answer = input()
    '''

while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break
    print("incorrect answer. please answer yes.") # model answer
