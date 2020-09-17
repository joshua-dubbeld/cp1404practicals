from prac_06.guitar import Guitar
guitar_to_add = []
guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = int(input("Cost: "))
    guitar_to_add = Guitar(name, year, cost)
    guitars.append(guitar_to_add)
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

for i, guitar in enumerate(guitars, 0):
    vintage_string = " (Vintage)" if guitar.get_age() >= 50 else ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))

