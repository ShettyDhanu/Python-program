#to find first n prime numbers

num=int(input("enter the value of num:"))
for a in range(2,num+1):
    b=0
    for i in range (2,a//2+1):
        if(a%i==0):
            b=b+1
    if(b==0):
        print(a)
