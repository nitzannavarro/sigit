
#zipping the string
def zipString(string):
    leng= len(string)
    i=0
    afterZip=''
    count=0
    #count how match frome eche charter and make the zip string
    while i<leng-1:
        count+=1
        if string[i]!=string[i+1]:
            afterZip+=string[i]
            afterZip += str(count)
            count=0
        i+=1
    count += 1
    afterZip += string[i]
    afterZip += str(count)
    print (afterZip)


st='aabbcdaaaaaa'
zipString(st)