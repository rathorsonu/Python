name = input("Entor bid person name: ")
bid_price = int(input("Enter bid price: $"))

bid_dict = {}
bid_dict[name] = bid_price

shoud_continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

continue_bidding = True

while continue_bidding:
    name = input("Entor bid person name: ")
    bid_price = int(input("Enter bid price: $"))
    bid_dict[name] = bid_price
    shoud_continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()


    if shoud_continue_bidding == 'no':
        continue_bidding = False
        print("Bidding is closed.")
        for key in bid_dict:
            if bid_dict[key] == max(bid_dict.values()):
                print(f"The winner is {key} with a bid of ${bid_dict[key]}")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
    