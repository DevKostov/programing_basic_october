drink = input()
sugar = input()
drink_count = int(input())

price = 0

if drink == "Espresso" and sugar == "Without":
    price = 0.90
elif drink == "Espresso" and sugar == "Normal":
    price = 1
elif drink == "Espresso" and sugar == "Extra":
    price = 1.20

if drink_count >= 5 and (drink == "Espresso" or drink == "Cappuccino"):
    price *= 0.75

if drink == "Cappuccino" and sugar == "Without":
    price = 1
elif drink == "Cappuccino" and sugar == "Normal":
    price = 1.20
elif drink == "Cappuccino" and sugar == "Extra":
    price = 1.60

if drink == "Tea" and sugar == "Without":
    price = 0.50
elif drink == "Tea" and sugar == "Normal":
    price = 0.60
elif drink == "Tea" and sugar == "Extra":
    price = 0.70

total_price = drink_count * price

if sugar == "Without":
    total_price *= 0.65

if total_price > 15:
    total_price *= 0.8

print(f"You bought {drink_count} cups of {drink} for {total_price:.2f} lv.")
