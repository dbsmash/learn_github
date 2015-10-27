def recursive_fib(n):
    if n <= 1:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)


def iterative_fib(n):
    '''
    This is an iterative implemention of the Fibonacci sequence
    '''
    a = 0
    b = 1
    for i in range(0, n):
        temp = b
        b = a + b
        a = temp
    return b

if __name__ == '__main__':
    print iterative_fib(20)
