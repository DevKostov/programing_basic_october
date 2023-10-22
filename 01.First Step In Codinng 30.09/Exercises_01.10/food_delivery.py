chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_price = 2.50

number_of_chicken_menus = float(input())
number_of_fish_menus = float(input())
number_of_vegetarian_menus = float(input())

price_without_delivery =  ((number_of_chicken_menus * chicken_menu_price)
                           + (number_of_fish_menus * fish_menu_price)
                           + (number_of_vegetarian_menus * vegetarian_menu_price))
desert_price = price_without_delivery * 0.2
total_price = price_without_delivery + desert_price + delivery_price

print(total_price)
