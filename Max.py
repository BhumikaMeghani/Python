class Max:
    def __init__(self,n1 , n2 , n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
    def max(self)->float:
        if (self.n1 > self.n2 and self.n1 > self.n3):
         return self.n1
        elif (self.n2>self.n1 and self.n2>self.n3):
          return self.n2
        else:
           return self.n3
n1 = float(input("Enter first number: "))
n2 = float(input ("Enter second number: "))
n3 = float(input("Enter third number: "))
m = Max(n1,n2,n3)
result = m.max()
print(f"Maximum Number is : {result}")