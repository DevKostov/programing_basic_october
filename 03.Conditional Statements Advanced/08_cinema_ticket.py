day_of_the_weekend = input()
ticket_price = 0
if (day_of_the_weekend == "Monday"
        or day_of_the_weekend == "Tuesday"
        or day_of_the_weekend == "Friday"):
    ticket_price = 12

elif (day_of_the_weekend == "Wednesday"
      or day_of_the_weekend == "Thursday"):
    ticket_price = 14

elif (day_of_the_weekend == "Saturday"
      or day_of_the_weekend == "Sunday"):
    ticket_price = 16
print(ticket_price)
