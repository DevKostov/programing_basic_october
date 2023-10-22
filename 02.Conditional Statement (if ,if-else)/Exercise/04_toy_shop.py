needed_price = float(input())
numbers_of_puzzle = int(input())
number_of_talking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_sum = numbers_of_puzzle * 2.6 \
            + number_of_talking_dolls * 3 \
            + number_of_teddy_bears * 4.10 \
            + number_of_minions * 8.20 \
            + number_of_trucks * 2
units_ordered = numbers_of_puzzle \
                 + number_of_talking_dolls \
                 + number_of_teddy_bears \
                 + number_of_minions \
                 + number_of_trucks
if units_ordered >= 50:
    total_sum = total_sum * 0.75

total_sum = total_sum * 0.90

difference = abs(total_sum - needed_price)

if total_sum >= needed_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")