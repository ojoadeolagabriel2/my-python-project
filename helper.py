def number_of_seconds_in_days(days, unit):
    return f"{days} days contains {24 * 60 * 60 * days} {unit}"


def validate_and_execute(day, unit):
    try:
        num_days = int(day)
        if num_days < 0:
            print(f"{num_days} cannot be less than zero")
        elif num_days == 0:
            print(f"{num_days} is cannot be zero")
        else:
            print(number_of_seconds_in_days(num_days, unit))
    except Exception as error:
        print(repr(error))


class DaysProcessor:
    """yello"""
    days_self = ""

    def __init__(self, default_day, default_unit):
        self.default_day = int(default_day)
        self.default_unit = default_unit

    def number_of_seconds_in_days(self, days, unit):
        self.days_self = days
        return f"{days} days contains {24 * 60 * 60 * days} {unit}"

    def validate_and_execute(self, day, unit):
        try:
            num_days = int(day)
            if num_days < 0:
                print(f"{num_days} cannot be less than zero")
            elif num_days == 0:
                print(f"{num_days} is cannot be zero, cannot determine {self.default_unit}")
            else:
                print(number_of_seconds_in_days(num_days, unit))
        except Exception as error:
            print(repr(error))


user_input_message = "hey user, enter the number of months and unit required:\n"
