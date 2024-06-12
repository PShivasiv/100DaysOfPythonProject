#This programe is calculate your BMI and tells you are over weight or under weight
height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg:"))
BMI = weight / height ** 2
if BMI < 18.5:
    print("Your are underweight")
elif BMI > 18.5 and BMI < 25:
    print("Your have a normal weight")
elif BMI > 25 and BMI < 30:
    print("Your have a over weight")
elif BMI > 30 and BMI < 35:
    print("You are obese")
else:
    print("You are cliniclly obese")
print("Your BMi is ", BMI)
