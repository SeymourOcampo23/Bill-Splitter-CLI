def add_tip(amount, prompt):
    """gets the initial amount and adds a tip"""
    percent_tip = 0
    while percent_tip <= 0:
        percent_tip = float(input(prompt))
    total = amount * (100 + percent_tip)/100
    return total


print()