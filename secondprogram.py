class Employer():
    salary = 100
    increment = 1.5

    @property
    def totalsalary(self):
        return self.salary * self.increment

    @totalsalary.setter
    def totalsalary (self , val):
        total = val/self.salary
        print(total)

e = Employer()
print(e.totalsalary)
e.totalsalary = 300