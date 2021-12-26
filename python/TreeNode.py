from utils import getHash

'''
Class: MerkleTreeNode
@property Right Node -> NULL
@property Left Node -> NULL
@property Value
@property Hash Value
'''
class MerkleTreeNode:
	def __init__(self, value, left=None, right=None):
		self._right = left
		self._left = right
		self._value = value
		self._hashValue = self._evaluate()

	def _evaluate(self):
		if (self._left):
			assert isinstance(self._left, str), "left child's value not of type (str)"
		if (self._right):
			assert isinstance(self._right, str), "right child's value not of type (str)"
		return getHash(self._value)

	@property
	def value(self):
		return self._value

	@property
	def hashValue(self):
		return self._hashValue

