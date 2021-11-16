#madlibs v1

#madlibs collects user input and inserts it into a text template to create a story. 

#user input to be inserted in the madlibs.
food_item_1 = input("Enter name of food: ")
country_1 = input("Enter name of a country: ")
comparative_1 = input("Enter a comparative: ")
country_2 = input("Enter name of a country: ")
number_1 = input("Enter a number: ")
vehicle_1=input("Enter a mode of transport: ")
verb_1 = input("Enter a verb: ")
number_2 = input("Enter a number: ")
verb_2 = input("Enter a verb: ")
colour_1 = input("Enter a colour: ")
vegetable_1 = input("Enter a vegetable: ")

#Using an f-string to embed user input into the madlibs template. 

madlibs = f"The largest {food_item_1} in the world was discovered recently in {country_1}. \
It is {comparative_1} than {country_2} and is as wide as {number_1} {vehicle_1}s. \
The amazing thing is that it can {verb_1} more than {number_2} people. \
If you get a chance, you can go and {verb_2} it at the {colour_1} {vegetable_1} museum."

#print the madlibs

print(madlibs)
