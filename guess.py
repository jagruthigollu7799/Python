secret = 7
guess = int(input("Enter your guess:"))
while guess != secret:
    print("Wrong! Try again.")
    guess = int(input("Enter your guess:"))
print("Correct! 🎉🎉🥳🥳")
