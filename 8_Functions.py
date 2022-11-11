#FUNCTIONS WITHOUT ARGUMNET
#Defining a function that can be called to mark completion of a task.
def task_finished(): 
    print("You have successfully finished the task!")

task_finished()

#Defining a function that returns an output = 0
def returnzero():
    return 0

x = returnzero()
print(x)

#FUNCTIONS WITH ARGUMNETS
def cubing(x):
    return x**2

print(cubing(11))

#Function with TWO arguments
def x_plus_y_square(x,y):
    return(x+y) ** 2

print(x_plus_y_square(3,5))

#EXAMPLE 1
#Function to convert temprature fro celcius to farenheit
def temp_farenh(temp):
    return (temp * (9/5)) + 32 #(temp °C × 9/5) + 32 = temp °F

print(temp_farenh(0))
print(temp_farenh(37))
print(temp_farenh(-40)) #At -40 degree celcius = farenheit

#EXAMPLE 2
#Function to find GM of 3 Nos.
def gm(x,y,z):
    g = (x*y*z)**(1/3)
    return g
x = gm (2,4,8)
print(x)
import math
y = round(x)
print(y)