class area:
    def __init__(self ,r,b,h): #Constructor
       self.r=r
       self.b=b 
       self.h=h
    def circle(self)->float:
     return 3.14*self.r*self.r
    def triangle(self)->float:
       return 0.5*self.b*self.h
rad=float(input("Enter radius for circle :"))
b=float(input("Enter breadth for triangle : "))
h=float(input("Enter height for triangle: "))
A=area(rad, b,h)

resultcir = A.circle()
resultTri = A.triangle()
print(f"Area of circle : {resultcir}")
print(f"Area of Triangle : {resultTri}")