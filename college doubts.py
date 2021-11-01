# h=6
# m=21
# if h>7:
#     print("invalid input")
# elif h>=5 and h<=7 :
#     amount=200
#     h=h-5
#     total=h*50+m+amount
# elif h<5:
#     total=h*50+m
# print(total)
#
# hours=6
# minutes=21
# amount=0
# if hours >=5 :
#     amount += 1
#     hours +=1
#     amount = amount+(hours)*50
#     amount = amount+(minutes)*1
# print (amount)

# h=6
# m=21
# if h==5:
#     amount=(200+m*1)
#     print(amount)
# elif h>7:
#     print("hours exceded")
# elif h>5:
#     amount=int((h*50+m*1)-50)
#     print(amount)
# elif h<7:
#     amount=(h*50+m*1)
#     print(amount)

# import math
# def countRec(choc, wrap):
#     if (choc < wrap):
#         return 0
#     newChoc = choc / wrap
#     return newChoc + countRec(newChoc + choc % wrap, wrap)
# def countMaxChoco(money, price, wrap):
#     choc = money / price
#     return math.floor(choc + countRec(choc, wrap))
# money = 15
# price = 1
# wrap = 3
# print(countMaxChoco(money, price, wrap))

# fg=int(input())
# physics=int(input())
# chemistry=int(input())
# mathematics=int(input())
# total_marks=mathematics+physics+chemistry
# average=total_marks/3
# if (physics<0 or chemistry<0 or mathematics<0):
#     print("invalid input")
# elif average>98:
#     print("qualifiied")
# else:
#      print("notqualified")

# pan=input()
# if len(pan)==10:
#     if (pan[0].isdigit()==True) and (pan[1].isupper()==True) and (pan[2].isupper()==True) and (pan[3].isupper()==True) and (pan[4].isdigit()==True):
#         print("valid")
#     else:
#         print("invalid")
# else:
#     print("Invalid")