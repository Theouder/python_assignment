import math
file = open(r"D:\python_assignments\Unbend_Model 4.stl")
x= file.readlines()
allpoints = []
allareas = []
for i in x:
   if 'vertex' in i:
      a = i.split()
      b = a[1:]
      c = [float(d) for d in b]
      allpoints.append(c)
      if len(allpoints)==3:
         p1,p2,p3=allpoints
         allpoints.clear()
         x1, y1, z1 = p1
         x2, y2, z2 = p2
         x3, y3, z3 = p3
         a1 =math.sqrt(pow(x2-x1 ,2)+pow(y2-y1 ,2)+pow(z2-z1 , 2))
         b1 =math.sqrt(pow(x3-x2, 2)+pow(y3-y2, 2)+pow(z3-z2, 2))
         c1 =math.sqrt(pow(x3-x1, 2)+pow(y3-y1, 2)+pow(z3-z1, 2))
         s = (a1+b1+c1)/2
         area=math.sqrt(s*(s-a1)*(s-b1)*(s-c1))
         allareas.append(area)    

print(allareas)
print(sum(allareas)) 