S = "IDID"

stringLength = len(S)
alist = [0]

for i in range(len(S)):
	letter = S[i]
	if letter == 'D':
		alist.append(alist[i]-(stringLength-i))
	if letter == 'I':
		alist.append(alist[i]+(stringLength-i))

print(alist)