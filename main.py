from replit import clear

#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)


bidder = input("Enter the your name: ")
bidding_amount = int(input("Enter your bid amount: $"))
bidding_record = {}
bidding_record[bidder] = bidding_amount

def adding_user(bidder, bidding_amount):
    bidding_record[bidder] = bidding_amount


def declare_result():
    highest_bidding = 0
    winner = ''
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount > highest_bidding:
            winner = bidder
            highest_bidding = bidding_amount
    return winner




continued = "yes"
while continued == "yes" or continued == "y":
    continued = input("There are other users who want to bid (Yes or No): ").lower()
    clear()
    if continued == "yes" or continued == "y":
        bidder = input("Enter the your name: ")
        bidding_amount = int(input("Enter your bid amount: $"))
        adding_user(bidder, bidding_amount)
else:
    print(f"The winner is {declare_result()} with a bid of ${bidding_record[declare_result()]}")

