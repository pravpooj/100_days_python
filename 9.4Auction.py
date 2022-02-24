from turtle import hideturtle
from clearscreen import clrscr
from art import logo

print(logo)

bids = {}
bid = True

def find_hights_bidder(bidding_record):
  higest_bid = 0
  winner = ""

  for bidder in bidding_record:
    bid_amout = bidding_record[bidder]
    if bid_amout > higest_bid:
      higest_bid = bid_amout
      winner = bidder
  print(f"The Winner is {winner} and bid is {bid_amout}")

  

while bid:
  name = input("what's your name?:\n")
  price = int(input("what Your bid?:\n$"))
  bid_winner = {}
  bids[name] = price
  print(bids)

  continue_bid = input("Any other user to bid?(Y/N):\n").capitalize()
  if continue_bid == "N":
    bid = False
    clrscr()
    find_hights_bidder(bids)
  else:
    clrscr()




  