# NOTE: For python " " == ' '

# Q1. Write program to print last character of any string? ie Print "E" from "IIT-JEE"?

# Q2. Write a program to find the last digit of a number?
num = 123456789 
print(num%10) #Using Modulo Operator

num = 77650
print(num%10)

y = str(num) #Using String
print(y[-1]) 


# Q3. Write a program to find the last name from a given full name?
name = "Aryan Jain"
x = name.find(" ")
print(name[x+1:])


# Q4. Write a program to exchange the values of 3 variables in a cyclic manner, without using any new variable?
x = 41
y = 57
z = 39
print(x,y,z)
x = x+y-z
y = x-y+z
z = x-y+z
x = y+z-x
print(x,y,z)


# Q5. Write a program which prints the output of division of two integers as a proper fraction?
D = 357
d = 19
q = D//d
r = D%d
print("%s %s/%s" %(q,r,d))

D = 121
d = 5
q = D//d
r = D%d
print(q," %s" %r, "/ %s" %d)
print(str(str(q)+" "+str(r)+"/"+str(d))) #Using String Concatenation

# Q6. Write a program to find the greatest integer less than or equal to a number?
x = 1.67
y = x%1
print (int((x-y)))

x = -3.57
y = x%1
print (int((x-y)))