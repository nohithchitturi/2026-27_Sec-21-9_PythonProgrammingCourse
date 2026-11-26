# Example solution: count vowels, consonants, digits and spaces
s = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
for ch in s:
    if ch.lower() in "aeiou":
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)