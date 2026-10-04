secret =7
guess = int(input("Enter your guess:"))
while guess!= secret:
    if guess < secret:
        print("Too low!")
    else:
        print("Too high")
        
    guess = int(input("Enter your guess:"))
    
print("Correct!")
