import time

def fun_timer(function):
    def wrapper(k):
        start_time=time.time()
        function(k)
        end_time=time.time()
        print('Execution time:', end_time-start_time, 'seconds')
    return wrapper

def fun_timer_cpu(function):
    def wrapper(k):
        start_time=time.time()
        function(k)
        end_time=time.time()
        print('CPU Execution time:', end_time-start_time, 'seconds')
    return wrapper

def result_in_bin(function):
    def wrapper(a,b):
        c=function(a,b)
        return bin(c)
    return wrapper
def timeit(fun):

    def wrapper(*args, **kw):
        start_time = time.time()
        result = fun(*args, **kw)
        end_time = time.time()
        print ('func:%r args:[%r, %r] took: %2.6f sec' % \
          (fun.__name__, args, kw, end_time-start_time))
        return result
    return wrapper

@timeit
def rangeFun(n,c):
    for i in range(n):
        continue

@result_in_bin
def sum(a,b):
    return a+b



rangeFun(9907850,1)
print(sum(4,8))
