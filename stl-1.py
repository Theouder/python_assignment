file = open(r"D:\python_assignments\myTet.stl")


# file = open(r"D:\python_assignments\myTet.stl")
# file = open("D:/python_assignments/myTet.stl")
# file = open("D:\\python_assignments\\myTet.stl")


x = file.readlines()
allpoints = []
for i in x:
    if "vertex" in i:
        b = i.split()
        
Face1 = allpoints[0:3]
Face2 = allpoints[3:6]
Face3 = allpoints[6:9]
Face4 = allpoints[9:]
print(b)
# print(Face1)
# print(Face2)
# print(Face3)
# print(Face4)