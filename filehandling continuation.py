# employ id employ name employ contact employ department basic salary net salary
#
f = open("employee details.txt", "w")
f.write("employee id="+input("enter your employee id =")+"\n")
f.write("employee name="+input("enter the value of name=")+"\n")
f.write("employee contact="+input("enter employee contact=")+"\n")
f.write("employee department="+input("enter the value of employee department=")+"\n")
B=int(input("enter the value of B="))
f.write("the value of B="+str(B))
ta=0.05*(B)
da = 0.04*(ta+B)
hra = 0.03*(ta+da+B)
cca = 0.08*(ta+da+hra+B)
pf = 0.1*(ta+da+hra+B)
IT = 0.07*(ta+da+hra+B+cca-pf)
NTS = (B+ta+da+hra+pf-cca-IT)
f.write("the value of nts="+str(NTS))
f.close()

f = open("employee details.txt", "r")
print(f.read())

# import os
# os.rename('employee details.txt','employees details.txt')
# os.remove('employees details.txt')
# os.mkdir('new')
# os.rmdir('new')

# print("-------------------------------------------------------------------------")
# print("						        Menu Card")
# print("-------------------------------------------------------------------------")
# print("\n BEVARAGES							 26 Dal Fry................ 140.00")
# print("----------------------------------	 27 Dal Makhani............ 150.00")
# print(" 1 Regular Tea............. 20.00	 28 Dal Tadka.............. 150.00")
# print(" 2 Masala Tea.............. 25.00")
# print(" 3 Coffee.................. 25.00	 ROTI")
# print(" 4 Cold Drink.............. 25.00	 ----------------------------------")
# print(" 5 Bread Butter............ 30.00	 29 Plain Roti.............. 15.00")
# print(" 6 Bread Jam............... 30.00	 30 Butter Roti............. 15.00")
# print(" 7 Veg. Sandwich........... 50.00	 31 Tandoori Roti........... 20.00")
# print(" 8 Veg. Toast Sandwich..... 50.00	 32 Butter Naan............. 20.00")
# print(" 9 Cheese Toast Sandwich... 70.00")
# print(" 10 Grilled Sandwich........ 70.00	 RICE")
# print("									 ----------------------------------")
# print(" SOUPS								 33 Plain Rice.............. 90.00")
# print("----------------------------------	 34 Jeera Rice.............. 90.00")
# print(" 11 Tomato Soup............ 110.00	 35 Veg Pulao.............. 110.00")
# print(" 12 Hot & Sour............. 110.00	 36 Peas Pulao............. 110.00")
# print(" 13 Veg. Noodle Soup....... 110.00")
# print(" 14 Sweet Corn............. 110.00	 SOUTH INDIAN")
# print(" 15 Veg. Munchow........... 110.00	 ----------------------------------")
# print("									 37 Plain Dosa............. 100.00")
# print(" MAIN COURSE						 38 Onion Dosa............. 110.00")
# print("----------------------------------	 39 Masala Dosa............ 130.00")
# print(" 16 Shahi Paneer........... 110.00	 40 Paneer Dosa............ 130.00")
# print(" 17 Kadai Paneer........... 110.00	 41 Rice Idli.............. 130.00")
# print(" 18 Handi Paneer........... 120.00	 42 Sambhar Vada........... 140.00")
# print(" 19 Palak Paneer........... 120.00")
# print(" 20 Chilli Paneer.......... 140.00	 ICE CREAM")
# print(" 21 Matar Mushroom......... 140.00	 ----------------------------------")
# print(" 22 Mix Veg................ 140.00	 43 Vanilla................. 60.00")
# print(" 23 Jeera Aloo............. 140.00	 44 Strawberry.............. 60.00")
# print(" 24 Malai Kofta............ 140.00	 45 Pineapple............... 60.00")
# print(" 25 Aloo Matar............. 140.00	 46 Butter Scotch........... 60.00")
# print("Press 0 to end ")

