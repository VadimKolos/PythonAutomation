ticketCount = int(input("input tickets count: "))

i = 0
fullPrice = 0
tickets = {"kid": 0, "young": 100, "adult": 200}

while i < ticketCount:
    i = i + 1
    age = int(input("input age for this ticket: "))
    if age < 18:
        fullPrice += tickets["kid"]
    if 18 <= age <= 25:
        fullPrice += tickets["young"]
    if age > 25:
        fullPrice += tickets["adult"]

if ticketCount > 3:
    print("Total price: ", fullPrice * 0.9)
else:
    print("Total price: ", fullPrice)