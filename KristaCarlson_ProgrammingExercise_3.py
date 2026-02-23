#function for collecting and returning expenses
def monthly_expenses():
    expenses = []

    while True:
        expense_type = input("Enter type of expense(type 'done' when finished): ")
        if expense_type.lower() == 'done':
            break

    try:
        amount = float(input(f"Enter amount of monthly expense {expense_type}: $"))
        expenses.append((expense_type, amount))

    except ValueError:
        print("Please enter valid number")

        return expenses

def calculate_monthly_expenses(expenses):
    total =

