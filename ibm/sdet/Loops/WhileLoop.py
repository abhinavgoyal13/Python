noOfStudents=int(input('Enter number of students:'))
counter=1
while counter <= noOfStudents:
    marks1 = int(input("Enter Marks1 :"))
    marks2 = int(input("Enter Marks2 : "))
    marks3 = int(input("Enter Marks3 : "))
    total = marks1 + marks2 + marks3
    average = total/3
    print(average)
    if average >= 75:
        print("Qualifed")
    else:
        print("Not Qualified")
    counter=counter+1
