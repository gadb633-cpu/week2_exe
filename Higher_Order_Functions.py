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

# exe 2
prices = [20, 75, 120, 45, 90]
expensive = list(filter(lambda p: p > 50, prices))
raised = list(map(lambda p: p + 10, expensive))
print(expensive)
print(raised)

# exe 3
words = ["banana", "fig", "cherry", "kiwi"]
students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]

print(sorted(words, key=len))
print(max(words, key=len))

for name, grade in sorted(students, key=lambda s: s[1], reverse=True):
    print(name)