import math
n = int(input())
m = n
c = []
pascal_triangle = []

for i in range(n+1):
    for j in range(m+1):
        pascal_triangle.append(int(math.factorial(n)/(math.factorial(j)*math.factorial(n-j))))
print(pascal_triangle)
