#bus ticket

chart=""
for row in range(1,8):
    for seat in range(1,5):
        amt=int(input("Tell us amount u have: "))
        if amt>=250:
            print("Ur seat Number: ",row,seat)
            chart+="$"
        else:
            chart+="#"
    chart+="\n"

print(chart)
