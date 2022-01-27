import os
from Silent_bid_art import logo as logo

print(logo)
bids = {}

def find_highest_bidder(bidding_record):
    highest_amount = 0
    for bidders in bidding_record:
        bid_amount = bidding_record[bidders]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidders
    print(f"The winner is {winner} with a bidding amount of ₹{highest_amount}")
    
def clear():
    os.system("cls")

while True:
    ask_name = input("Enter your name: ")
    ask_amount = float(input("Enter the amount of money you want: ₹"))
    bids[ask_name] = ask_amount
    want_to_continue = input("Is there any other bidders?\nType (yes/no)\n").lower()

    if want_to_continue == "yes":
        clear()

    elif want_to_continue == "no":
        find_highest_bidder(bids)
        break

    else:
        print("You made a typo!!")
        want_to_continue = input("Is there any other bidders?\nType (yes/no)\n").lower()
