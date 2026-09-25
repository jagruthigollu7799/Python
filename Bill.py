Bill = int(input("What is electricity bill:"))

if Bill <= 100:
    print(" 5 rupees per unit")
    print("Total:",Bill*5)
elif Bill <= 200:
    print(" 7 rupees per unit")
    print("Total:",Bill*7)
else:
    print(" 10 rupees per unit")
    print("Total:",Bill*10)
