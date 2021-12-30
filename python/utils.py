import hashlib
from python.merkletreenode import MerkleTreeNode

def getHash(value):
	"""
	@function create hash from value
	"""
	return hashlib.sha256(value.encode('utf-8')).hexdigest()

def merkleNodesFromList(txs: list) -> list:
	"""
	@function create merkle tree nodes from list of tx
	@param txs {list} transactions for merkle nodes
	@return listNodes {list} list of merkle nodes
	"""
	listNodes = []
	for tx in txs:
		listNodes.append(MerkleTreeNode(tx))
	return listNodes

def makePair(txs: list) -> list:
	"""
	@function make pairs from a list
	@param lst {list} list from which pairs to be made
	@return pairs {list} list of pairs
	"""
	pairs = []
	length = len(txs)
	for i in range(0, length, 2):
		if i+1 == length:
			pairs.append((txs[i],None))
			break
		pairs.append((txs[i], txs[i+1]))

	return pairs