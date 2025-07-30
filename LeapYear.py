import string
class leap:
    def __init__ (self,y):
        self.y = y
    def check(self)->string:
        if (self.y%4==0):
            return 'Leap Year'
        else:
            return 'Not a Leap Year'
y = int(input("Enter year : "))
l = leap(y)
result = l.check()
print(f"{y} is {result}")