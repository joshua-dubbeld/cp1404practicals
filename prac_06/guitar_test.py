from prac_06.guitar import Guitar

CURRENT_YEAR = 2020

g1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
g2 = Guitar("Another Guitar", 2013, 20)

print(g1)
print(g2)

print(g1.get_age(CURRENT_YEAR))
print(g1.cost)