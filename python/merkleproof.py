from python.merkletree import MerkleTree
from python.merkletreenode import MerkleTreeNode
from python.utils import getHash, merkleNodesFromList, makePair

class MerkleProofNode:
	"""
	node for merkle proof
	@property direction `bit` direction of node in the proof
	@property tx transaction to be verified
	"""
	def __init__(self, direction, tx):
		self._direction = direction
		self._tx = tx

	def __eq__(self, __o: object) -> bool:
		if isinstance(self, __o.__class__):
			return self.__dict__ == __o.__dict__
		return False

	@property
	def direction(self):
		return self._direction

	@property
	def tx(self):
		return self._tx

class MerkleProof:
	def __init__(self, tx: str, merkleTree: MerkleTree):
		assert tx, "empty tx"
		assert isinstance(merkleTree, MerkleTree), "invalid merkle tree"

		leaves = merkleTree.leaves
		assert tx in leaves, "invalid tx"

		self._merkleTree = merkleTree
		self._tx = tx
		self._merkleProof = self._buildMerkleProof()

	def _buildMerkleProof(self) -> list:
		"""
		@function build merkle proof and check for required nodes
		@param tx leaf nodes to make merkle proof from
		@param leaves merkle tree leaves
		"""
		try:
			tx = self._tx
			nodes = merkleNodesFromList(self._merkleTree.leaves)

			proof = []
			while len(nodes) != 1:
				temp = []
				pairs = makePair(nodes)
				for pair in pairs:
					parentValue = pair[0].hashValue + (pair[1].hashValue if not pair[1] != None else "")
					parentNode = MerkleTreeNode(parentValue, pair[0], pair[1])

					if tx in pair:
						idx = pair[0] == tx
						proof.append(MerkleProofNode(idx, pair[idx]))
						tx = parentNode
					temp.append(parentNode)

				nodes = temp

			return proof
		except Exception as e:
			print(e)
			return []

	def verifyProof(self, blockHeader: str) -> bool:
		"""
		@function verify merkle proof with block header without using the tree
		@param merkleProof merkle proof of the tree
		@param blockHeader block header to be verified against
		"""
		try:
			assert blockHeader, "empty blockheader"

			tx = self._tx

			for node in self._merkleProof:
				tx = getHash(node.hashValue + getHash(tx))

			return blockHeader == tx
		except Exception as e:
			print(e)
			return False


	@property
	def merkleTree(self):
		return self._merkleTree

	@property
	def tx(self):
		return self._tx

	@property
	def merkleProof(self):
		return self._merkleProof
