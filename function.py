#tuple
#tupples are immutable,no chance possible
cd = (4, 5)
print(cd[1])

#Functions

def say_hi():
    print("Hello,user")
    
say_hi()

def say_hi(name):
    print("Hello," + name)
    
say_hi("Farhan")

def say_hi(name,age):
    print("Hello," + name +" U are " + str(age))
    

def cube(num):
    return num*num*num
       
print(cube(5))





