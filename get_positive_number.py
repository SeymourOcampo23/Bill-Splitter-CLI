def get_positive_number(prompt):
    """Will keep asking user until they enter a whole number > 0"""
    num_people = 0
    while num_people <= 0:
        try:
            num_people = int(input(prompt))
        except ValueError:
            print("Must be a whole number greater than 0.")
            continue
    return num_people
