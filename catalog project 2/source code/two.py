class Auction:
    def __init__(self, item_name, start_price):
        self.item_name = item_name
        self.start_price = start_price
        self.current_price = start_price
        self.bidders = {}

    def place_bid(self, bidder_name, bid_amount):
        if bid_amount > self.current_price:
            self.current_price = bid_amount
            self.bidders[bidder_name] = bid_amount
            print(f"Bid placed by {bidder_name} for {bid_amount} on {self.item_name}")
        else:
            print("Bid amount is too low. Please try again.")

    def get_current_price(self):
        return self.current_price

    def get_bidders(self):
        return self.bidders

    def close_auction(self):
        if len(self.bidders) > 0:
            winner = max(self.bidders, key=self.bidders.get)
            print(f"Auction closed. Winner is {winner} with a bid of {self.bidders[winner]}")
        else:
            print("No bids placed. Auction closed without a winner.")

def main():
    item_name = input("Enter the item name for auction: ")
    start_price = float(input("Enter the starting price for the auction: "))
    auction = Auction(item_name, start_price)
    while True:
        print("\n1. Place a bid")
        print("2. Get current price")
        print("3. Get bidders")
        print("4. Close auction")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            bidder_name = input("Enter your name: ")
            bid_amount = float(input("Enter your bid amount: "))
            auction.place_bid(bidder_name, bid_amount)
        elif choice == "2":
            print(f"Current price: {auction.get_current_price()}")
        elif choice == "3":
            print("Bidders:")
            for bidder, bid_amount in auction.get_bidders().items():
                print(f"{bidder}: {bid_amount}")
        elif choice == "4":
            auction.close_auction()
            break
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
