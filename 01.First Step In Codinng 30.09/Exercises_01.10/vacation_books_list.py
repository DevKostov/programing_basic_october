pages_in_current_book = int(input())
pages_per_hour = int(input())
days_available = int(input())

total_hours_needed = pages_in_current_book / pages_per_hour

hours_per_day_needed = total_hours_needed / days_available

print(int(hours_per_day_needed))
