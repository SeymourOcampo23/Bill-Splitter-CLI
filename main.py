from add_tip import add_tip
from format_money import format_money
from get_number import get_number
from split_bill import split_bill
from get_positive_number import get_positive_number

def main():
    prompt = "What was the amount: "
    prompt_tip = "How much do you want to tip in percentage?: "
    total = add_tip(get_number(prompt), prompt_tip)
    num_people = get_positive_number("How many people to split by?:")
    cost_per_person = split_bill(total, num_people)
    print(format_money(cost_per_person, total, num_people ))


if __name__ == "__main__":
    main()
    