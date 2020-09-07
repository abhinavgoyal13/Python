for i in range(5):
    print(i)
print("****************************")
for i in range(1,6):
    print(i)
print("******************")
#start, stop, step
for i in range(1,5,2):
    print(i)

noOfStudents=int(input('Enter number of students:'))
counter=1
for counter in range(0,noOfStudents):
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

for i in range(10,2,-2):
    print(i)

n=10
while True:
    print(n)
    n=n-2
    if n==0:
        break
print("Done")

#continue keyword
while True:
    line = input('Enter the input: ')
    if line == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

