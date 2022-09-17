'''Create a Triangle class that accepts three side-lengths of the triangle as a, b and c as parameters at the time of object creation. Class Triangle should have the following methods : • Is_valid () : Returns valid if triangle is valid otherwise returns Invalid. o A triangle is valid when the sum of its two side-length are greater than the third one. That means the triangle is valid if all three condition are satisfied : ▪a+b>c ▪a+c>b ■ b + c> a • Side_Classification() : - If the triangle is invalid then return Invalid. Otherwise, it returns the type of triangle according to the sides of the triangle as follows : o Return Equilateral if all sides are of equal length. o Return Isosceles if any two sides are of equal length and third is different. o Return Scalene if all sides are of different lengths. Angle_Classification() : - If the triangle is invalid then return Invalid. Otherwise, return type of triangle using Pythagoras theorem. For example if a <= b <= c. then o If a² + b²>c² return Acute o If a² + b² = c² return Right o If a² + b² < c² return obtuse In the formula of angle classification, the square of the largest side length should be compared to the sum of squares of the other two side lengths. • Area() : - If the triangle is invalid then return Invalid. Otherwise, return the area of the triangle. o Area = √s(sa)(sb)(s - c)
Where s = (a+b+c)/2 '''

class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def Is_valid(self):
        if(self.a+self.b>self.c and self.b+self.c>self.a and self.c+self.a>self.b):
            return 'Valid'
        return 'Invalid'
    
    def Side_Classification(self):
        if(self.Is_valid()=='Invalid'):
                return 'Invalid'
        if(self.a==self.b==self.c):
            return 'Equilateral'
        elif(self.a==self.b or self.b==self.c or self.c==self.a):
            return 'Isosceles'
        return 'Scalene'
    
    def Angle_Classification(self):
        if(self.Is_valid()=='Invalid'):
            return 'Invalid'
        a,b,c=sorted((self.a,self.b,self.c))
        if(a*a+b*b>c*c):
            return 'Acute'
        elif(a*a+b*b==c*c):
            return 'Right'
        return 'Obtuse'
        
    def Area(self):
        from math import sqrt
        if(self.Is_valid()=='Invalid'):
            return 'Invalid'
            
        a,b,c=self.a,self.b,self.c
        s=(a+b+c)/2
        area=sqrt(s*(s-a)*(s-b)*(s-c))
        return area

a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())
