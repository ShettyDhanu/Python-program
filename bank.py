#2. Bank charges 20rs fee for debit transaction each if its more than 5 from the last 10 transaction list

for debit in range(1,10+1):
    count=0
    transact=input("you want to do transaction")
    if transact=="yes":
        count+=1
    else:
        print("remain same")
        count=count
        if count<5:
            print("youll get penalty of 20re")
        
        else:
            print("u have no penalty")

