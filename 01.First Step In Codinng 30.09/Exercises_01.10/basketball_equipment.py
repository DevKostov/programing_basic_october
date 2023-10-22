annual_tax = int(input())
sneakers_price = annual_tax * 0.6
dress_price = sneakers_price * 0.8
ball_price = dress_price / 4
accsessories_price = ball_price / 5
total_sum = (annual_tax
             + sneakers_price
             + dress_price
             + ball_price
             + accsessories_price)
print(total_sum)