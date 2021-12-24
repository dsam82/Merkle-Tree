import sys
from merkletree import buildMerkleTree

def parseFile(filePath):
	lines = []
	tree = {}
	with open(filePath, "r") as file:
		lines = file.readlines()
		if (len(lines)) < 1:
			print("invalid file")
			return
	file.close()

	for line in lines:
		lineSplit = line.split(" ")
		tree[lineSplit[4][:-1]] = lineSplit[6]

	return tree

def searchTree(tree, searchVal):
	if (not tree or searchVal == ""):
		return None

	vals = []
	for key, val in tree.items:
		if searchVal in key:
			vals.append(val)
			searchVal = val

	return vals

def main():
	if (len(sys.argv) < 3):
		print("Enter filename and search string")
		return

	filePath = sys.argv[1]
	searchStr = sys.argv[2]
	if (filePath == "" or searchStr == ""):
		print("Enter valid args")
		return

	tree = parseFile(filePath)
	val = searchTree(tree, searchStr)
	if (val):
		print("Yes", val)
	else:
		print("No")



if __name__=="__main__":
	main()