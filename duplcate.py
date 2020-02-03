arr = [20, 45, 60, 45, 90,100];     
     
print("Duplicate elements in given array: ");

    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j]);

number=int(input("any number"))
number=number%arr==0

