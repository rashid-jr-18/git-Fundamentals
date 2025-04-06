# def sad():
#     print("crying ..")
# def happy():
#     print("smilling...")
    
# def calm_down():
#     print("calm dowm")
    
# def feeling(func):
#     func()
#     return calm_down
    
# fun=feeling(happy)
# fun()

# higher oder fun takes funa s aarguments and prints the function


#inheritance

#super function


# class  employee():
    
    
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
#     def show_detail(self):
#         print(f'namee: {self.name} and salary is {self.salary}')
# class manager (employee):
#     def __init__(self,name,salary,depart):
#         super().__init__(name,salary)
#         self.depart=depart
#     def show_detail_man(self):
#         self.show_detail()
#         print(f'sdepartment: {self.depart}')
        
# e1= employee("rashid",50000)

# e1.show_detail()

# m1= manager("salaman",70000,"hr")
# m1.show_detail_man()



#single inheritance
# class animal:
#     def eat(self):
#         print("animal eats food")
# class dog(animal):
#     def bark(self):
#         print("dog is barking")
# d= dog()
# d.bark()
# d.eat()


# class user():
#     def logging(self):
#         print("logging in")
#     def register(self):
#         print("registering")

# # hierachical
# class students(user):
#     def greet_stud(self):
#         print("students greet")
# class faculty(user):
#     def greet_facul(self):
#         print("facuty greet")
#         #multilevel inheritance 
# class temp_faculty(faculty):
#     def temp_greet(self):
#         print("tem facultyb grret")
        
#         # multiple
# class students_faculty(students,faculty):
#     def study(self):
#         print("studying")
 
 
# # stud = students()
# # stud.greet_stud()  
# # stud.logging()
# # stud.register()


# # stud1= faculty()
# # stud1.register()
# # stud1.greet_facul()
# # stud1.logging()

# # stud2= temp_faculty()
# # stud2.greet_facul()
# # stud2.logging()
# # # stud2.register()
# # stud2.temp_greet()

# #multiple inheritance
# st=students_faculty()
# st.study()
# st.greet_facul()
# st.greet_stud()
# st.logging()
# st.register()

# method chaining   $  method overidding 
# class user:
#     def greet(self):
#         print("hello user")
        
#     def logi (self):
#         print("loggin ")
#         return self
#     def register(self):
#         print("register") 
#         return self       
# class students(user):
#     def greet(self):
#         print("hekko students")
        
# s=students()
# s.greet()

# #method chaining
# s.logi().register().logi()

#method overloading


class students:
    def mydetails(self):
        print("my details is none")
    def mydetails(self,name=None):
        print(f"my name is {name}")
s= students()
s.mydetails()
s.mydetails("rashid")


