def calculate_sum(num_list):
    """
    This function takes in a list of integers and returns their sum.
    """
    sum = 0
    for num in num_list:
        sum += num
    
    return sum
    
print(calculate_sum([1, 2, 3, 4, 5]))
print(calculate_sum([10, 20, 30, 40, 50]))
print(calculate_sum([100, 200, 300, 400, "500"]))
