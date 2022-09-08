import hashlib
import itertools, more_itertools
import random

#nonces = list(more_itertools.repeatfunc(random.randint, 0, 9872346873468, times=5))
#print(nonces)

def solve(dif, msg):
	while True:
		nonce = random.randint(0, 89698710)
		h = hashlib.sha256()
		h.update(bytes(msg))
		h.update(bytes(nonce))
		dig = h.hexdigest()
		#print("{:e}".format(int(dig, base=16)), dif, int(dig, base=16) <= dif)
		if int(dig, base=16) <= dif:
			return nonce