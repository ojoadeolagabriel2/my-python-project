from datetime import datetime

target_date = input("enter your target summary [goal:date]:\n")
target_date_parts = target_date.split(":")

goal = target_date_parts[0]
deadline = target_date_parts[1]
print(target_date_parts)

today_date = datetime.today()
target_date = datetime.strptime(deadline, "%d.%m.%Y");

result = target_date - today_date
print(result)
print(type(result))
print(f"interval in hours {int(result.total_seconds() / 60 / 60)}")
