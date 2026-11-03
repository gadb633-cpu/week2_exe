
# def is_pass_grade(grade):
#     if grade >= 60:
#         return "pass!!"
#     else:
#         return "fail!!"
# print(is_pass_grade(45))    

# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade
#     def is_passing_grade(self):
#         if self.grade >= 60:
#             return "pass!!"
#         else:
#             return "fail!!" 
# Gad = Student("gad",95)
# print(Gad.is_passing_grade())      

# def get_how_much_days():
#     how_much_days  = int(input("enter your anser: "))
#     return how_much_days

# def get_list_temp(num_of_days):
#     temp_list = []
#     for i in range(num_of_days):
#         day_temp = float(input("enter temp day: "))
#         temp_list.append(day_temp)
#     return temp_list

# def get_temp_avg(temp_list):
#     avg_temp = sum(temp_list) /len(temp_list)
#     return avg_temp

# def get_temp_status(avg_temp):
#     if avg_temp >30:
#         return f"avg: {avg_temp} hot!!"
#     elif 30 <avg_temp>20:
#         return f"avg: {avg_temp} normal!!" 
#     else:
#         return f"avg: {avg_temp} cold!!"

# def main():
#     how_much_days = get_how_much_days() 
#     temp_list = get_list_temp(how_much_days)
#     temp_avg = get_temp_avg(temp_list)
#     print(get_temp_status(temp_avg))

# main()      

def parse_percentage(text):
    try:
        if not text.endswith("%"):
            raise ValueError("must end with %!!")        
        num = int(text[:-1])
        if 0 > num or num > 100:
            raise ValueError("must be between 0-100!!")
        return num
    except ValueError as error:
        return error
print(parse_percentage("120"))  

import logging

logging.basicConfig(filename="app.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s: %(message)s")


def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    if b == 0:
        logging.error("Division by zero attempted.")
        return None
    return a / b

result = divide(10, 1)

   