class Solution(object):
	
	def nearestPalindromic(self, n):

		def findPositivePalindrome(n):
			Palindrome = False
			while Palindrome == False:
				n = int(n) + 1
				n = str(n)
				if len(n) % 2 == 0:
					# Even Digits
					digitList = []
					for digit in n:
						digitList.append(digit)
					numberLength = len(digitList)
					halfLength = numberLength / 2
					halfLength = int(halfLength)
					firstHalf = digitList[:halfLength]
					secondHalf = digitList[halfLength:]
					secondHalf.reverse()
					
					if firstHalf == secondHalf:
						return n
						Palindrome = True
						break

				else:
					# Odd Digits
					# Get middle digit index
					middleIndex = (len(n) - 1) / 2
					middleIndex = int(middleIndex)

					# Convert string to mutable list
					digitList = []
					for digit in n:
						digitList.append(digit)
					digitList.pop(middleIndex)

					numberLength = len(digitList)
					halfLength = numberLength / 2
					halfLength = int(halfLength)
					firstHalf = digitList[:halfLength]
					secondHalf = digitList[halfLength:]
					secondHalf.reverse()
					if firstHalf == secondHalf:
						return n
						Palindrome = True
						
						break
				n = int(n)
				n = str(n)
				Palindrome = False

		def findNegativePalindrome(n):
			Palindrome = False
			while Palindrome == False:
				n = int(n) - 1
				n = str(n)
				if len(n) % 2 == 0:

					# Even Digits
					digitList = []
					for digit in n:
						digitList.append(digit)
					numberLength = len(digitList)
					halfLength = numberLength / 2
					halfLength = int(halfLength)
					firstHalf = digitList[:halfLength]
					secondHalf = digitList[halfLength:]
					secondHalf.reverse()

					
					if firstHalf == secondHalf:
						return n
						Palindrome = True
						break

				else:
					# Odd Digits
					# Get middle digit index

					middleIndex = (len(n) - 1) / 2
					middleIndex = int(middleIndex)

					# Convert string to mutable list
					digitList = []
					for digit in n:
						digitList.append(digit)
					digitList.pop(middleIndex)

					numberLength = len(digitList)
					halfLength = numberLength / 2
					halfLength = int(halfLength)
					firstHalf = digitList[:halfLength]
					secondHalf = digitList[halfLength:]
					secondHalf.reverse()
					if firstHalf == secondHalf:
						return n
						Palindrome = True
						
						break
				n = int(n)
				n = str(n)
				Palindrome = False

		if int(n) <= 10:
			
			a = int(n)-1
			a = str(a)
			return a

		if int(n) == 11:
			a = 9
			a = str(a)
			return a


		pos = findPositivePalindrome(n)
		neg = findNegativePalindrome(n)
		pos = int(pos)
		neg = int(neg)
		posAbs = abs(int(n) - pos)
		negAbs = abs(int(n) - neg)

		print(posAbs)
		print(negAbs)

		if posAbs < negAbs:
			print(n, "closest palindrome is", pos)
			return str(pos)
		else:
			print(n, "closest palindrome is", neg)
			return str(neg)



answer = Solution.nearestPalindromic("", "88")
print(answer)