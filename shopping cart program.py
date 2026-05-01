#shopping cart program
print("--------------------")
print("       MENU       ")
print("--------------------")

menu = {"apple" :3,
          "banana" :2,
          "orange" :2.50,
          "pineapple":5}
cart = []
total = 0
for key,value in menu.items() :
    print(f"{key}:RM{value:.2f}")

while True :
    fruits = input("Please enter the fruit that what you want(q to quit) : ")
    if fruits == "q" :
        break
    elif fruits not in menu.keys() :
        print("Sorry, please enter a valid fruit.")
    elif fruits in menu.keys() :
        cart.append(fruits)


print("------------------")
print("      cart        ")
print("------------------")
for item in cart :
    total += menu[item]
    print(item,end=" ")

print()
print(f"This is your bills.")
print(f"Total:RM{total:.2f}.")
print("Have a nice day!")