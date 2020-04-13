

class Solution(object):
	
	def run(self, n):

		def findPositivePalindrome(n):
			Palindrome = False
			while Palindrome == False:
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
				n = int(n) + 1
				n = str(n)
				Palindrome = False

		def findNegativePalindrome(n):
			Palindrome = False
			while Palindrome == False:
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
				n = int(n) - 1
				n = str(n)
				Palindrome = False


		pos = findPositivePalindrome(n)
		neg = findNegativePalindrome(n)
		pos = int(pos)
		neg = int(neg)

		print(pos, neg)
		posAbs = abs(int(n) - pos)
		negAbs = abs(int(n) - neg)

		print(posAbs, negAbs)

		if posAbs > negAbs:
			return neg
		else:
			return pos



Solution.run("", "555")