import art
print (art.logo)


def highest_bid(bidding_dictionary):
    winner= " "
    highest_bidder = 0
    for bidder in  bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount>highest_bidder:
            highest_bidder=bid_amount
            winner= bidder
    print(f"The winner is {winner}, with a bid of ${highest_bidder}")


bidder_details={}  #<--- empty directory

more_bidders=True
while more_bidders:
    bidder_name = str(input("What is the bidder's name? ")).lower()
    bid_amount = float(input("What is the bidder's amount? $"))
    bidder_details[bidder_name] = bid_amount
    are_there_any_other_bidders = input("Are there any other bidders? Type yes / no \n").lower()
    if are_there_any_other_bidders=="no":
        more_bidders=False
        highest_bid(bidder_details)
    elif are_there_any_other_bidders=="yes":
        print("\n" *200)   #<--- Clearing the screen, so no one can see the other bids