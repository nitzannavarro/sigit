
#function that cheack if the id is good
def chackID(id):
    lastdigit=id%10
    id/=10
    id = int(id)
    sum=0
    # run at all digits of the number
    while id!=0:
        digit=(id%10)*2
        id /= 10
        id=int(id)
        if digit>9:
           digit =(digit%10)+((digit/10)%10)
           digit = int(digit)
        sum+=digit
        sum += (id % 10) * 1
        id /= 10
        id = int(id)
    sum=10-(sum%10)
    if lastdigit == sum:
        print ('good id')
    else:
        print('bad id')


chackID(322482464)