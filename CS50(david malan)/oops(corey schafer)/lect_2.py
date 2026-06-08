class employee :
    raise_amount = float(input("enter raise_amount :"))

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
        self.fullname = first + " " + last 

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = employee("corey","schafer",400000)
emp_2 = employee("radhe","shayam",1000008)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.fullname)
print(emp_1.email)
print(emp_2.fullname)
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)
print(emp_2.fullname)
print(emp_2.email)