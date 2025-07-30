import string
class check:
    def __init__(self,num):
        self.num = num
    def checknum(self)->string:
        if (self.num%2==0):
            return 'Even'
        else:
            return 'Odd'
n = float(input("Enter number : "))
c=check(n)
result = c.checknum()
print(f"{n} is {result}")