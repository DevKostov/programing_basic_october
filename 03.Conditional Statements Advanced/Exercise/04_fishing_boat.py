budget = int(input())
season_type = input()
number_of_fisherman = int(input())
boat_rent = 0

if season_type == "Spring":
    boat_rent = 3000
    if number_of_fisherman <= 6:
        boat_rent *= 0.9
    if 7 < number_of_fisherman <= 11:
        boat_rent *= 0.85
    if number_of_fisherman > 12:
        boat_rent *= 0.75

if season_type == "Summer" or season_type == "Autumn":
    boat_rent = 4200
    if number_of_fisherman <= 6:
        boat_rent *= 0.9
    if 7 < number_of_fisherman <= 11:
        boat_rent *= 0.85
    if number_of_fisherman > 12:
        boat_rent *= 0.75

if season_type == "Winter":
    boat_rent = 2600
    if number_of_fisherman <= 6:
        boat_rent *= 0.9
    if 7 < number_of_fisherman <= 11:
        boat_rent *= 0.85
    if number_of_fisherman >= 12:
        boat_rent *= 0.75

if number_of_fisherman % 2 == 0 and season_type != "Autumn":
    boat_rent *= 0.95

difference = abs(boat_rent - budget)
if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")