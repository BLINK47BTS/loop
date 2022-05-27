'''x=int(input("enter value"))
a=1
while a<=x:
    if a%2==0:
        print(a,"is even")
    else:
        print(a,"is odd")
    a+=1
    '''

'''a=1
while a<5:
  print(a,"\n",a,a+1)
  a+=1
  '''
  
'''a=1
while a<=9:
    b=1
    while b<=9:
        print(b)
        b+=1
    a+=1
    '''
    
'''a=7
b=10
print(a-(-b))'''

# year = int(input("Input a year: "))
# if (year % 4== 0):
#     leap_year = True
# else:
#     leap_year = False
# month = int(input("Input a month [1-12]: "))
# if month<=12:
#   if month in (1, 3, 5, 7, 8, 10, 12):
#     month_length = 31
#   elif month == 2:
#       if leap_year:
#         month_length = 29
#       else:
#         month_length = 28
#   else:
#     month_length = 30
# # else:
# #   print("re enter month")
#   day = int(input("Input a day [1-31]: "))
#   if day<=31:
#     if day < month_length:
#       day += 1
#     else:
#       day = 1
#       if month == 12:
#           month = 1
#           year += 1
#       else:
#           month += 1
#   else:
#     print('re enter date')
# else:
#   print("re enter month")
  
# print("The next date is [yyyy-mm-dd]",day,month,year)


# name="my name is nisha"
# print(len(name)
'''a="python is easy"
print(len("a))'''

'''for i in range(1,5,3):
  print(i*'l')'''
'''d="welcome to my blog"
print(d[14])
print(d[-4])  
'#print(len(d))
print(d.index('b'))'''

'''a=(input("month name starting 3 letters ;- "))
if a in ('jan','jul','mar','may','oct','dec','jul','JUL','JAN','DEC','MAR','OCT','MAY','JULY','AUG'):
  print(a, "has 31 days")
elif a=='feb' or a=='february':
  print(a, 'has 28 days')
elif a in ('apr','jun','sep','nov','NOV','JUN','SEP','APR'):
  print(a, "has 30 days")
else:
  print("enter month")
'''

'''a=int(input("angle 1 :- "))
b=int(input("angle 2 :- "))
c=int(input("angle 3 :- "))
if a==60 and b==60 and c==60:
  print("it is a equilateral triangle")
elif a==c or b==c or a==b and (a+b+c==180):
  print("an isosceles triangle")
elif a+b+c==180 and a!=b!=c:
  print("scalene triangle")
else:
  print("not a triangle")'''


'''x=int(input("enter your number"))
if(x>=1500 and x<= 2700):
  print("true")
  if(x%7==0 and x%5==0):
      print("divisible")
  else:
      print("save water")
else:
  print("all")'''
  
  
'''quantity=int(input(" quantity :"))
cost=quantity*45
if cost>=1000:
  print(cost-cost*0.10)
else:
  print(cost)
  
cost=int(input("price : "))
if cost>100000:
  print(cost*0.15+cost,"tax")
elif cost>50000 and cost<=100000:
  print(cost*0.10+cost,'tax')
elif cost<=50000:
  print(cost*0.5+cost,"tax")
  
city=input("city : ")
if city=="Delhi" or city=='delhi':
  print("Red Fort")
elif city=="Agra" or city=='agra':
  print("Taj Mahal")
elif city=="Jaipur" or 'jaipur':
  print("Jal Mahal")
else:
  print("not found")'''
  
'''a=int(input("no 1 : "))
b=int(input("no 2 : "))
c=int(input("no 3 ; "))'''
'''if a>b:
  if a<c:
    print(a)
elif b<c:
    print(b)
else:
    print(c)
   '''
'''if (a>b and a<c) or (a>c and a<b):
  print(a)
elif (b>a and b<c) or (b>c and b<a):
  print(b)
else:
  print(c)'''
  
'''a=int(input("star"))
i=1
while i<=a:
  print('*'+" "*i+'*')
  i+=1'''
  
"""a=int(input("table :- "))
i=1
while i<=10:
  print(a,"*",i,"=",a*i)
  i+=1"""
  
"""a=int(input("num :- "))
i=1
while i<=a:
  print('*'*i)
  i+=1"""
  
"""a=int(input("star"))
i=1
while i<=a:
  print('*'+" "*i+'*')
  i+=1"""
  
# a = int(input("Enter a num: "))

# i = 1
# while i<=a:
#   print("* "*i)
#   i+=1

