pend={700:"sandisk",500:"hp",570:"sony",700:"toshiba",800:"strontium"}
price=0
print(pend)
def delete(start=0):
    price=int(input("Which price pendrive do you want to delete"))
    if pend.get(price,"This does not exist"):
        del pend[price]
        print(pend)
        start+=1
        if start>len(pend)-1:
            return
        delete()
    else:
        print("The price you selected does not exists")
        return
    
delete()
