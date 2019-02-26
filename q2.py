


# the user enter a number until he has written stop then the function prints the sum of the user's numbers.
def q2A():
    sum=0
    enter=input('enter a number and Stop to stop the progrem\n')
    while enter!='Stop':
        sum+=int(enter)
        enter = input('enter a number and Stop to stop the progrem\n')
    print (str(sum))

# the user enter a list like this 1,2,3,4 then the function prints the sum of the user's list.
def q2B():
    sum=0
    enter = input('enter a list of number (exmple 1,2,3,4)\n')
    afterSplit= enter.split(',')#split the list by the ,
    for i in afterSplit:
        sum+=int(i)
    print(str(sum))
q2B()