# for hollow triangle
# a = int(input("Enter a num: "))
# i = 0
# print("*")
# while i<a-2:
#   print("*"+" "*i+"*")
#   i+=1
# print("*"*(i+2))

# a=int(input("num : "))
# i=0
# while i<a:
#   if i==0:
#     print("*")
#   elif i==a-1:
#     print("*"*(i+1))
#   else:
#     print("*"+" "*(i-1)+"*")
#   i+=1

# equilateral triangle
# a = int(input("Enter a num: "))
# c = a
# i = 1
# while i<=a:
#   print(" "*c+"* "*i)
#   i+=1
#   c-=1
    
# print("88"+"helo "*0)

#diamond
# a = int(input("Enter a num: "))
# b = a
# i = 1
# print("*")
# while i<=a:
#     print(" "*b+"* "*i)
#     i+=1
#     b-=1
# while i>0:
#     print(" "*b+"* "*i)
#     i-=1
#     b+=1

# y=int(input("no : "))
# i=0
# j=i
# while i<y:
#   print(j,j+i)
#   i+=1

#digit=input("digit : ")
#print(digit[-3:])

# num=int(input("no  : "))
# rows=0
# while rows<num:
#   star=rows+1
#   while star>0:
#     print("*",end=" ")
#     star-=1
#   print()
#   rows+=1

# Q1 factorial
# a=int(input("number : "))
# i=1
# fac=1
# while i<=a:
#   fac*=i
#   print(fac)
#   i+=1
# print(a,"!","=",fac,end="")
# Q2 fibonacci series
#0 1 1 2 5
# a=int(input("number :- "))
# i=0
# while i<a:
#   print(i+1)
#   i+=1
# Q3 armstrong number
# 1^3+3^3+5^3=153
# a=int(input("num : "))
# i=1
# while i<=a:
#   if a%2==1:
#     print(i**3,"+")
#     i+=2
# Q4 decimal to binary using input
# t=int(input("number : "))
# print(bin(t))

# a=int(input("enter a number"))
# if a<=10 and a>=0:
#   if a%2==0:
#     print(a**2)
#   else:
#     print(a**3)
# else:
#   print("re-enter value")

# a="56.67"
# print(int(float(a)))

# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%
# a=int(input("salary : "))
# if a<=10000:
#   print(a*0.2,"HRA",a*0.8,"DA",a+a*0.2+a*0.8,"GROSS SALARY")
# elif a<=20000:
#   print(a*0.25,"HRA",a*0.9,"DA",a+a*0.25+a*0.9,"GROSS SALARY")

# a="internet"
# c="20"
# b="20.98"
# print(int(c)+int(c))

# a="internet"
# c="20"
# b="20.98"
# print(a,c)

# a="internet"
# c="20"
# b="20.98"
# print(a*20)

# a="honey"
# A="honey"
# b=20
# B=21
# c=21.7
# C=67.7
# d=13+5j
# D=34-6j
# e="True"
# E="False"
# print(a)
# print(A)
# print(b)
# print(B)
# print(c)
# print(C)
# print(d)
# print(D)
# print(e)
# print(E)

# NUM_1=20
# num1=21
# NUM1="bhawna"
# print(NUM_1,num1,NUM1)

# a=int(input("marks : "))
# if a<25:
#   print("F GRADE")
# elif a>25 and a<=45:
#   print("E GRADE")
# elif a>45 and a<=50:
#   print("D GRADE")
# elif a>50 and a<=60:
#   print("C GRADE")
# elif a>60 and a<=80:
#   print("B GRADE")
# else:
#   print("A GRADE")

# a=int(input("age : "))
# b=int(input("age : "))
# c=int(input("age : "))
# if a>b and a>c:
#   print(a,"oldest")
# elif b>c and b>a:
#   print(b,"is oldest")
# elif c>a and c>b:
#   print(c,"is oldest")
# if a<b and a<c:
#   print(a, "is youngest")
# elif b<a and b<c:
#   print(b,"is youngest")
# else:
#   print(c,"is youngest")

# a=10
# b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a//b)
# print(a%b)

# x=int(input("enter your  number:"))
# y=int(input("enter your number:"))
# z=input("operator:")
# if z=="+" or z=="add":
#   print(x+y)
# elif z=="-" or z=="subtract":
#   print(x-y)
# elif z=="*" or z=="multiply":
#   print(x*y)
# elif z=="/" or z=="divided":
#   print(x/y)

