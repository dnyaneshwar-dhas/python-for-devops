print("Hello World") 
print("My name is Dnyaneshwar")
print("I am learning python programming")
------------------------------------------------------------------
---------------------#Variable---------------------------------
#variable is basically a name that refer to some value 

#example:1
age = 25
print( age )

#example:2
name = "dnyaneshwar"
city = "pune"
age = 25
print(age)
print(name)
print(city)

#basic operator 
a = 8
b = 9

addition = a + b 
subtraction = a - b 
multiplication = a * b
division = a / b 

print("Division is:", division)
print("multiplication is:", multiplication)
print("Addition is :", addition)
print("subtraction is:", subtraction)

#Take input 
#1
name = input("Enter your name: ")
city = input("Enter your city name: ")

print(name)
print(city)

#2
name = input("Enter your name: ")
city = input("Enter city name: ")

print("Hello " + name)
print("This is nice city, " + city)

#convert input to integer
#1
age = int(input("Enter your age: "))

print(age + 5) 

#2
num1 = int(input("Enter first num:"))
num2 = int(input("Enter second num:"))
print(num1 + num2)

##*********************************************************##
##Arithmetic Operators 
# Addition         
a = 10       
b = 6          
result = a + b  
print(result)


# Subtraction
a = 10
b = 5
result = a - b 
print(result)


# Multiplication 
a = 6
b = 3
result = a * b 
print(result) 


# Division 
a = 10
b = 2
result = a / b 
print(result)


# Reminder
a = 10
b = 3
result = a % b 
print(result)


# Floor Division //
a = 10
b = 3 
result = a // b
print(result) 


# power **
a = 2
b = 3   
result = a ** b
print(result)

##********************************************************##
## Comparison Operator 
# equal to (==)
a = 10
b = 10
result = a == b 
print(result)


# not equal to (!=)
a = 10
b = 20
result = a != b 
print(result)


# greater than (>)
a = 10
b = 5
result = a > b
print(result)


# less than (<)
a = 15
b = 20
result = a < b
print(result)


# greater than or equal to (>=)
a = 15
b = 20
result = a >= b
print(result)


# less than or equal to (<=)
a = 15      
b = 20
result = a <= b
print(result)

## Condition Statement 
#if (1)                | (2)
marks = 80             | age = 20
if marks >= 50:        | if age >= 18:
    print("pass")      |    print("You can vote")

## if-else(1)                                |(2)
age = 20                                     | marks = 80
if age >= 18:                                | if marks <= 50:
    print("you are eligible to vote")        |     print ("fail")
else:                                        | else:
    print("you are not eligible to vote")    |     print("pass")

## if-elif-else
marks = 85
if marks >= 90:
    print("Pass with A Grade")
elif marks >= 75:
    print("Pass with B Grade")
elif marks >= 60:
    print("Pass with C Grade")

else: 
    print("Fail")
    
