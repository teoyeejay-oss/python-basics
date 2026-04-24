#Personal information
name = input("Please enter your name: ")
gross_salary = float(input("Please enter the amount of your gross salary(RM): "))
credit_number =input("Please enter your credit number(****-***-****): ")
while len(credit_number) <13 :
    credit_number = input("Please enter again your credit number because it's not valid: ")
bank_name = input("Please enter your bank name: ")


name =name.capitalize()
print(f"Welcome {name}!" if len(credit_number) >= 13 else "Your credit number is not valid.")

if 5000 > gross_salary >3000   :
    net_salary1 = gross_salary - (gross_salary*(11.7/100))
    print(f"Your total salary is RM{net_salary1:.2f}")
elif gross_salary >=5000 :
    net_salary2 = gross_salary - (gross_salary*(13.5/100))
    print(f"Your total salary is RM{net_salary2:.2f}")

last_digit = credit_number[9:13]
print(f"And your last digit number of your credit number is ****-***-{last_digit},later I will transfer your salary into your {bank_name} account.")
