import hashlib, sys

def getHash(value):
	return hashlib.sha256(value.encode('utf-8')).hexdigest()

class MerkleTreeNode:
	def __init__(self, value, left=None, right=None):
		self.right = left
		self.left = right
		self.value = value
		self.hashValue = getHash(value)

def buildMerkleTree(lines, outfile):
	leaves = []
	for line in lines:
		leaves.append(MerkleTreeNode(line))


	while len(leaves) != 1:
		temp = []
		length = len(leaves)
		for i in range (0, length, 2):
			if (i+1 == length):
				temp.append(leaves[i])
				break

			leftChild = leaves[i]
			rightChild = leaves[i+1]
			outfile.write("Left Child -> value: %s, hash: %s\n" % (leftChild.value, leftChild.hashValue))
			outfile.write("Right Child -> value: %s, hash: %s\n" % (rightChild.value, rightChild.hashValue))

			parentValue = leftChild.hashValue + rightChild.hashValue
			parentNode = MerkleTreeNode(parentValue, leftChild, rightChild)
			outfile.write("Parent created -> value: %s, hash: %s\n" % (parentNode.value, parentNode.hashValue))

			temp.append(parentNode)
		leaves = temp

	return leaves[0]


def main():
	if (len(sys.argv) == 1):
		print("Enter filename")
		return

	filename = sys.argv[1]
	if (filename == ""):
		print("Enter valid filename")
		return

	with open(filename) as file:
		lines = file.readlines()
		lines = [line.rstrip() for line in lines]

	if (len(lines) < 1):
		print("Invalid file")
		return

	outfile = open("merkletree.out", "w")

	merkleRoot = buildMerkleTree(lines, outfile)
	print(merkleRoot)

	outfile.close()


if __name__=="__main__":
	main()