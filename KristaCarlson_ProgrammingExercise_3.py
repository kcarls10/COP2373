from functools import reduce
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
    total = reduce(lambda acc, expenses: acc + expenses[1], expenses, 0)
    return total

def highest_monthly_expense(expenses):
    return reduce(lambda  x, y: x if x[1] > y[1] else y, expenses)

def lowest_monthly_expense(expenses):
    return reduce(lambda  x, y: x if x[1] < y[1] else y, expenses)

def main():
    expenses = monthly_expenses()
    total = calculate_monthly_expenses(expenses)
    highest = highest_monthly_expense(expenses)
    lowest = lowest_monthly_expense(expenses)

    print(f"total monthly expenses: ${total}")
    print(f"highest monthly expenses: {highest[0]} ${highest[1]}")
    print(f"lowest monthly expenses: {lowest[0]} ${lowest[1]}")

if __name__ == '__main__':
        main()

