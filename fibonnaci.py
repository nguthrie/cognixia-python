
def fibo_less_than_n(n):
    N0 = 0
    N1 = 1
    
    previous_fib = N0
    current_fib = N1

    while current_fib < n:
        print(current_fib)
        tmp = current_fib
        current_fib = current_fib + previous_fib
        previous_fib = tmp
        

fibo_less_than_n(10000)