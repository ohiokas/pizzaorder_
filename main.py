#show tittle
print ("WELCOME TO OURS STORE")
print ("___PIZZA CRUST___")

print("Input Your Name: ")
name = input() #get user name
print("Input Your Table: ")
table = input() #get user table

total_hrga = 35000

#showing topping menu
print("Our Topping Menu, Please choose one")
print("frankfuter bbq, meat monsta, super supreme, chiken lovers, cheese lovers, and american fav")
topping = input("Enter our fav toppings: ")
if topping == "frankfutter bbq" or topping == "meet monsta" or topping == "super supreme" or topping == "chiken lovers" or topping == "cheese lovers" or topping == "american fav":
    total_hrga = 50000 #get topping price
else:
    total_hrga = 0
  print("Sorry, your fav topping was sold out/nothing")

#showing and inputing crust menu 
print("Our Crust Menu, Pelase choose one ")
print("""original,
         stuffedcrust cheese,
         stuffedcrust sausage""")
crustPizza = input("Choose your fav crust : ")
if crustPizza == "original":
    total_hrga += 0
elif crustPizza == "stuffedcrust cheese":
        total_hrga += 20000 
elif crustPizza == "stuffedcrust sausage":
        total_hrga += 10000
else:
        print("Sorry, Your fav Crust was sold out")

#showing and inputing pizza size menu
print("Our Size Menu, Pelase choose one ")
print("""regular,
         medium,
         large""")
size = input("Choose your fav size : ")
if size == "regular":
    total_hrga += 0
elif size == "medium":
      total_hrga += 20000
elif size == "large":
        total_hrga += 40000
else:
    print("Sorry, Your fav Size was sold out")
