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
        
emp_1 = employee("radhe","shayam",100008)
print("before pay raise :",emp_1.pay)
pay = emp_1.apply_raise()
print("after pay raise:",emp_1.pay)
print("email :",emp_1.email)
print("full name",emp_1.fullname)

# regular way of splitting then printing i.e. using self.

emp_str_1 = "john-cena-700000"

first,last,pay = emp_str_1.split("-")
emp_info = employee(first,last,pay)

print("emp_str full name is ",first + " "+last)
print ("emp_str pay scale ",pay)