# n=int(input("num : "))
# i=1
# while i<=n:
#   if i==1:
#     print(i,end="")
#   elif i%2==0:
#     print("+",i**2,end="")
#   elif i%2==1:
#     print("-",i**2,end="")
#   i+=1

# a=int(input("no. of rows : "))
# i=1
# while i<=a:
#   print(i*":)")
#   i+=1

# n=int(input("n ; "))
# i=2
# print("1",end=" ")
# while i<=n:
#   if i%2==0:
#     print("+",i**2,end=" ")
#   else:
#     print(-i**2,end=" ")
#   i+=1

# steps
# i=1
# while i<=5:
#   print(" "*i+"*"*i)
#   i+=1

# i=1
# while i<4:
#   j=1
#   while j<4:
#     print(j*"*", end='')
#     j+=1
#   i+=1
#   print()

# i=1
# while i<=5:
#   j=1 
#   while j<=i:
#     print(i+j-1,end="")
#     j+=1
#   i+=1
#   print()

# number and star pattern
# n=int(input("num : "))
# i=1
# while i<=n:
#   if i%2==1:
#     print("*"*i,end="")
#     j=1
#   else:
#     while j<=i:
#       print(j,end="")
#       j+=1
#   print()
#   i+=1
# or with space
# n=int(input("num : "))
# i=1
# while i<=n:
#   if i%2==1:
#     print("*"*i)
#     j=1
#   else:
#     while j<=i:
#       print(j,end="")
#       j+=1
#   print()
#   i+=1 

#atm code
# print("Welcome to Bank of India")
# print("please insert your card")
# print("card has been processing")
# print("HINDI")
# print("GUJRATI")
# print("MARATHI")
# print("ENGLISH")
# lan=input("select language : ")
# if lan=="english" or lan=="hindi" or lan=="marathi" or lan=="gujrati":
#   print(lan)
# else:
#   print("invalid language")

# pin=int(input("Enter your 4 digit pin number: "))
# if pin<=9999:
#   print("xxxx")
# # else:
# #   print("not valid pin")
  
#   print("choose account")
#   print("JOINT ACCOUNT")
#   print("CURRENT ACCOUNT")
#   print("SAVINGS ACCOUNT")
#   acc=input("choose account : ")
#   if acc=="SAVINGS ACCOUNT":
#     print(acc)
#   elif acc=="JOINT ACCOUNT":
#     print(acc)
#   elif acc=="CURRENT ACCOUNT":
#     print(acc)
  
#   print("Withdraw")
#   print("Balance Enquiry")
#   print("Deposit")
#   transaction=input('choose transaction : ')
#   if (transaction=='Withdraw') or (transaction=='Deposit') or (transaction=='Balance Enquiry'):
#     print(transaction)
#     if transaction=='Withdraw':
#       amount=int(input("amount : "))
#       if amount<=10000:
#         print(10000-amount,"Current Balance")
#       else:
#         print("not sufficient balance")
#         print("transaction in process")
#         print(10000-amount)
#     elif transaction=='Balance Enquiry':
#       print("your balance is 10000")
#     elif transaction=='Deposit':
#       deposit=int(input("deposit amount : "))
#       print('amount has been deposited')
#       print(10000+deposit,"Current Balance")
#   else:
#     print('not valid transaction')

#   recipt=input("recipt : ")  
#   if recipt=='no':
#     print("THANK YOU")
#   elif recipt=='yes':
#     print("take your recipt",'\n','THANK YOU')
# else:
#   print("invalid")

# library code
# print("welcome to the WORLD OF BOOKS")
# s=int(input("S NO. : "))
# name=input("Name : ")
# book=input("Book Name : ")
# date=input("Date : ")
# days=int(input("No. of days : "))
# if days<=5:
#   print(" No Extra Charges")
# elif days>5 and days<=10:
#   print(days*5,"Extra charge of Rs.5/day")
# elif days>10:
#   print(days*10,"Extra charges of Rs.10/day")

# table from user
# a=int(input("enter a no. "))
# print(a,"*",1,"=",a*1)
# print(a,"*",2,"=",a*2)
# print(a,"*",3,"=",a*3)
# print(a,"*",4,"=",a*4)
# print(a,"*",5,"=",a*5)
# print(a,"*",6,"=",a*6)
# print(a,"*",7,"=",a*7)
# print(a,"*",8,"=",a*8)
# print(a,"*",9,"=",a*9)
# print(a,"*",10,"=",a*10)

