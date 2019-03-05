

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            #if i have the risult in the cache it return him
            return cache[args]
        result = func(*args)
        # add to the cache the new result
        cache[args] = result
        return result

    return memoized_func
#send the function to the Decorator Cache function
@memoize
def fibo(n):
    if n<2:
        return n
    return fibo(n-1)+fibo(n-2)

print( fibo(200))
