# Higher-Order Functions
# exe 1
def apply_to_all(numbers, action):
    new_numbers = []
    for num in numbers:
        new_numbers.append(action(num))
    return new_numbers    
def double(n):
    return n*2
print(apply_to_all([1, 2, 3], double))
print(apply_to_all([1, 2, 3], lambda n: n * n))
print(apply_to_all([1.6, 2.4], round))
