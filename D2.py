#positive and negative numbers in a list
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
negative = [] #negative numbers list
positive = []#positive numbers list
for n in numbers:
    if n < 0:
        negative.append(n)#n is added to negative list
    else:
        positive.append(n)#n is added to positive list
print("Positive numbers:", positive)
print("Negative numbers:", negative)