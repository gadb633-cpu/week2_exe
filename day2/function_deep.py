# function deep
# exe 1
def make_greeting(name, greeting="Hello", punct="!"):
    return f"{greeting}, {name} {punct}"
print(make_greeting("Dana"))
print(make_greeting("Avi", "Good morning"))
print(make_greeting("Noa", punct="?"))

# exe 2
def average(*numbers):
    avg = 0
    for num in numbers:
        avg +=num
    if avg == 0:
        raise ValueError("need at least one number")    
    return avg / len(numbers)


print(average(80, 90))
print(average(70, 80, 90, 100))
try:
    average()
except ValueError as error:
    print("error:", error)


