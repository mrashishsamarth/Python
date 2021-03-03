number_of_atoms = int(input())
resulting_quantity = int(input())
half_life = 0
while number_of_atoms > resulting_quantity:
    number_of_atoms = (number_of_atoms / 2)
    half_life += 1
    days = int(half_life) * 12
print(days)
