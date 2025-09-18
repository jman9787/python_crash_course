
guests = ["Abraham Lincoln", "Michelle Killam", "Ruth Ann Montgomery"]

for guest in guests:
    print(f"Hello {guest}, We would like to cordially invite you to the greatest dinner ever!")

print(f"Sorry! {guests[1]} cannot make it!")

del guests[1]
print(guests)

for guest in guests:
    print(f"Hello {guest}, We would like to cordially invite you to the greatest dinner ever!")


print("Heyo! We found a bigger table ")

new_guests = ["Spencer", "Jeffrey", "Beverly"]

guests.insert(0, new_guests[0])
guests.insert(1, new_guests[2])
guests.append(new_guests[1])

print(guests)
