one_package_of_pens = 5.80
one_package_of_markers = 7.20
board_cleaner_per_litter = 1.20

needed_package_of_pens = int(input())
needed_package_of_markers = int(input())
needed_litters_of_board_cleaner = int(input())
discount_percentages = int(input())


total_price = ((one_package_of_pens * needed_package_of_pens) +
               (needed_package_of_markers * one_package_of_markers) +
               (needed_litters_of_board_cleaner * board_cleaner_per_litter))

discount = total_price * (discount_percentages / 100)
total_amount = total_price - discount

print(total_amount)