flower_type = input()
number_of_flowers = int(input())
budget = int(input())
price = 0

if flower_type == "Roses":
    price = 5
    if number_of_flowers > 80:
        price *= 0.9
if flower_type == "Dahlias":
    price = 3.8
    if number_of_flowers > 90:
        price *= 0.85
if flower_type == "Tulips":
    price = 2.80
    if number_of_flowers > 80:
        price *= 0.85
if flower_type == "Narcissus":
    price = 3
    if number_of_flowers < 120:
        price *= 1.15
if flower_type == "Gladiolus":
    price = 2.5
    if number_of_flowers < 80:
        price *= 1.2

total_sum = price * number_of_flowers
difference = abs(total_sum - budget)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
