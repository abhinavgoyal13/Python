x = int(input("Enter a number"))
i = 2
flag = 0

while (i < x):
    if x % i == 0:
        flag = 1
        break
    else:
        i = i + 1
        continue

if flag == 1:
    print("Its Not a prime number")
else:
    print("Its a prime number")

# Next 5 prime numbers after entering a number
x = int(input("Enter a number"))

count=0
while (True):
    i = 2
    flag = 0
    while (i < x):
        if x % i == 0:
            flag = 1
            break
        else:
            i = i + 1
            continue

    if flag != 1:
        count=count +1
        print("{0} is a prime number".format(x))
        if count==5:
            break
    x=x+1



