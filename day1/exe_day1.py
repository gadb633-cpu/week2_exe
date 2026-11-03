# # part 1
# # exe 1
# def get_total_price_items(price,quantity):
#     total_price = price * quantity
#     if total_price > 500:
#         total_price -=50
#     return total_price

# print(get_total_price_items(120,5))
# print(get_total_price_items(20,3))

# # exe 2
# LIMIT_PRICE = 200
# DELIVERY = 30
# def add_delivery_price(price,limit_price,delivery):
#     if price < limit_price:
#         price +=delivery
#     return price    

# # exe 3
# def is_valid_password(password):
#     if len(password) >= 8:
#         for char in password:
#             if char.isnumeric():
#                 return True
#         return False    
#     else:
#         return False
# print(is_valid_password("abc12345"))
# print(is_valid_password("abcdefgh"))
# print(is_valid_password("a1"))

# # part 2
# # exe 1
# def get_reception(names,amont,quantity):
#     total_price = 0
#     for i in range(len(names)):
#         total_price += amont[i]
#         print(f"{names[i]}: {quantity[i]} X {amont[i]} = {quantity[i] * amont[i]}")
#     print(f"total: {total_price}")
# get_reception(["Pen", "Notebook", "Bag"], [5, 12, 60], [4, 2, 1]) 

# # exe 2
# def parity(num):
#     if num %2==0:
#         return "even"
#     else:
#         return "odd"

# print(parity(4))
# print(parity(7))

# # exe 3
# def get_info():
#     weight = float(input("enter weight: "))
#     height = float(input("enter height: "))
#     return [weight,height]
# def calculate_bmi(weight, height):
#     return f"BMI: {round(weight/(height*height),1)}"
# list_info = get_info()
# print(calculate_bmi(list_info[0],list_info[1]))

# part 3
# exe 1
# if age > 18
#     print("adult")  SyntaxError

# # B
# print(total_price)        Runtime Error

# # C
# def area(width, height):
#     return width + height   Logical Error

# exe 2
# 1. ZeroDivisionError: division by zero
# 2. File "shop.py", line 3, in average_price
# 3. File "shop.py", line 12, in <module>
    # print(checkout([20, 30], 0))

# # exe 3
# def to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9
# print(to_celsius(212))
# print(to_celsius(32))

# part 4
# exe 1
# 1. Reproduce 
# 2. Isolate
# 3. Understand 
# 4. Fix 
# 5. Verify 

# # exe 2
# def find_max(numbers):
#     largest = numbers[0]
#     for number in numbers:
#         if number > largest:
#             largest = number
#     return largest

# print(find_max([4, 9, 2]))
# print(find_max([-7, -3, -10]))

# # exe 3
# def count_vowels(word):
#     count = 0
#     for letter in word:
#         if letter in "aeiou":
#             count = count + 1
#     return count

# print(count_vowels("banana"))

# # part 5
# # exe 1
# def to_number(text):
#     try:
#         return int(text)
#     except:
#         return None
# print(to_number("42"))
# print(to_number("hello"))
# print(to_number("7"))

# # exe 2
# def safe_divide(a_text, b_text):
#     try:
#         return int(a_text) / int(b_text)
#     except ZeroDivisionError:
#         return "cannot divide by zero"
#     except ValueError:
#         return "numbers only"
# print(safe_divide("10", "4"))
# print(safe_divide("10", "0"))
# print(safe_divide("ten", "2"))    

# # exe 3
# try:
#     number = int("12abc")
# except ValueError as error:
#     print("Could not convert:", error)    

# # part 6
# # exe 1
# def half(text):
#     try:
#         number = int(text)
#     except ValueError:
#         print("not a number:", text)
#     else:
#         print("half is", number / 2)
#     finally:
#         print("checked", text)

# half("8")
# half("x")
# '''
# half is 4.0
# checked 8
# not a number: x
# checked x
# '''

# # exe 2
# def check(number):
#     try:
#         if number > 0:
#             return "positive"
#         return "not positive"
#     finally:
#         print("done checking", number)

# print(check(5))
# print(check(-2))
# '''
# done checking 5
# positive
# done checking -2
# not positive
# '''

# # exe 3
# def parse_quantity(text):
#     try:
#         number=int(text)
#     except ValueError as error:
#         print(f"invalid: {text}",error)
#     else:
#         print(f"quantity: {number}")
#     finally:
      #         print("----")
# parse_quantity("3")
# parse_quantity("three")        

# # part 7
# # exe 1
# def set_age(age):
    
#     if 0 > age or age > 120:
#         raise ValueError(f"age must be between 0 and 120  {age}")
#     return age
    
# for age in [25, -3, 150]:
#     try:
#         print("ok:", set_age(age))
#     except ValueError as error:
#         print("error:", error)  

# # exe 2
# def validate_username(name):
#     if 3 > len(name):
#         raise ValueError(f"too short")
#     if " " in name:
#         raise ValueError(f"no spaces allowed")
#     return name

# for name in ["dana", "al", "big boss"]:
#     try:
#         print("valid:", validate_username(name))
#     except ValueError as error:
#         print(name, "->", error)    

# exe 3
