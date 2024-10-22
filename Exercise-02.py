#exercise 02 shopping cart program

item= input("WHat item would you like to buy?")
price= float(input("What is the price?"))
quantity= int(input("How many would you like to buy? :"))

total= price* quantity

print(f"you have brought {item} x {quantity}/s")
print(f"your total bill is :{total}")