from collections import defaultdict
import sys 
import resource
 
#set rescursion limit and stack size limit
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

maxNode = 875714
t = 0
s = None
visited = [False for i in range(maxNode + 1)]
leader = [0 for i in range(maxNode + 1)]
finish = [None for i in range(maxNode + 1)]

def buildGraph(f):
	graph, reversedGraph = {i: [] for i in range(1, maxNode + 1)}, {i: [] for i in range(1, maxNode + 1)}
	for line in f:
		split = line.split()
		splitInts = [int(a) for a in split]
		graph[splitInts[0]].append(splitInts[1])
		reversedGraph[splitInts[1]].append(splitInts[0])
	return graph, reversedGraph

def dfsLoop(graph):
	global s
	for i in sorted(graph.keys(), reverse = True):
	    if graph[i] and visited[i] is False:
			s = i
			dfs(graph, i)

def dfs(graph, i):
	global t, visited, finish, leader
	visited[i] = True
	leader[i] = s
	for j in graph[i]:
		if visited[j] is False:
			dfs(graph, j)
	t += 1
	finish[i] = t

def dfsNewLoop(graph):
	global s
	count = finish.count(None)
	finishWithoutNone = [f for f in finish if f is not None]
	print finishWithoutNone, count
	index = sorted(range(len(finishWithoutNone)), key = lambda k: finishWithoutNone[k], reverse = True)
	updatedIndex = [i + count for i in index]
	print updatedIndex
	for i in updatedIndex:
		if visited[i] is False:
			s = i
			dfs(graph, i)

def main():
	global visited
	f = open('SCCtest.txt', 'r')
	G, Grev = buildGraph(f)
	dfsLoop(Grev)
	print finish
	print G
	visited = [False for i in range(maxNode + 1)]
	dfsNewLoop(G)
	counts = defaultdict(int)
	for x in leader[1:]:
		counts[x] += 1
	print sorted(counts.items(), reverse = True, key = lambda tup: tup[1])[:5]

main()