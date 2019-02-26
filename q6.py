
#fuction that get a number and calculate the number * 2
def Multi(x):
    return x*2


#fuction that get a number and calculate the pow of the number
def pow(x):
    return x*x

#fuction that get a pointer to function and a array and do the function on all the valuo
def Map(f,a):
    i=0
    while i<len(a):
        a[i]=f(a[i])
        i+=1

a=[1,2,3,4]
Map(Multi,a)
print (a)
Map(pow,a)
print ( a)