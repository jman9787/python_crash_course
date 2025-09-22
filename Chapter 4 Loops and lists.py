magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)

favorite_pizzas = ['Pepperoni', 'Mushroom', 'Sausage']

for pizza in favorite_pizzas:
    print(f'{pizza}')

print('I really love pizza!')

to_a_million = []

for number in range(1, 1_000_001):
    to_a_million.append(number)

print(max(to_a_million))
print(min(to_a_million))

print(sum(to_a_million))


for number in range(0,21,2):
    print(number)

for number in range(11):
    cube = number ** 3
    print(cube)

new_cubes = [value**3 for value in range(1,11)]

print(new_cubes[:3])
print(new_cubes[3:])