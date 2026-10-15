#task 1
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a>b:
    print(a, "is greater than", b)
elif a<b:
    print(b, "is greater than", a)
else:
    print(a, "is equal to", b)


#task 2
y=float(input("Enter a number: "))
if y>0:
    print("The number is positive")
elif y<0:
    print("The number is negative")
else:
    print("The number is equal to zero")


#task 3
x=int(input("Enter a number: "))
if x % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


#task 4 
s = int(input('Enter your score: '))
if 0 <= s <= 100:
    if s >= 91:
        print("Grade: A")
    elif s >= 81:
        print("Grade: B")
    elif s >= 71:
        print("Grade: C")
    elif s >= 61:
        print("Grade: D")
    elif s >= 51:
        print("Grade: E")
    elif s < 51:
        print("Grade: F")
    else:
        print("Invalid score")


#task 5
a1 = int(input("Enter the first number: "))
a2 = int(input("Enter the second number: "))
a3 = int(input("Enter the third number: "))
if a1 >= a2 and a1 >= a3:
    print(a2, "is the largest number")
elif a2 >= a1 and a2 >= a3:
    print(a2, "is the largest number")
else:
    print(a3, "is the largest number")


#task 6
y1 = int(input("Enter the first number: "))
y2 = int(input("Enter the second number: "))
u = input("Enter an operation symbol: ")
if u=="+":
    print(y1+y2)
elif u=="-":
    print(y1-y2)
elif u=="*":
    print(y1*y2)
elif u=="/":
    print(y1/y2)
elif u=="%":
    print(y1%y2)
elif u=="**":
    print(y1**y2)
elif u=="//":
    print(y1//y2)
else:
    print("Invalid operation")


#task 7
age=int(input("Enter the age"))
if age>0 and age<=12:
    print("Child")
elif age>=13 and age<=17:
    print("Teenager")
elif age>=18 and age<=64:
    print("Adult")
elif age>=65:
    print("Senior")
else:
    print("Invalid age")


#task 8
op=int(input()) #op-original price
if op<100:
    print("No discount")
elif op>=100 and op<=299:
    da=op*0.1 #da-discount amount
    fp=op-da #final price
    print(op, da, fp)
elif op>=300 and op<499:
    da=op*(15/100)
    fp=op-da
    print(op, da, fp)
else:
    da=op*0.2
    fp=op-da
    print(op, da, fp)


#task 9
k1=int(input("Enter the first number: "))
k2=int(input("Enter the second number: "))
k3=int(input("Enter the third number: "))
if k1>k2 and k1>k3:
    if k2>k3:
        print(k3, k2, k1)
    else:
        print(k2, k3, k1) 
if k2>k1 and k2>k3:
    if k1>k3:
        print(k3, k1, k2)
    else:
        print(k1, k3, k2)
if k3>k1 and k3>k2:
    if k1>k2:
        print(k2, k1, k3)
    else:
        print(k1, k2, k3)


#task 10
balance = 1000
t = int(input("Enter the amount of withdrawal: "))
if t<=0:
    print("Invalid amount")
elif t>balance:
    print("Insufficient balance")
else:
    print("Remaining balance is ",balance - t)


#task 11
e=int(input("Enter monthly electricity usage in kWh: "))
if e>=0 and e<=100:
    l=e*0.08
    print(e,0.08,l)
elif e>=101 and e<=300:
    l=i*0.12
    print(e,0.12,l)
elif e>300:
    l=e*0.15
    print(e,0.15,l)
else:
    print("Invalid input")


#task 12
start_fee = 2
d = float(input("Distance: "))
if d < 0:
    print("Invalid distance")
else:
    if d <= 5:
        df = d * 0.70
    elif d <= 15:
        df = 5 * 0.70 + (d - 5) * 0.60
    else:
        df = 5 * 0.70 + 10 * 0.60 + (d - 15) * 0.50
    total_fare = start_fee + df
    print("Starting fee:", start_fee, "AZN")
    print("Distance fee:", df, "AZN")
    print("Total amount:", total_fare, "AZN")


#task 13
g = int(input("Enter your age "))
r = float(input("Enter your salary "))
v = float(input("Enter your requested loan amount "))
if g < 18:
    print("Loan is rejected because of your age")
elif r < 500:
    if v > r * 10:
        print("Loan is rejected because requested loan is more than ten times your salary")
    else:
        print("Loan is rejected because of your salary ")
else:
    print("Loan is approved")


#task 14
a1 = int(input("Enter the first number: "))
b1 = int(input("Enter the second number: "))
c1 = int(input("Enter the third number: "))
if a1 + b1 > c1:
    if a1 + c1 > b1:
        if b1 + c1 > a1:
            if a1 == b1:
                if b1 == c1:
                    print("Equilateral")
                else:
                    print("Isoscales")
            elif b1 == c1:
                if a == b:
                    print("Equilateral")
                else:
                    print("Isoscales")
            elif a1 == c1:
                if c1 == b1:
                    print("Equilateral")
                else:
                    print("Isoscales")
            else:
                print("Scalene")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")
else:
    print("Triangle cannot be created")


#task 15
a2 = float(input("Enter your exam score: "))
b2 = float(input("Enter your school score: "))
c2 = int(input("Enter your age: "))
if c2 < 16:
    print("Application is rejected because of your age")
elif a2 >= 600:
    print("Application is accepted with a scholarship")
elif a2 <= 599 and a2 >= 450:
    print("Application is accepted")
elif a2 <= 449 and a2 >= 300:
    if b2 >= 80:
        print("Application is accepted")
    else:
        print("Application is rejected because of your schools core")
else:
    print("Application is rejected because of your exam score ")