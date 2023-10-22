racket_price = float(input())
number_of_rackets = int(input())
number_of_sneakers = int(input())

sneakers_price = racket_price / 6

total_equipment_price = (racket_price * number_of_rackets) + (sneakers_price * number_of_sneakers)

other_equipment_price = total_equipment_price * 0.2

djokovic_price = (total_equipment_price + other_equipment_price) // 8

sponsors_price = total_equipment_price + other_equipment_price - djokovic_price

print(f"Price to be paid by Djokovic {int(djokovic_price)}")
print(f"Price to be paid by sponsors {int(sponsors_price)}")