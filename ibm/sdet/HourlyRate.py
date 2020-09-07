hourlyRate= int(input("Enter Hourly rate"))
hoursWorked= int(input("Enter hours worked"))
if hoursWorked>40 :
    pay=40*hourlyRate+(hoursWorked-40)*1.5 *hourlyRate
else:
    pay=hoursWorked*hourlyRate

print(pay)

