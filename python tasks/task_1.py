age=int (input("enter your Age: "))

privilage= input("privilage : Y  or  N  ")

amount=int(input("amount in total : "))

if (amount < 1000):
        if (age > 70):
            if(privilage == "Y"):
                total_discount = amount*0.85
                print("final billing amount is : ", total_discount)
            else:
                total_discount = amount*0.90
                print("final billing amount is : ", total_discount)
        else:
            total_discount = amount*0.95
            print("final billing amount is : ", total_discount)
elif  (amount >= 1000 and amount < 5000):
    if (age > 70):
            if(privilage == "Y"):
                total_discount = amount*0.80
                print("final billing amount is : ", total_discount)
            else:
                total_discount = amount*0.85
                print("final billing amount is : ", total_discount)
    else:
        total_discount = amount*0.90
        print("final billing amount is : ", total_discount)
elif  (amount >=5000):
    if (age > 70):
            if(privilage == "Y"):
                total_discount = amount*0.75
                print("final billing amount is : ", total_discount)
            else:
                total_discount = amount*0.80
                print("final billing amount is : ", total_discount)
    else:
        total_discount = amount*0.85
        print("final billing amount is : ", total_discount)
else:
    print("enter correct information:")
