def get_number(prompt):
    """asks user for a number(int > 0)"""
    bill = 0
    while bill <= 0:
        bill = float(input(f"{prompt}"))
    return bill
