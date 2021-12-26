'''
Author: dsam82 [http://github.com/dsam82]
Source:
- (https://github.com/droid76/Merkle-Tree)
- (https://github.com/Blockchain-for-Developers/merkle-tree)
'''

import sys
from TreeNode import MerkleTreeNode


'''
Merkle Tree implementation with default hash function sha256
Arbitrary amount of nodes can be added, in consequence of which
tree will be reconstructed by appending the new txs into the current txs
'''
class MerkleTree:
	def __init__(self, txs, outfile):
		assert txs, "No transaction to be hashed"
		assert isinstance(txs, list), "txs not a list"
		self._leaves = txs
		self._nodes = []
		self._root = self._buildMerkleTree()
		self._block_header = self._root.hashValue
		self._outfile = outfile

	'''
	Builds Simple Binary Merkle Tree and saves nodes in file
	'''
	def _buildMerkleTree(self):
		leaves = []
		for leaf in self._leaves:
			leaves.append(MerkleTreeNode(leaf))

		while len(leaves) != 1:
			temp = []
			length = len(leaves)
			for i in range (0, length, 2):
				if (i+1 == length):
					temp.append(leaves[i])
					break

				leftChild = leaves[i]
				self._outfile.write("Left Child -> value: %s, hash: %s\n" % (leftChild.value, leftChild.hashValue))

				rightChild = leaves[i+1]
				self._outfile.write("Right Child -> value: %s, hash: %s\n" % (rightChild.value, rightChild.hashValue))

				parentValue = leftChild.hashValue + rightChild.hashValue
				parentNode = MerkleTreeNode(parentValue, leftChild, rightChild)
				self._outfile.write("Parent created -> value: %s, hash: %s\n" % (parentNode.value, parentNode.hashValue))

				temp.append(parentNode)
			leaves = temp

		return leaves[0]

	def _add_to_tree(self):
		self._root = self._buildMerkleTree()
		self._block_header = self._root.hashValue

	def add_txs(self, new_txs):
		assert new_txs, "No new transaction to be added"
		assert isinstance(new_txs, list), "new_tns not a list"
		self._leaves.append(new_txs)
		self._add_to_tree()

	'''Return tree's txs list'''
	@property
	def leaves(self):
		return self._leaves

	'''Return tree root'''
	@property
	def root(self):
		return self._root

	'''Return tree root's hash value'''
	@property
	def block_header(self):
		return self._block_header


def main():
	if (len(sys.argv) == 1):
		print("Enter filename")
		return

	filename = sys.argv[1]
	assert filename, "invalid file"

	with open(filename) as file:
		lines = file.readlines()
		lines = [line.rstrip() for line in lines]

	assert len(lines) > 1, "invalid txs"

	outfile = open("merkletree.out", "w")

	merkleRoot = MerkleTree(lines, outfile)
	print(merkleRoot.root)

	outfile.close()


if __name__=="__main__":
	main()