from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"Income": "Income", "Expense": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the Amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero number")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the Category. \n1. Income \n2. Expense\n").capitalize().strip()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please try again!")
    return get_category()
def get_description():
    return input("Enter a Description(optional): ")
