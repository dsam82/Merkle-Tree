# MerkleTree

> Contains a beginner's guide implementation for merkle tree in Python

## Getting Started

Construct tree, generate proof, and verify proofs.

### Construct Merkle Tree

```python
from merkletree import MerkleTree

# file for tree details
outfile = open("merkletree.out", "w")
const tree = MerkleTree(['a', 'b', 'c'], outfile)
print(tree.block_header)

outfile.close()
```

outfile

```text
Left Child -> value: a, hash: ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
Right Child -> value: b, hash: 3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d
Parent created -> value: ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d, hash: 62af5c3cb8da3e4f25061e829ebeea5c7513c54949115b1acc225930a90154da
```

### Generate and Verify Proof

```python
from merkleproof import MerkleProof
from merkletreenode import MerkleTreeNode
from utils import getHash

const tx = MerkleTreeNode('d')

proof = MerkleProof(tree, tx)

print(proof.merkleProof)

# verify Proof
const hash = getHash(tx.value)
print(proof.verifyProof(hash))
```

## Credits

- [Bitcoin Fundamentals](https://youtu.be/2kPFSoknlUU)
- [Blockchain-for-Developers](https://github.com/Blockchain-for-Developers/merkle-tree)
- [MerkleTree.js](https://github.com/miguelmota/merkletreejs)
