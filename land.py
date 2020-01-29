#if and else
#squarefeet,pincode

square=float(input("tell us the square_feet"))
pincode=int(input("tell us pincode of city:"))
if square<=500 or square<=1 and pincode==574240:
    print("registration charges is:2400")
elif square<=1000 or square<=4 and pincode==52345:
    print("restration charges is:3600")
elif square >=1500 or square<=8 and pincode==56789:
    print("registration charges is:4800")
else:
    print("sorry,enter valid")
