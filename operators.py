# product_price = 5000
# delivery_charges= 100
# total_price = product_price + delivery_charges
# print("total price:", total_price)





# a=10
# b=3
# #assignment operators#

# print( a+b)
# print( a-b)
# print( a*b)
# print( a/b)
# print( a//b)
# print( a%b)
# print( a**b)

# student = 10
# group = 3

# print(student//group)
# print(student**group)



# followers = 100
# followers = followers+1
# print(followers)


# followers += 1
# print(followers)

# followers -=1
# print(followers)

# #comparision operators#

# save_password = "1234"
# entered_password = "1234"
# print(save_password == entered_password)

# save_password = "1234abc"
# entered_password = "1234abc"
# print(save_password == entered_password)

# save_password = "1234abcd"
# entered_password = "1234"
# print(save_password == entered_password)
# #######################33
# #logical operators#
# balance = 5000
# pin_correct = True
# if balance >= 1000 and pin_correct:
#     print("withdraw allowed")
# else:
#     print("failed")


# balance = 500
# pin_correct = True
# if balance >= 1000 and pin_correct:
#     print("withdraw allowed")
# else:
#     print("failed")


# ###billing clculator#######
# item_price = (int(input("enter the price")))
# quantity = (int(input("enter the quantity")))
# total = item_price*quantity
# print(total)

# product= input("enter product name: ")
# price= int(input("enter price: "))
# quantity= int(input("enter the quantity: "))
# discount= int(input("enter the discount price: "))
# total= price*quantity
# final_bill= total-discount
# print("product=",product)
# print("total amount=",total)
# print("final bill=",final_bill)

# #########conditions##########

# password = input("enter the password")
# if password== "admin@2005":
#     print("Welcome")
# else:
#     print("Wrong Password")

# age = 20
# if age >= 18:
#     print("eligible to vote")


# #####multiple conditions########

# marks=int(input("Enter the marks: "))
# if marks >=90:
#     print("A grade")
# elif marks >=75:
#     print("B grade")
# elif marks >=65:
#     print("C grade")
# else:
#     print("fail")


# marks=int(input("Enter the marks: "))
# if marks >=95:
#     print("10 cgpa")
# elif marks >=85:
#     print("9 cgpa")
# elif marks >=75:
#     print("8 cgpa")
# else:
#     print("fail")

# ######logical conditioning#########
# age=25
# salary=50000
# if age>=18 and salary>30000:
#     print("loan approved")

# day="sunday"
# if day=="saturday" or day=="sunday":
#     print(" not a holiday")

# login=True

# if not login:
#     print("login")

# #####exercise#######
# pin="admin@2005"
# amount=50000
# pin=input("Enterpin ")
# if pin==pin:
#      print("the pin is valid")
#      ask_amount=int(input("enter the amount to the withdraw "))
#      if ask_amount<=amount:
#         amount -=ask_amount
#         print("withdraw successfull")
#      else:
#         print("insufficient balance")
#      print("your balance:",amount)
# else:
#     print("the pin is invalid")


# ##########################
# ########loop###########

# for i in range(5):
#     print("send mail")
# users=["himani","chakrika","avinash"]
# for users in users:
#     print("message sent to",users)


# for i in range(2,6):
#     print(i)


# name="dhoni" 

# for ch in name:
#     print(ch)


# ############while############
# count = 1
# while count <=5:
#     print(count)
#     count +=1

# for i in range(10):
#     if i==5:
#         continue
#     print(i)

# for i in range(10):
#     if i==5:
#         break
#     print(i)


# password=""
# while password !="1234":
#     password=input("enter password:")
#     print("login successfull")


# student1="ram" 
# student2="sam"
# student3="rana"

student=[
    "ram",
    "sam",
    "rana"
]
student.append("himani")
student.remove("sam")
print(student)