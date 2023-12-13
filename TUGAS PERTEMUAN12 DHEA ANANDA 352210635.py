word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

for letter in word1:
    print(letter)

print("\n")

for letter in word2[::-1]:
    print(letter)
