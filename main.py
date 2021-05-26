import math
import os
import logging
import django
from helper import *

number_of_days = ""
months_of_the_year = ["jan", "feb", "mar"]
months_of_the_year_set = {"jan", "jan"}
information = {"days": 20, "unit": "seconds"}
logger = logging.getLogger("MAIN")

if 'posix' in os.name:
    logger.error("os is called " + os.name)

while number_of_days != "exit":
    months_of_the_year.append("apr")
    number_of_days = input(user_input_message)
    number_of_days_arr = number_of_days.split(",")

    for number_of_days_item in set(number_of_days_arr):
        print(DaysProcessor.__doc__)
        print(math.pi)
        day_processor = DaysProcessor(20, "seconds")
        day_processor.validate_and_execute(number_of_days_item, information["unit"])
