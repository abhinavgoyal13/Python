a=['a',1,'2.3',"sada"]
print(a)
print(type(a))
print(type(a[0]))
#Inserring 10 at beginning
a[0]=10
print(a)

for i in a:
    print(i)

print(list(range(0,5)))

print(len(a))
# len is a function.. string/arraylist.. anyone can use it.. its not method associated with any

a=['a',1,'2.3',"sada"]
print(a[0:2])
print(a[-1])
print(a[::-1])

b=a
print(a)
print(b)
b[0]=25

#both a and b changes.. as they are by reference

print(id(a))
print(id(b))

#using copy there will be different references, so value will be diff for botth c and a
c= a.copy()
print(c)
print(a)
c[0]=100
print(c)
print(a)

#nested list

a=[1,2,[3,4,5]]
print(a[2][0])

print(2 in a)

a.append(100)
a.clear()

a=[1,2,3]
b=[5,6]
a.append(b)
print(a)

a=[1,2,3]
b=[5,6]
a.extend(b)
print(a)

#even number in list
a=[]
for i in range(1,10):
    if(i%2==0):
           a.append(i)

    print(a)
#list comprehension for even numbers

even_nos = [num for num in range(1,10) if num % 2 == 0]
print(even_nos)

#list comprehension
lst=[2,3,4,5,6,7]
lst1=[num*2 if num%2==0 else num*3 for num in lst]
print(lst1)

lst=list(range(1,10))
isEven=[num * 2 if num % 2==0 else num*3 for num in lst]
print(isEven)
#*******************
#num = [5,4,7,9,12,15,22,75,100,107]
# 1. Form a list by dividing every element by 2
#from Jigsaw Academy 01 to All Participants:
# 2. Form a list for all elements divisible by 5



#**************
Data = [' X-DSPAM-Confidence:0.8l475 ',' X-DSPAM-Confidence:0.765 ',
        ' X-DSPAM-Confidence:0.7065 ','Y-DSPAM-Confidence:0.9985 ',
        'Y-DSPAM-Confidence:0.6585 ']

xNumber = 0
xCount = 0
yNumber = 0
yCount = 0
for string in Data:
    string = string.strip()
    if string.startswith('X-DSPAM'):
        # xNumber = xNumber + float(string[19:])
        xNumber = xNumber + float(string.split(':')[1])
        xCount = xCount + 1
    if string.startswith('Y-DSPAM'):
        # yNumber = yNumber + float(string[19:])
        yNumber = yNumber + float(string.split(':')[1])
        yCount = yCount + 1

print('mean of X-DSPAM-Confidence is ', (xNumber) / xCount)
print('mean of Y-DSPAM-Confidence is ', (yNumber) / yCount)