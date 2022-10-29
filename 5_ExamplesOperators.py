#Example 1
#BDMAS Test
a = 24/2-6
b = 24-6/2
c = (3+1)*(4+4)/(1+1)
print(a,b,c)

#Example 2
#Find number of divisiors of 360?
#Ans. Prime Factorisation Of 360 = 2*2*2*3*3*5
#360 = 2^3 * 3^2 * 5^1
n = (3+1)*(2+1)*(1+1)
print(n)

#Example 3
# Find e^pi v/s pi^e?
import math
from re import X
t = math.e ** math.pi
p = math.pi ** math.e
print("e^pi > pi^e ? ", t > p)
print(t,p)
print("e > pi ? ", math.e > math.pi)

#Example 4
#1. Exchange values inside variables using a dummy variable.
x = 2
y = 3
print (x,y)
temp = x
x = y
y = temp
print (x,y)
#2. Exchange values inside variables without using a dummy variable.
x = 2
y = 3
print (x,y)
x = x + y
y = x - y
x = x - y
print (x,y)
#3. Exchange values inside variables without using a dummy variable. Using LISTS.
x = 2
y = 3
print (x,y)
x,y = y,x
print (x,y)