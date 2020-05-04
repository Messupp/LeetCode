A = [3,1,2,4]
evens = []
odds = []
for i in A:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

output = evens + odds
print(output)