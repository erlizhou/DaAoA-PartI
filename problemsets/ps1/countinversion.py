def sortAndCount(A, n):
	if n == 1:
		return (A, 0)
	mid = len(A) / 2
	lefthalf = A[:mid]
	righthalf = A[mid:]
	(B, X) = sortAndCount(lefthalf, len(lefthalf))
	(C, Y) = sortAndCount(righthalf, len(righthalf))
	(D, Z) = countSplitInv(B, C, n)
	return (D, X + Y + Z)

def countSplitInv(B, C, n):
	count = i = j = 0
	D = [0 for x in range(n)]
	for k in range(n):
		while i < len(B) and j < len(C):
			if B[i] < C[j]:
				D[k] = B[i]
				i += 1
			else:
				D[k] = C[j]
				j += 1
				count += len(B[i:])
			k += 1
		while i < len(B):
			D[k] = B[i]
			i += 1
			k += 1
		while j < len(C):
			D[k] = C[j]
			j += 1
			k += 1
	return (D, count)


filename = 'IntegerArray.txt'
f = open(filename, 'r')
array = []
for line in f:
	array.append(int(line))
(final, inversion) = sortAndCount(array, len(array))
print inversion
