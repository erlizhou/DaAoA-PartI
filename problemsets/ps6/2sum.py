def main():
	f = open('algo1-programming_prob-2sum.txt', 'r')
	table = []
	distinct = set()
	for line in f:
		table.append(int(line))
		distinct.add(int(line))
	counter = 0
	for i in range(-10000, 10001):
		if i % 100 == 0:
			print i
		for num in table:
			if i - num != num and i - num in distinct:
				counter += 1
				break
	return counter

print main()