# moth,day input and o/p is season
# month=input("Month name:- ")
# days=int(input("No. of days in the month:- "))
# if month>="jan" and month<="dec":
#   print("yes")

# gender=input("M or F : ")
# age=int(input("age : "))
# days=int(input("no. of days : "))
# if gender=='M':
#   if age>=18 and age<30:
#     # wage=700 
#     print(days*700,"wages")
#   elif age>=30 and age<=40:
#     # wage=800 
#     print(days*800,'wages')
#   else:
#     print("enter appropriate age")
# # elif gender=='F':
# if gender=='F':
#   if age>=18 and age<30:
#     # wage=750
#     print(days*750,'wages')
#   elif age>=30 and age<=40:
#     # wage=850
#     print(days*850,'wages')
#   else:
#     print("enter appropriate age")
# # print(days*wage)

# equilateral hollow triangle
# n=int(input("rows : ")) 
# i=1
# while i<=n: 
#   if i==1: 
#     print("@"*(n-1)+"*")
#   elif i==n: 
#     print("*@" * i)
#   else: 
#     print(" @"*(n-i) + "*" + "@" * (2*i-3) + "*")
#   i+=1

# a=input("password : ")
# if len(a)>=8:
#   if ((a[0]) in "@","!","#","$","%","^","&","*","(",")","-","_"):
#     #   print('o')
#     # else:
#     #   print("weak password")
#     if (a>="a" and a<="z"):
#     #   print('p')
#     # else:
#     #   print("weak")  
#       if (a>="A" and a<="Z"):
#     #   print('l')
#     # else:
#     #   print("week")
#         if (a>="0" and a<="9"):
#           print("the strong password",a) 
# else:
#     print("weak password")

# unit=int(input("unit of electricity : "))
# if unit<=100:
#   print("no charge")
# elif unit>100 and unit<200:
#   charge=(unit-100)*5
#   print(charge,"charges")
# elif unit>=200:
#   y=unit-300
#   h=(unit-200)*10
#   u=y*10
#   print(u+h)

#hollow triangle 
# row=1
# while row<=4:
#   col=1
#   while col<=7:
#     if row==4 or row+col==5 or col-row==3:
#       print("*",end=" ")
#     else:
#       print(end="  ")
#     col+=1
#   row+=1
#   print()

# temple cap
# row=1
# while row<=5:
#   col=1
#   while col<=9:
#     if row==4 or row+col==6 or col-row==4:
#       print("*",end=" ")
#     else:
#       print(end="  ")
#     col+=1
#   row+=1
#   print()

# row=1
# while row<=5:
#   col=1
#   while col<=9:
#     if row==5 or row+col==6 or col-row==4:
#       print("*",end=" ")
#     else:
#       print(end="  ")
#     col+=1
#   row+=1
#   print()


#hollow right triangle
#a = int(input("Enter a num: "))
# i = 0
# print("*")
# while i<(a-2):
#   print("*"+"  "*i+"*")
#   i+=1
# print("* "*(i+2))

#equilateral triangle hollow
# n=int(input("enter row no.:  "))
# i =0
# while i<(n):
#   if i==0:
#     print(" "*(n-1)+"*")
#   elif i==(n-1):
#     print("* "*(n))
#   else:
#     print(" "*(n-i-1)+"*"+"#"*((i*2)-1)+"*")
#   i+=1

#  for hollow pyramid

# rows=int(input("enter rows "))
# col=2*rows-1
# mid=col//2
# i=1
# while i<=rows:
#   j=1
#   while j<=col:
#     if i==rows or i+j==mid+2 or j-i==mid:
#       print("*",end="")
#     else:
#       print(end=" ")
#     j+=1
#   i+=1
#   print()

# a = int(input("Enter a num: "))
# b = a
# i = 1
# print("*")
# while i<=a:
#     print(" "*b+"* "*i)
#     i+=1
#     b-=1  


# hackathon
# if else atm code
# print("Welcome to MY BANK")
# print("please insert your card")
# print("card is processing")
# print("Hindi")
# print("Assamee")
# print("Tamil")
# print("English")
# language=input("select language : ")
# if language in ("Hindi","Assamee","English","Tamil"):
#   print(language)
# else:
#   print("invalid option")

# pin=int(input("Enter your 4 digit pin number: "))
# if pin<=9999:
#   print("xxxx")

