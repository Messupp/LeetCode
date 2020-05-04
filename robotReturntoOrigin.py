a = "LL"

movesDict = {
	"U":1,
	"D":-1,
	"L":-10,
	"R":10
}

output = 0
for i in a:
	output += movesDict[i]

print(output)

if output == 0:
	print('yo')
else:
	print('no')