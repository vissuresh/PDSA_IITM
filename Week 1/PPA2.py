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