#   print("choose account")
#   print("Joint account")
#   print("Current account")
#   print("Savings account")
  
#   account=input("choose account : ")
#   if account=="Savings account":
#     print(account)
#   elif account=="Joint account":
#     print(account)
#   elif account=="Current account":
#     print(account)
  
#   print("Withdraw")
#   print("Change pin")
#   print("Deposit")
#   transaction=input('choose transaction : ')
#   if (transaction=='Withdraw') or (transaction=='Change pin') or (transaction=='Deposit'):
#     print(transaction)
#     if transaction=='Withdraw':
#       amount=int(input("amount : "))
#       if amount<=10000:
#         print(10000-amount,"Current Balance")
#       else:
#         print("not sufficient balance")
#         print("transaction in process")
#         print(10000-amount)
#     elif transaction=='Change pin':
#       print("Type your pin")
#       pin=int(input("Enter pin : "))
#       if pin<=9999:
#         print("xxxx")
#         print("Enter your OTP")
#         OTP=int(input("OTP : "))
#         if OTP<=9999:
#           print("xxxx")
#           print("OTP verified")
#           print("Enter new pin")
#           newpin=int(input("New pin here : "))
#           print("pin changed successfully")
#       else:
#         print("try again")
#     elif transaction=='Deposit':
#       deposit=int(input("deposit amount : "))
#       print('amount has been deposited')
#       print(10000+deposit,"Current Balance")
#   else:
#     print('not valid transaction')

#   recipt=input("recipt : ")  
#   if recipt=='no':
#     print("THANK YOU")
#   elif recipt=='yes':
#     print("take your recipt",'\n','THANK YOU')
# else:
#   print("not valid pin")

#electricity bill
# unit=int(input("unit of electricity : "))
# if unit<=100:
#   print("no charge")
# elif unit>100 and unit<=200:
#   charge=(unit-100)*5
#   print(charge,"charges")
# elif unit>200:
#   y=unit-300
#   h=(unit-200)*10
#   u=y*10
#   print(u+h,"total charges")

# last digit divisible by 3 or not
# a=int(input("number : "))
# b=a%10
# print(b,"last digit")
# if b%3==0:
#   print("divisible by 3")
# else:
#   print("not divisible by 3")

#attendance
# classes=int(input("no. of classes held : "))
# attendance=int(input("no.of classes attended : "))
# percentage=(classes/attendance*75/100)*75
# if percentage==75 or percentage>75:
#   print(percentage,"allowed to sit in exam")
# else:
#   print(percentage,"not allowed to sit in exam")

# bonus of 5%
# salary=int(input("enter your salary here : "))
# service=int(input("years of service : "))
# if service>=5:
#   print(salary*0.5,"bonus")
# else:
#   print("no bonus")

#library code
# print("welcome to the MY WORLD OF BOOKS")
# s=int(input("S NO. : "))
# name=input("Name : ")
# book=input("Book Name : ")
# date=input("Date : ")
# days=int(input("No. of days : "))
# if days<=5:
#   print(days*2, "Extra charge of Rs.2/day")
# elif days>5 and days<=10:
#   print(days*3,"Extra charge of Rs.3/day")
# elif days>10 and days<=15:
#   print(days*4,"Extra charges of Rs.4/day")
# else:
#   print(days*5,"Extra charges of Rs.5/day")

#kilometeres
# distance=int(input("distance in Kms : "))
# if distance<=10:
#   print(distance*11,"bill")
# elif distance>10 and distance<=100:
#   print(distance*10,"bill")
# elif distance>100:
#   print(distance*9,"bill")

# 75% attendance
# total=int(input("total working days : "))
# absent=int(input("no. of days for absent : "))
# present=total-absent
# percentage=(present/total*75/100)*100
# if percentage>=75:
#   print(percentage,"able to sit in exam")
# else:
#   print(percentage,"not able to sit in exam")

# three digit or not
# a=int(input("enter a no. : "))
# if a>100 and a<1000:
#   print(a,"three digit no.")
# else:
#   print(a,"is not a three digit no. ")

# doubt ques
# i=3
# j=5
# k=7
# if i>j:
#   if j>k:
#     i=j
#   else:
#     j=k
# else:
#   if j>k:
#     j=i
#   else:
#     i=k
# print(i,j,k)

# factorial
# a=int(input("number : "))
# i=1
# f=1
# while f<=a:
#   f*=i
#   if a==1:
#     print(a)
#   elif a>1:
#     print(a,"*",end=" ")
#   a-=1
# f+=1

