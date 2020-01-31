#to remove number of charecters from string

str=input("enter the string")
start=int(input("enter the starting index"))
end=int(input("enter the end index"))
if len(str)>end:
    str=str[:start:]+str[end+1::]
print(str)
        

