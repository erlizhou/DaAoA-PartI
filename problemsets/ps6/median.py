import heapq

def main():
	maxHeap = []
	minHeap = []
	f = open('Median.txt', 'r')
	total = 0
	for line in f:
		if len(maxHeap) == 0 or int(line) < -maxHeap[0]:
			heapq.heappush(maxHeap, -int(line))
		else:
			heapq.heappush(minHeap, int(line))
		if len(maxHeap) > len(minHeap) + 1:
			item = heapq.heappop(maxHeap)
			heapq.heappush(minHeap, -item)
		elif len(minHeap) > len(maxHeap) + 1:
			item = heapq.heappop(minHeap)
			heapq.heappush(maxHeap, -item)
		if len(maxHeap) >= len(minHeap):
			total += -maxHeap[0]
		else:
			total += minHeap[0]
	return total % 10000

print main()