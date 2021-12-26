import hashlib, sys

def getHash(value):
	return hashlib.sha256(value.encode('utf-8')).hexdigest()