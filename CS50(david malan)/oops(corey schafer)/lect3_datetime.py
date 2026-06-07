import datetime
class employee:
    raise_amt = float(input("raise_amt :"))
    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = (first + "." + last + "@gmail.com")
        self.fullname = first + " " + last
    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amt)
        
# emp_1 = employee("radhe","shayam",100008)
# print("before pay raise :",emp_1.pay)
# pay = emp_1.apply_raise()
# print("after pay raise:",emp_1.pay)
# print("email :",emp_1.email)
# print("full name",emp_1.fullname)

# # # regular way of splitting then printing i.e. using self.

# # emp_str_1 = "john-cena-700000"

# # first,last,pay = emp_str_1.split("-")
# # emp_info = employee(first,last,pay)

# # print("emp_str full name is ",first + " "+last)
# # print ("emp_str pay scale ",pay)

# # splitting by using  @classmethod(cls)

#     @classmethod
#     def from_string(cls,emp_str):
#         first,last,pay = emp_str.split("-")
#         return cls(first,last,pay)

# emp_str_1 = "john-cena-700000"
# emp_2 = employee.from_string(emp_str_1)
# print("emp_2 full name is ",emp_2.fullname)
# print("emp_2 pay scale is ",emp_2.pay)     



# using @staticmethod

    @staticmethod
    def is_workingday(day):
        days = [
            "monday",
            "tuesday",
            "wednesday",
            "thusday",
            "friday",
            "saturday",
            "sunday"
        ]
        day_name = days[day.weekday()]
        if day.weekday() == 5 or day.weekday() == 6:
            return day_name, False
        return day_name, True 
year = int(input("year is :"))
month = int(input("month is :"))
day = int(input("day is : "))

my_date = datetime.date(year,month,day)
day_name , working = employee.is_workingday(my_date)

print("date is ",my_date)
print("day name is ", day_name )

if employee.is_workingday(my_date):
    print("its a working day")
else :
    print("its a holiday")    





