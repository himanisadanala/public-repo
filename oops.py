# ############oops#############
# class student:#class name
#     name="himani"#attribute
#     def study(self): #a represent a group of object
#         print("himani is studying")
# s1=student() #s1 is a object
# print(s1.name)
# s1.study() #study is a method

# class student:#class name
#     def detail(self): #a represent a group of object
#         print("had breakfast")
# s1=student() #s1 is a object
# s1.detail() #study is a method


# student.detail(s1)



######constructre####
# class student:
#     def __init__(self,name,age):#collector
#         self .name=name
#         self.age=age
# s1=student("himani",22)
# s2=student("yogesh",21)
# print(s1.name,s1.age)
# print(s2.name,s2.age)


# class bank:
#     def __init__(self,balance):
#         self.balance=balance

#     def check_balance(self):
#         print(self.balance)

# account=bank(50000)
# account.check_balance()

# class user():
#     def __init__(self,name):
#         self.name=name
#     def login(self):
#         print(self.name,"logged in")

# u1=user("himani")
# u1.login()

#######inheritence#########
# Parent class (Base class)
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating.")

# # Child class (Derived class) inheriting from Animal
# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} says Woof!")

# # Create an object of the child class
# my_dog = Dog("Buddy")

# # Call the inherited method from the parent class
# my_dog.eat()

# # Call the specific method from the child class
# my_dog.bark()


############
# class thatta:
#     def land(self):
#         print("thatta's land")

# class appa(thatta):
#     def house(self):
#         print("appa's house")

# class maga(appa):
#     def bike(self):
#         print("son has bike")

# obj=maga()
# obj.land()
# obj.house()
# obj.bike()

###################
# class appa:
#     def house(self):
#         print("appa has house")
# class amma:
#     def car(self):
#         print("amma has car")
# class maga(appa,amma):
#     def bike(self):
#         print("maga has bike")

# thirdclass=maga()

# thirdclass.house()
# thirdclass.car()
# thirdclass.bike()


############################

# class student:
#     def __init__(self,name):
#         self.name=name
    
#     def __str__(self):
#         return self.name
# s=student("king")
# print(s)

# def login(func):
#     def wrapper():
#         print("checking login")
#         func()
#     return wrapper
# @login
# def dashboard():
#     print("dashboard pages")
# dashboard()
#############
# def message(func):
#     def wrapper():
#         print("function started")

#         func()
#         print("function ended")

#     return wrapper
    
# @message
# def hello():
#     print("hello python")

# hello()



# import json
# student={
#     "name":"himani",
#     "age":22
# }
# data=json.dumps(student)
# print(data)

import requests
response=request.get(
    "https://api.github.com/users/python"
)
data=response.json()
print (data)