# n=input("python : ")
# i=1
# while i<=n:
#   if i%2==1:
#     print("python"*i,end="")
#     j=1
#   else:
#     while j<=i:
#       print(" ",end="")
#       j+=1
#   print()
#   i+=1

#Q6
# a=int(input("no. : "))
# b=a%10
# c=b%2
# i=2
# while i<=a:
#   if c==0:
#     print("divisible")
#   else:
#     print("not divisible")
#   break

# Q3 weird
# a=int(input("no. : "))
# i=1
# while i<=a:
#   if a%2==1:
#     print("weird")
#   elif a%2==0:
#     if a>=2 and a<=5:
#       print("not weird")
#     elif a>=6 and a<=20:
#       print("weird")
#     else:
#       print("not weird")
#   break

# Q6 challenge     
# i=1
# while i<11:
#   j=1
#   print(int(input("no: ")))
#   i+=1
#   j+=1

#Q3 number is prime or not
# n=int(input("num : "))
# i=n
# while i<=n:
#   if n==1:
#     print("nor prime nor composite")
#   elif n==2 or n==3 or n==5 or n==7:
#     print("prime no.")
#   elif n%2==0 or n%3==0 or n%5==0 or n%7==0:
#     print("not prime")
#   else:
#     print("prime number")
#   i+=1

# Q1 f) consecutive no.
# a=int(input("number : "))
# i=1
# while i<=a:
#   print(i)
#   i+=1

# Q1 d) happy no.
# num=int(input("num : "))
# while num>0:
#   rem=0
#   sum=0
#   rem=num%10
#   sum=sum+(rem*rem)
#   num=num//10
#   print(sum)
#   result=num
#   while result!=1 and result!=4:
#     result= "is happy no."
#     if result==1:
#       print(str(num+"is happy no."))
#     elif result==4:
#       print(str(num+"not a happy no."))

# Q palindrome num
# n=int(input("Enter number:"))
# a=n
# b=0
# while n>0:
#     d=n%10
#     print(d)
#     b=b*10+d
#     n=n//10
# if(a==b):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")

# unit=input('enter a character : ')
# if (unit>='a' and unit<='z') or (unit>='A' and unit<='Z'):
#   print("it is a alphabet")
# elif (unit>="0" and unit<="9"):
#   print("it is a digit")
# elif (unit<='0' and unit<='-9'):
#   print("it is a negative digit")
# else:
#   print("it is a special character")

# i=0
# while i<=10:
#   print(i)
#   i+=2

# d=int(input("distance : "))
# if d<=10:
#   print(d*11)
# elif d>10 and d<=100:
#   print((d*10)-110)
# elif d>100:
#   a=(d-100)*9
#   b=(d-90)*9
# #   print(a+b)

# a=int(input("side 1 :- "))
# b=int(input("side 2 :- "))
# c=int(input("side 3 :- "))
# if a+b>c and b+c>a and a+c>b:
#   print("triangle")
# else:
#   print("not")

# a=int(input("no. of rows :- "))
# i=1
# while i<=a:
#   print("*",end="")
#   i+=1

# a=int(input("no. 1 :- "))
# b=int(input("no. 2 :- "))
# i=a+1
# while a<b:
#   if a%2==0:
#     a+=2
#     print(a)

# a=input("name : ")
# i=1
# while i<=5:
#   print("hello",a)
#   i+=1
  
# i=1
# while i<=5:
#   print("hello")
#   i+=1

# i=1
# while i<=5:
#   print(i)
#   i+=1
  
# i=1
# while i<=5:
#   a=input("name ")
#   print(i)
#   i+=1

# i=0
# while i<=15:
#   if i==0:
#     print(i,"is zero")
#   elif i%2==0:
#     print(i,"is even")
#   else:
#     print(i,"is odd")
#   i+=1

# i=10
# while i<=150:
#   print(i,end=' ')
#   i+=10

# a=int(input("no."))
# i=0
# j=a%10
# while i>=0:
#   # j=a%10
#   if j%2==0 and j%3==0:
#     print(j,'is divisible by 2 and 3')
#     # i+=1

# a=int(input("no. "))
# k=a%10
# j=k//10
# while a>999:
#   print(k,j,end='')

# a=int(input("no. "))
# while a>0:
#   k=a%10
#   print(k,end='')
  # j=a//10

# i=int(input("no,"))
# while i>0:
#   k=i%10
#   print(k,end='')
#   i=i//10

