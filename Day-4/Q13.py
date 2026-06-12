def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_series = [0, 1]
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
        
    return fib_series
