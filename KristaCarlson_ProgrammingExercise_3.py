def monthly_expenses():
    expenses = []

    while True:
        expense_type = input("Enter type of expense(type 'done' when finished): ")
        if expense_type.lower() == 'done':
            break

    try:
        amount = int(input("Enter amount of monthly expense: "))

    except ValueError:
        print("Please enter valid number")

