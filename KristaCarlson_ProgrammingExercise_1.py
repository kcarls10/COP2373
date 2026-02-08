## Takes user input for amount of tickets requested.
def customer_input():
    tickets_requested = int(input('How many tickets do you need?: '))
    return tickets_requested
## Keeps track of remaining tickets by subtracting user input amount.
def remaining(tickets_requested, remaining_tickets):
    remaining_tickets -= tickets_requested
    print(f'{remaining_tickets} tickets remaining')
    return remaining_tickets
## Main function. Contains while loop, calls functions, validates input, tracks tickets available and buyers.
def main ():
    tickets_available = 10
    buyers = 0

    while tickets_available > 0:
        tickets_requested = customer_input()
        if 1 <= tickets_requested <= 4 and tickets_requested <= tickets_available:
            tickets_available = remaining(tickets_requested, tickets_available)
            buyers += 1
        else:
            print('Invalid input. Maximum tickets allowed (4)')

    print('\nSold out')
    print(f'Number of buyers: {buyers}')

if __name__ == "__main__":
    main()