# f = open("menu.txt", "w")
# TN = int(input("Enter your TN="))
# if (TN>25):
#     print("it is invalid")
# print("Select 1 for bread")
# print("Select 2 for starter")
# print("Select 3 for Shahi Sabji")
# print("Select 4 for Colddrinks")
# print("Select 5 for Salad")
# f.write("TN="+str(TN)+"\n")
# n= int(input("Enter value in n\n"))
# f.write("n="+str(n)+"\n")
# for n in range(n,6):
#     if (n==1):
#         print("Select 1 for normal_bread= 10,\nSelect 2 for butter_bread= 20,\nSelect 3 for khamiri bread=30,\n"
#               "select 4 for garlic bread= 40, \n")
#         bread = int(input("the bread you have chosen=:\n"))
#         f.write("bread chosen="+str(bread)+"\n")
#         if(bread==1):
#             bread = 10
#             f.write("10RS")
#         elif(bread==2):
#             roties = 20
#             f.write("20RS")
#         elif(bread==3):
#             bread = 30
#             f.write("30rs")
#         else:
#             bread = 40
#             f.write("40rs")
#             # return n
#     for n in range(n,6):
#         if(n==2):
#             print("select 1 for panneer tikka=100, \nselect 2 for malai paneer=140, \nselect 3 for soya chapp=110")
#             starter = int(input("the starter chosen="+"\n"))
#             f.write("starter chosen="+str(starter)+"\n")
#             if(starter==1):
#                 starter = 120
#                 f.write("starter="+str(120))
#             elif(starter==2):
#                 starter = 140
#                 f.write("starter="+str(140))
#             else:
#                 starter = 110
#                 f.write("starter="+str(110))
#     for n in range(n,6):
#         if (n==3):
#             print("select 1 for paneer tikka butter masala=210, \nselect 2 for paneer bhurji=230, \nselect 3 for mix veg=180, \n"
#             "select 4 for tawa chapp=190, \n")
#             shahi_sabji = int(input("shahi_sabji you have chosen=")+"\n")
#             f.write("shahi_sabji you have chosen="+str(shahi_sabji)+"\n")
#             if(shahi_sabji==1):
#                shahi_sabji = 210
#                f.write("shahi_sabji="+str(210))
#             elif(shahi_sabji==2):
#                shahi_sabji = 230
#                f.write("shahi_sabji="+str(230))
#             elif(shahi_sabji==3):
#                 shahi_sabji = 180
#                 f.write("shahi_sabji="+str(180))
#             else:
#                 shahi_sabji = 190
#                 f.write("shahi_sabji="+str(190))
#     for n in range(n,6):
#         if(n==4):
#             print("select 1 for coca_cola(200m), \nselect 2 for thumps_up(200ml), \nselect 3 for frooti(175ml), \nselect 4 for chhas(300ml)")
#             colddrink=int(input("the drink you have chosen="))
#             f.write("cloddrink you have chosen"+str(colddrink)+"\n")
#             if(n==1):
#                 colddrink = 30
#                 f.write("coca_cola="+str(30))
#             elif(n==2):
#                 colddrink = 30
#                 f.write("thumps_up="+str(30))
#             elif(n==3):
#                 colddrink = 30
#                 f.write("frooti="+str(30))
#             else:
#                 colddrink = 35
#                 f.write("chhas="+str(35))
#     for n in  range(n,6):
#         if(n==5):
#             print("selct 1 for vegetable salad, \nselect 2 for humus salad, \nselect 3 for colslo salad, \n")
#             salad=int(input("the salad you have chosen=")+"\n")
#             f.write("salad you have chosen"+str(salad)+"\n")
#             if n==1:
#                 salad=45
#                 f.write("salad="+str(salad)+"\n")
#             elif n==2:
#                 salad=65
#                 f.write("salad="+str(salad)+"\n")
#             else:
#                 salad=75
#                 f.write("salad="+str(salad)+"\n")

# class Food(object):
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def getprice(self):
#         return self.price
#     def __str__(self):
#         return self.name + ' : ' + str(self.getprice())
# def buildmenu(names, costs):
#     menu = []
#     for i in range(len(names)):
#         menu.append(Food(names[i], costs[i]))
#     return menu
# names = ['Coffee', 'Tea', 'Pizza', 'Burger', 'Fries', 'Apple', 'Donut', 'Cake']
# costs = [250, 150, 180, 70, 65, 55, 120, 350]
# Foods = buildmenu(names, costs)
# n = 1
# for el in Foods:
#     print(n, '. ', el)
#     n = n + 1