hoursWorked=int(input("Enter number of hours worked: "))
rate=int(input("Enter Rate: "))

if hoursWorked > 40:
    extraTime=hoursWorked-40
    GrossPay=(40*rate + extraTime*1.5*5)
else:
    GrossPay=hoursWorked*rate
    
print(f"Gross Pay is: {GrossPay}")