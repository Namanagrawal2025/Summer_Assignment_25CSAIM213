def print_armstrong_in_range(lower, upper):
    armstrong_numbers = []
    
    for number in range(lower, upper + 1):
        num_str = str(number)
        power = len(num_str)
        
        total_sum = sum(int(digit) ** power for digit in num_str)
        
        if total_sum == number:
            armstrong_numbers.append(number)
            
    return armstrong_numbers
