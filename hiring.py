for i in range(0,19+1):
    
    if i<=7:
        print("already booked")
        continue
    else:
        skill=input("tell us your skill")
        if skill=="java" or skill=="python" or skill=="script":
            print("you are recruited")
        else:
            print("better luck next tym")
