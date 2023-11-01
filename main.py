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