# a=int(input("no.1 : "))
# b=int(input("no.1 : "))
# i=a
# sum=0
# Sum=0
# while i<=b:
#   if i%2==0:
#     sum+=i
#     print(i,"even","sum",sum)
#   elif i%2!=0:
#     Sum+=i
#     print(i,"odd","sum",Sum)
#   i+=1
# print(sum,"all even numbers sum")
# print(Sum,"all odd numbers sum")

# a=int(input("no. 1 : "))
# b=int(input("no. 2 : "))
# i=1
# sum=0
# while i<=b:
#   sum+=a
#   i+=1
#   print(sum)

# a=int(input("enter a no. : "))
# i=1
# f=1
# while i<=a:
#   if a==1:
#     print(a)
#   elif a>1:
#     f*=i
#     # print(f)
#   i+=1
# print(f)

# i=1
# sum=0
# while i<11:
#   a=int(input('no. : '))
#   sum+=a
#   i+=1
# print(sum)
# print(sum/10)

# i=1
# while i<=50:
#   while i<=25:
#     print(i,end='')
#     i+=5

# i=1
# while i<=5:
#   j=1
#   while j<10:
#     print(j,end='')
#     j+=1
#   print()
#   i+=1

#square
#j<=a is also right
# a=int(input("no. "))
# i=1
# while i<=a:
#   j=1
#   while j<a:
#     print(j,end='')
#     j+=1
#   print()
#   i+=1

#number triangle without gap
#with gap put i<a
# a=int(input("no. "))
# i=1
# while i<=a:
#   j=1
#   while j<=i:
#     print(j,end='')
#     j+=1
#   print()
#   i+=1

# a=int(input("no. "))
# i=1
# while i<=a:
#   j=1
#   while j<=a:
#     print(j,end='')
#     j+=1
#   print()
#   i+=1

# i=1
# while i<=50:
#   if i%3!=0 and i%5!=0:
#     print(i)
#   # elif i%3==0:
#   #   print('fizz')
#   # elif i%5==0:
#   #   print('buzz')
  # elif i%3==0 and i%5==0:
  #   print("Fizz-buzz")
  # elif i%3==0:
  #   print('fizz')
  # elif i%5==0:
  #   print('buzz')
  # i+=1  
  
  
#   L=[23, 45, 32, 25, 46, 33, 71, 90]
# while 232 in L:
#   if L%2!=0:
#     print(L)
#   i+=1




# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# while a>0 or a<0:
#   if a+b==20:
#     print("20")
#   else:
#     print("The sum of the given two numbers is",a+b)
#   break

# QUESTION 32
# a=int(input("no. : "))
# i=1
# while i<=a:
#   if i==1:
#     print(1,end=' ')
#     if i>1:
#       if i%2==0:
#         print(i*i,end='+')
#       # else:
#       elif i%2==1:
#         print(i*i,end='-')
#     i+=1

#patterns
# n=int(input("rows : ")) 
# i=1
# while i<=n: 
#   if i==1: 
#     print(" "*(n-1)+"*")
#   elif i==n: 
#     print("* " * i)
#   else: 
#     print(" "*(n-i) + "*" + " " * (2*i-3) + "*")
#   i+=1

# n=int(input("num : "))
# i=1
# while i<=n:
#   if i%2==1:
#     print("*"*i,end="")
#     j=1
#   else:
#     while j<=i:
#       print(j,end="")
#       j+=1
#   print()
#   i+=1
  
# n=int(input("num : "))
# i=1
# while i<=n:
#   if i%2==1:
#     print("*"*i)
#     j=1
#   else:
#     while j<=i:
#       print(j,end="")
#       j+=1
#   print()
#   i+=1 

# a=int(input("no. "))
# i=1
# while i<=a:
#   j=1
#   while j<=i:
#     print(j,end='')
#     j+=1
#   print()
#   i+=1
  
# a=int(input("no. of rows : "))
# i=1
# while i<=a:
#   print(i*"*")
#   i+=1
  
# n=int(input("num : "))
# j=0
# i=j+2
# while j<=n:
#   print(j+1)
#   print()
#   j+=1
#   print(j+1,i,end='')

#  n=int(input("Enter number:"))
# a=n
# b=0
# while n>0:
#     d=n%10
#     print(d)
#     b=b*10+d
#     n=n//10
# if(a==b):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")

