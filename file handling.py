# f = open("mydemo.txt","w")
# f.write("this is first line\n")
# f.write("this is second line\n")
# f.close()

# f = open("mydemo.txt","r")
# print(f.read())

# f = open("mydemo.txt","a")
# f.write("this is third line\n")
# f.close()

# f = open("mydemo.txt","r")
# print(f.read())
#
# f = open("mydemo.txt","a")
# f.write("this is third line\n")
# f.close()
#
# f = open("mydemo.txt","r")
# print(f.read())
#
# f = open("mydemo.txt","r")
# for line in f:
#     print(line,end="")
# f.close()

# f = open("demo names.txt", "w")
# f.write(input("names")+"\n")
# f.write(input("birthdate")+"\n")
# f.close()
#
# f = open("demo names.txt","r")
# print(f.read())

# f = open("personal details.txt", "w")
# f.write("Name:"+input("enter your name = ")+"\n")
# f.write("Age:"+input("enter your age = ")+"\n")
# f.write(input("enter your birthdate = ")+"\n")
# f.write(input("enter your salary = ")+"\n")
# f.write(input("enter your blood group = ")+"\n")
# f.write(input("enter your company name = ")+"\n")
# f.write(input("enter your favorite colour = ")+"\n")
# f.write(input("enter your native city/village = ")+"\n")
# f.close()
#
# f = open("personal details.txt", "r")
# for line in f:
#     print(line, end="")
# print(f.read())
#
# name=input("enter your name =")
# print("hello",name,"it is your assistant")
#
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[::4])
# #run time polymor prism
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[0:4])

# employ id employ name employ contact employ department basic salary net salary
#
# f = open("employee details.txt", "w")
# f.write(("person inserting its detail = "+input("enter your employee id = ")+"\n"))
# f.write("employee id = "+input("enter employee id you want to search =")+"\n")
# f.write("employee name = "+input("enter the value of name = ")+"\n")
# f.write("employee contact = "+input("enter employee contact = ")+"\n")
# f.write("employee department = "+input("enter the value of employee department = ")+"\n")
# B=int(input("enter the value of B = "))
# f.write("the value of B = "+str(B) +"\n")
# ta=0.05*(B)
# da = 0.04*(ta+B)
# hra = 0.03*(ta+da+B)
# cca = 0.08*(ta+da+hra+B)
# pf = 0.1*(ta+da+hra+B)
# IT = 0.07*(ta+da+hra+B+cca-pf)
# NTS = (B+ta+da+hra+pf-cca-IT)
# f.write("the value of nts = "+str(NTS)+"\n")
# f.close()
#
# f = open("employee details.txt", "a")
# f.write("Thanks for visiting \n")
# f.close()
#
# f = open("employee details.txt" , "r")
# print(f.read())

# import os
# os.rename('employees details.txt','employee details.txt')
# os.remove('employee details.txt')
# os.mkdir('new')
# os.rmdir('new')