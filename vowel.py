word = input("Enter a word:")
count = 0 
for letter in word:
    if letter in "aeiou":
        count = count + 1
print(f"Number of vowels = {count}")
