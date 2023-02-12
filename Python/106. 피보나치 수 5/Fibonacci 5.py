def fibo(n):
    if n < 2:
        return n
    return fibo(n-2) + fibo(n-1)

n = int(input())
print(fibo(n)) 