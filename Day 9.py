import Auction_Func
Logo = Auction_Func.hammer[0]
print(Logo)

print("Welcome to Secret Auction")
input("Press e to continue...")
print("\n" * 100)

name = input("Enter your Name: ")
bid = float(input("Enter your Bidding Price: "))

house = {
    "Name": [name],
    "Bid": [bid]

}
new = input("Are there any other Users who wants to bid? (Yes/No): )")
print("\n" * 100)

while not new == "No":
    name = input("Enter your Name: ")
    bid = float(input("Enter your Bidding Price: "))

    house["Name"].append(name)
    house["Bid"].append(bid)

    new = input("Are there any other Users who wants to bid? (Yes/No): ")
    print("\n" * 100)

print("\n" * 100)

highest_bid = 0
for m_bid in house["Bid"]:
    if m_bid > highest_bid:
        highest_bid = m_bid

print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
print("Congratulations to the highest bidder!!")
print(f"Highest bidder is {house["Name"][house["Bid"].index(highest_bid)]} with bid of {highest_bid} !!")
print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

print("\n" * 4)
print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
print("Details of all the Bidders:")
print(house["Name"])
print(house["Bid"])
print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")





