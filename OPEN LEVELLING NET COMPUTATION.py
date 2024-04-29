import math

print("This program calculates the elevations in open levelling net")
print("-"*55)

k_point = input("Enter the point ID of known point :")

print("Enter the elevation of point ",k_point," (m) :")
k_point_1 = float(input())

un_point= int(input("Enter the number of unknown points :"))

points = []
points.append(k_point)

for i in range(un_point):
    np = (input("Enter the point ID of unknown point " + str(i+1) + " : "))
    points.append(np)

BS = []
for i in range(0, un_point):
    BSr = float(input("Enter the BS reading of point " + str(points[i]) + " (m) : "))
    BS.append(BSr)
    
FS = []
for i in range(1, 1 + un_point):
    FSr = float(input("Enter the FS reading of point " + str(points[i]) + " (m) : " ))
    FS.append(FSr)

sum_points = []
for i in range(un_point):
    sum_point = BS[i] - FS[i]
    sum_points.append(sum_point)

h = sum_points[0]
hb = float(k_point) + h
h1 = hb + h
h2 = h1 + h
h3 = h2 + h

print("-"*73)
print("%-15s %-15s %s" %("Point ID", "Point ID", "Delta H"))
print("-"*55)
print("%-15s %-15s  %s" %(k_point, points[1], sum_points[0]))

