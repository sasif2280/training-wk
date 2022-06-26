def cal_bmi(height,weight):

    bmi=weight/((height/100)**2)
    print(bmi," \n \n you are ", end="") 


 
    if bmi < 18.5:
    
        print("underweight")
    
    elif bmi >= 18.5 and bmi < 25:
    
        print(" Healthy weight")
    
    elif bmi >= 25 and bmi < 30:
    
        print("overweight")
    
    else:
    
        print("overweight")
    
height=float(input("\nenter your height in cm : "))

weight=float(input("\nenter your weight in kg :"))

cal_bmi(height,weight)
    
    
