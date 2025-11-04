from datetime import datetime


def calculate_age(birthdate_str):

    try:

        birthdate = datetime.strptime(birthdate_str, "%Y/%m/%d")
        today = datetime.today()

        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        return age
    
    except ValueError:
        return "WRONG"


birthdate_str = input()
print(calculate_age(birthdate_str))