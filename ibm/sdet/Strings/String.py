string1="hello"
print(string1)
print("*********************")
print(string1[0])
print("*********************")
for i in string1:
    print(i)
print("*********************")
print(string1[:])
print("*********************")
print(string1[2:4])
string2="Hello Python"
print(string2[2:8:2])

#Reverse a string1
print(string2[::-1])
# supports negativee indexing

# Palindrome string
string2=input("Enter a string")
if string2==string2[::-1]:
    print("Its a Palindrome")
else:
    print("Not a Palindrome")

string1="Hello"
print(string1.swapcase());

print(string1.find("e"))

#python
string1="python"
for i in string1:
    print(i,end=",")

print("*******************")
print(string1.replace("",","))

#************
print(len("abc"))

#************** Occurenec of character a in "Banana"
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

