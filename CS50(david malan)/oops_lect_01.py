class employee :
    def __init__(self,first,last,pay,house):
        self.first = first
        self.last = last
        self.pay = pay
        self.last = last
        self.house = house
        self.emai = first + "." + last + "@gmai.com"

    def fullname(self):
        return"{}{}".format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * 1.6)

emp_1 = employee("corey","chase","50000","jonasburg")
emp_2 = employee("glenn","maxwell","70000","sydney")
emp_3 = employee("David","warner","75000","melborne")
emp_4 = employee("sam","curran","89000","london")

print(f"the salary of employee 2 is ",emp_2.pay)
print(f"the salary of employee 1 is" ,emp_1.pay)
print(f"the salary of employee 2 is ",emp_3.pay)
print(f"the salary of employee 1 is" ,emp_4.pay)