# decimal to binary
# a=int(input('no. : '))
# b=a
# binary=0
# i=0
# while b>0:
#   remainder=b%2
#   binary=binary+remainder*(10**i)
#   b=b//2
#   i+=1
# print(binary,'binary')


# a=int(input('no. : '))
# if a==2 or a==3 or a==5:
#   print(a,'is prime')
# elif a%2==0 or a%3==0 or a%5==0:
#   print(a,'is not prime')
# else:
#   print(a,'is prime')
  
# print(49+(6/8*6))
# print(8*6)
# print(6/48)
# print(49+0.125)


# i=5
# while i>0:
#   j=5
#   while j>=1:
#     print(j,end='')
#     j-=1
#   print()
#   i-=1

#right triangle
# a=int(input("no. "))
# i=1
# while i<=a:
#   j=1
#   while j<=i:
#     print(j,end='')
#     j+=1
#   print()
#   i+=1

#12345 inverted right triangle  
# a=int(input("no. : "))
# i=a
# while i>0:
#   j=1
#   while j<=i:
#     print(j,end='')
#     j+=1
#   print()
#   i-=1
  
#same no. in one line 
# a=int(input("no. : "))
# i=a
# while i>0:
#   j=1
#   while j<=i:
#     print(i,end='')
#     j+=1
#   print()
#   i-=1
 
# name pattern
# a=input("name : ")
# b=len(a)
# # i=a
# while b>0:
#   j=1
#   while j<=b:
#     print(b,end='')
#     j+=1
#   print()
#   b-=1

# a=input("name : ")
# b=len(a)
# # i=a
# while b>=len(a):
#   j=1
#   while j<=b:
#     print(a[0],end='')
#     j+=1
#   print()
#   b-=1

# x=int(input('no. : '))
# N=int(input('no. : '))
# n=1
# print(1,'+',end='')
# while n<=N:
#   if x>1:
#     print(x**n,'/',n,end='+ ')
#     n+=1

# N=int(input('no. : '))
# n=1
# print(1)
# while n<=N:
#   print('x','^',n,'/',n)
#   n+=1

#number pattern
# n=int(input("num : "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1

# i=0
# while i<=50:
#   print(i)
#   # print(i*2)
#   i+=1
# i+=1
# print(i)


'''loops'''
'''question 1 a)
i=0
while i<=20:
  print(i)
  i+=2'''
  
'''question 1 b)
i=1
while i<=19:
  print(i)
  i+=2'''
  
'''question 1 c)
i=1
while i<=10:
  print(i)
  i+=1'''
  
''' name b hh aaa...'''
# a=input('name : ')
# i=0
# while i<len(a):
#   if a>='a' and a<='z' or a>='A' and a<="Z":
#     j=0
#     while j<=i:
#       print(a[i],end='')
#       j+=1
#   print()
#   i+=1
  
""" name b bh bha...."""
"""a=input('name : ')
i=0
while i<len(a):
  if a>='a' and a<='z' or a>='A' and a<="Z":
    j=0
    while j<=i:
      print(a[j],end='')
      j+=1
  print()
  i+=1"""
 
'''1 33 555''' 
'''a=int(input('no : '))
i=1
while i<=a:
    j=1
    while j<=i:
      print(i,end='')
      j+=1
    print()
    i+=2'''

# a=int(input('no. : '))
# i=a
# while i<=a:
#   while i>=1500 and i<=2700:
#     if i%5==0 and i%7==0:
#       print(i)
#   i+=1

# i=1
# while i<=5:
#   j=1
#   while j<=i:
#     if j%2==1:
#       print(j,end=" ")
#       j+=1
#   print()
#   i+=1
  
# for i in range(5):
#   for j in range(i,5):
#     print(" ",end=" ")
#   for j in range(i+1):
#     print("*",end=" ")
#   print()
  
# i=1
# j=1
# while i<=5:
#   while j<=i:
#     # print("*",end='')
#     j+=1
#   while j<=i+1:
#     print("*"*i,end='')
#     j+=1
#   print()
#   i+=1

# i=1
# while i<=5:
#   print(i*'*')
#   i+=1
  
# j=5
# while j<=5:
#   print(j*'*')
#   j-=1

# a=int(input('no.'))
# b=int(input('no.'))
# c=int(input('no.'))
# while a<=c:
#   if a>b and a<c:
#     print(a,'is')
#   elif a<b and a>c:
    
# while b<=c:
#   if b>a and b<c:
#     print(b,'no')
