
SECRETCODE='1234'
MONEY=1234
#make the login
def start():
    b= True
    while b:
        secretcode= input('pls enter your secret code:\n')
        if secretcode==SECRETCODE:#check if the secret code is corect
            if Menu():
                b=False



def Menu():
    global MONEY
    global SECRETCODE
    #choice the thing he want to do
    choice=input('pls enter your choice:\n'
                 'a-check your money \n'
                 'b-take money\n'
                 'c-change secret code\n'
                 'd-to exit\n')
    if choice=='a':
        print ('you have: '+str(MONEY)+'$') # show the money that he have
    elif choice=='b':#take money
        mon = input('how match money you are take:\n'
                       'a-20 \n'
                       'b-50\n'
                       'c-difrent money\n')
        if mon== 'a':
            MONEY-=20
        elif mon == 'b':
            MONEY -= 50
        elif mon == 'c':
            MONEY -= int(input('how match money you are take:\n'))
    elif choice == 'c':# change secret code
        SECRETCODE=input('enter the new secret code:\n')
    elif choice == 'd':# exit
        return 1
    return 0

start()
