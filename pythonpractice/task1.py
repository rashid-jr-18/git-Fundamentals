
#   calculator ///////////
# num1= int(input("Enter the no 1"))
# num2 = int (input ('enter the no 2'))

# operator =  input ("Enter the operator(+,-,*,%,/)")

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def div(a,b):
#     return a/b
# def multi(a,b):
#     return a*b
# def remainder(a,b):
#     return a%b

# if operator=="+":
#     print(add(num1,num2))
# elif operator=="-":
#     print(sub(num1,num2))
# elif operator=="*":
#     print(multi(num1,num2))
# elif operator=="/":
#     print(div(num1,num2))
# elif operator=="%":
#     print(remainder(num1,num2))
    
# else :
#     print("enter a valliid operator")

# students marks//////

# mark= int (input('enter your score out of 100'))
# if mark >=90:
#     print("grad A")
# elif mark>=80 and mark<=90:
#     print("grad b")
# elif  mark>=70 and mark<=80:
#     print("grad c")  
# elif  mark>=60 and mark<=70:
#     print("grad d")  
# else :
#     print ("fail")
     
     
# #palindrome check

# str= input("ENTER THE WORD")

# txt = str[::-1]
# #print(txt)
# if txt==str:
#     print("palindrome")
# else:
#     print("noy a palindrome")
    
 #odd or even 
 
 
# a= int(input("ENTER THE no"))

# if a%2==0:
#     print("even")
# else :
#     print("odd")
    
    
# prime no:

# a= int(input("enter the no"))
# count=0

# if a>1:
#     for i in range(2,a):
#         if a % i == 0:
#                 print(f"{a } is a  not prime no")
#                 break
#     else:
#         print(F"{a} is  a prime no")
                
# else:
#     print(f" {a} is not a prime no")
              
       # fibinocci 
       
# n= int(input("enter the no"))

# a,b=0,1
# count=0
# while count<n:
#     print(a)
#     temp=a
#     a=b
#     b= temp+b
#     n-=1


#iconic way fast method when doing in python     This is called tuple unpacking in Python


# n= int(input("enter the no"))

# a,b=0,1
# count=0
# while count<n:
#     print(a)
#     a,b=b,a+b 
#     n-=1

# 1 to 100 even no change to @


# for i in range(1,101):
#     if i%2==0:
#       print("@",end=" ")
#     else:
#         print(i,end=" "   )
        

        # user details
        
# name= input("Enter the name")
# age= input("enter the age ")
# city = input ("enter the city")

# def userdetails(name,age,city):
#        print(f"username is{name} and age{age} and their ciy{city}")
       
# userdetails(name,age,city)

#  retrive the keys and value from dict

# user={
#        "name":"rashid",
#        'age': 23,
#        "city": "sattir"
#        }


# keys_s=user.values()
# print(keys_s)

# print(user['age'])
    
    
    
    # collection iterate each elments in list
    
# num=[1,2,3,4,5]
# for i in num:
#   print(i**2)

# s_num=[]
# for  i in num:
#        s_num.append(i**2)
       
# print(s_num)



       #  lambda  function task 
# n=(2,3,4,5,6)
# even= filter(lambda x:x %2 !=0,n)
# print(list(even))
# print(even)

# a= [1,2,3,4]
# b = map(lambda x: x *2,a)
# print(list(b))

# from functools import reduce

# a= [1,2,3,4,5]
# b= reduce(lambda x ,y : x*y,a)
# print(b)


# from functools import lru_cache

# num=lambda n:n if n <=1 else num(n-1)+num(n-2)
# for i in range(8):
#     print(num(i),end=" ")

# fact = lambda n : 1 if n==0 else n * fact(n-1)

# print(fact(5))


# num = lambda s : s[::-1]
# print(num("hello"))


n= lambda n: int(str(n)[::-1])

print(n(123456))
  
  
