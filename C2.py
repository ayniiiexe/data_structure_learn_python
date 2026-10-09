# count vowels
string=input("Enter a string: ")
vowels=0
for char in string:
    if char in "aeiouAEIOU":
        vowels+=1
print("Number of vowels:", vowels)