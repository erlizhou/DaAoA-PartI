def quickSort(A, n):
	if n <= 1:
		return 0
	index = choosePivot3(A, n)
	m = n - 1
	A1, A2 = partition(A, 0, n - 1, index)
	m1 = quickSort(A1, len(A1))
	m2 = quickSort(A2, len(A2))
	return m + m1 + m2

def partition(A, l, r, index):
	p = A[index]
	A[index], A[l] = A[l], A[index]
	i = l + 1
	for j in range(l + 1, r + 1):
		if A[j] < p:
			A[j], A[i] = A[i], A[j]
			i += 1
	A[l], A[i - 1] = A[i - 1], A[l]
	return A[:i - 1], A[i:]

def choosePivot1(A, n):
	return 0

def choosePivot2(A, n):
	return -1

def choosePivot3(A, n):
	if n % 2 == 0:
		mid = n / 2 - 1
	else:
		mid = (n - 1) / 2
	if A[mid] >= A[0] and A[0] >= A[-1]:
		return 0
	elif A[mid] < A[0] and A[0] < A[-1]:
		return 0
	elif A[mid] < A[0] and A[0] >= A[-1]:
		if A[mid] >= A[-1]:
			return mid
		else:
			return -1
	elif A[mid] >= A[0] and A[0] < A[-1]:
		if A[mid] >= A[-1]:
			return -1
		else:
			return mid

filename = 'QuickSort.txt'
f = open(filename, 'r')
array = []
for line in f:
	array.append(int(line))
comparison = quickSort(array, len(array))
print comparison