price_per_one_kilogram_vegetables = float(input())
price_per_one_kilogram_fruits = float(input())
total_kilos_of_vegetables = float(input())
total_kilos_of_fruits = float(input())

exchange_rate = 1.94

total_price_in_euro = ((price_per_one_kilogram_vegetables * total_kilos_of_vegetables)
                      + (price_per_one_kilogram_fruits * total_kilos_of_fruits)) / 1.94

print(f"{total_price_in_euro:.2f}")