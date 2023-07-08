'''
This module will contain all the different methods to solve fibonacci series problem.
It can be the normal recursion method as well as method that involve the use of Dynamic Programming
Concepts.
Both Memoization and Tabulation approach will be shown.
'''


def fibonacci_naive(n: int):
    '''This function will use the naive method to solve fibonacci series problem.'''
    if(n<=1):
        return n
    else:
        return (fibonacci_naive(n-1)+fibonacci_naive(n-2))

def fibonacci_memoisation_core(n: int, dp: list):
    '''This function will use top-down approach to solve fibonacci.'''
    if(n<=1):
        return n
    elif(dp[n]!=-1):
        return dp[n]
    else:
        dp[n] = fibonacci_memoisation_core(n-1, dp) + fibonacci_memoisation_core(n-2, dp)
        return dp[n]

def fibonacci_memoisation(n: int):
    '''This function calls the core memoisation fucntion.'''
    dp = [-1]*(n+1)
    return fibonacci_memoisation_core(n, dp)

def fibonacci_tabulation(n: int):
    '''This function will follow bottom-up approach'''
    dp = [0,1]
    if(len(dp)<=n):
        for index in range(2, n+1):
            dp.append(dp[index-1] + dp[index-2])
    return dp[n]

def fibonacci_best(n: int):
    '''This function is the best for fibonacci series.'''
    pre = 0
    post = 1
    if(n<=1):
        return n
    else:
        for i in range(2, n+1):
            fib = pre + post
            pre = post
            post = fib
        return post


if(__name__=='__main__'):
    n = int(input("Enter the position of element you want (Starting from 0) : "))
    import time
    start = time.perf_counter()
    value = fibonacci_best(n)
    end = time.perf_counter()
    et1 = end - start
    print(f'{value} is obtained in {et1} seconds by Best Algorithm')
    start = time.perf_counter()
    value = fibonacci_memoisation(n)
    end = time.perf_counter()
    et2 = end - start
    print(f'{value} is obtained in {et2} seconds by Memoisation Algorithm')
    start = time.perf_counter()
    value = fibonacci_tabulation(n)
    end = time.perf_counter()
    et3 = end - start
    print(f'{value} is obtained in {et3} seconds by Tabulation Algorithm')
    start = time.perf_counter()
    value = fibonacci_naive(n)
    end = time.perf_counter()
    et4 = end - start
    print(f'{value} is obtained in {et4} seconds by Naive Algorithm')
    l = [et1, et2, et3, et4]
    print(sorted(l))
    print("Thank You")
