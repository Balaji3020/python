weight = float(input("enter your weight in kg:"))
height = float(input("enter your height in cm:"))

height_in_meters =height / 100
BMI = weight / (height_in_meters **2)

print("your BMI is:",BMI)

if BMI < 18.5:
    print("under weight")
elif 18.5 <= BMI < 25:
    print("healthy weight")
elif 25 <= BMI <30:
    print("over weight")   
else:
    print("obessed")    