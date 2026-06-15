def reverse_number(n, current_reverse=0):
    if n == 0:
        return current_reverse
    return reverse_number(n // 10, current_reverse * 10 + n % 10)
