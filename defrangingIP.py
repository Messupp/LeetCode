address = "1.1.1.1"
aList = []
for i in address:
	if i == '.':
		aList.append('[.]')
	else:
		aList.append(i)
output = ''.join(aList)
print(output)