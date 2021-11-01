# class animal:
#     def speaking(self):
#         print("animal speaking")
# #child class dog inherits the base class animal
# class dog(animal):
#     def barking(self):
#         print("dog barking")
# d = dog()
# d.barking()
# d.speaking()


# class calculation1:
#     def addition(self,a,b):
#         return a+b
# class calculation2:
#     def multiplication(self,a,b):
#         return a*b
# class derived(calculation1,calculation2):
#     def division(self,a,b):
#         return a/b
# d = derived()
# print(d.addition(10,20))
# print(d.multiplication(10,20))
# print(d.division(10,20))

# class animal:
#     def speaking(self):
#         print("animal speaking")
# #the child class dog inherits the base class animal
# class dog(animal):
#     def barking(self):
#         print("dog barking")
# #the child class puppy inherits another child class dog
# class puppy(dog):
#     def eating(self):
#         print("puppy eating bread")
# d = puppy()
# d.barking()
# d.speaking()
# d.eating()

# basic_salary=int(input("basic salary="))
# class net_salary:
#     def net_salary(self):
#         return basic_salary
# class taxes(net_salary):
#     def taxes(self):
#         return taxes
#     DA=0.333*(basic_salary)
#     class taxes1(net_salary):
#         def taxes1(self):
#             return taxes
#     HRA=0.15*(basic_salary+DA)
#     class taxes2 (net_salary):
#         def taxes2(self):
#             return taxes
#     CCA=0.0899*(basic_salary+DA+HRA)
#     class taxes3(net_salary):
#         def taxes3(self):
#             return taxes
#     PF=0.079*(basic_salary+DA+HRA+CCA)
#     class taxes4(net_salary):
#         def taxes4(self):
#             return taxes
#     INCOME_TAX=0.1*(basic_salary+DA+HRA+CCA)
#     class taxes5(net_salary):
#         def taxes5(self):
#             return taxes
#     net_salary=basic_salary+DA+HRA+CCA-PF-INCOME_TAX
#     print("net_salary=",net_salary)
# d=taxes()
# print(d.taxes())