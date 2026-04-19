#BMI calculator

weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))
bmi = weight/(height*height)
bmi = round(bmi,2)


if  18.5 <= bmi < 25 :
    print (f"Your bmi is {bmi},so you are normal.")
elif 16 <= bmi < 18.5  :
    print (f"Your bmi is {bmi},so you are underweight.")
elif 25 <=  bmi < 30  :
    print(f"Your bmi is {bmi},so you are overweight")
elif 30 <= bmi <40  :
    print(f"Your bmi is {bmi},so you are obesity")
elif bmi <= 0 :
    print("invalid input")
