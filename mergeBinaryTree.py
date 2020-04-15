# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def mergeTrees(self, t1, t2):
		"""
		:type t1: TreeNode
		:type t2: TreeNode
		:rtype: TreeNode
		"""
		mergedTrees = []
		lent1 = len(t1)
		lent2 = len(t2)

		if lent2>lent1:
			for i in range(len(t2)):
				try:
					if t1[i] != "null" and t2[i] != "null":
						mergedTrees.append(t2[i] + t1[i])
					elif t1[i] == "null" and t2[i] != "null":
						mergedTrees.append(t2[i])
					elif t2[i] == "null" and t1[i] != "null":
						mergedTrees.append(t1[i])
				except:
					mergedTrees.append(t2[i])

		if lent1>lent2:
			for i in range(len(t1)):
				try:
					if t2[i] != "null" and t1[i] != "null":
						mergedTrees.append(t1[i] + t2[i])
					elif t2[i] == "null" and t1[i] != "null":
						mergedTrees.append(t1[i])
					elif t1[i] == "null" and t2[i] != "null":
						mergedTrees.append(t2[i])
				except:
					mergedTrees.append(t1[i])
		return mergedTrees


Solution.mergeTrees("", [1,3,2,5], [2,1,3,"null",4,"null",7])