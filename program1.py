print("Hello World") 
print("My name is Dnyaneshwar")
print("I am learning python programming")
------------------------------------------------------------------
---------------------#Variable------------------------------------
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
#if (1)               
marks = 80             
if marks >= 50:        
    print("pass")      

#(2)
age = 20
if age >= 18:
    print("You can vote")


## if-else(1)                                
age = 20                                     
if age >= 18:                               
    print("you are eligible to vote")        
else:                                        
    print("you are not eligible to vote") 

#(2)
marks = 80
if marks <= 50: 
    print("fail")           
else:
    print("pass")


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


##Loops 
#for 
#(1)
for i in range(1, 6):
    print(i)

#(2)
servers = ["server1", "server2", "server3"]
for server in servers:
    print(server)

#(3)
names = ["Dnyanu", "Sagar", "Amit", "Hrutik", "Sudarshan", "Yash"]
for name in names:
    print("Hello Friend", name)

#while
#(1)
count = 1
while count <= 5:
    print(count)
    count = count + 1 

#(2)
count = 10
while count >= 1:
    print (count)
    count = count - 1 

##f-strings
#(1)
name = "Omkar"
age = 22
print(f"My name is {name}")
print(f"My name is {age}")

#(2)
server = "web-svc-1"
cpu = 85 
print (f"server {server} cpu is {cpu}% ")

##Lists 
names = ["Dnyanu","Rahul","Ashish"]
print(names)

##list Indexing
tools = ["AWS","Docker","Teraform","jenkins"]
print(tools[2])
print(tools[3])

#(2)
cloud_services = ["Ec2","S3","Rds","vpc","eks"]
print(cloud_services[0])
print(cloud_services[2])
print(cloud_services[4])

##append() -----> use to add the item in the list
tools = ["AWS","Docker","Kubernetes"]
print(tools)
tools.append("Jenkins")
print(tools)

##remove() --->use to remove from list
tools = ["aws","docker","kubernetes","jenkins"]
print(tools)
tools.remove("jenkins")
print(tools)

##insert() ---->use to add item in specific position
tools = ["Aws","Docker","Jenkins"]
print(tools)
tools.insert(2,"kubernetes")
print(tools)

##pop() ---> remove an item using itd index 
names = ["Omkar","Ajay","Hrutik","Atharva"]
print(names)
names.pop(2)
print(names)

##len() ---> find the number of items 

tools = ["aws","Docker","kubernets","jenkins"]
print(len(tools))

##in() ---->check if an item exist in list 
tools = ["AWS","Kubernetes","Jenkins"]
if "Docker" in tools:
    print("Docker is available")
else:
    print("Docker is not available")

## sort() && reverse()
#(1)
numbers = [ 50,10,20,40,30]
print (numbers)
numbers.sort()

#(2)
numbers = [50,10,20,40,30]
print(numbers)
numbers.sort(reverse=True)
print(numbers)