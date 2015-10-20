import random
import copy

def buildGraph(f):
	graph = {}
	for line in f:
		split = line.split()
		splitInts = [int(a) for a in split]
		graph[(splitInts[0],)] = splitInts[1:]
	return graph

def karger(graph):
	while len(graph) > 2:
		start = random.choice(graph.keys())
		choice = random.choice(graph[start])
		for k in graph.keys():
			if choice in k:
				graph[start + k] = [i for i in graph[k] + graph[start] if i not in start + k]
				del graph[k], graph[start]
	return graph
		
def runIteration(graph, n):
	minimum = None
	for i in range(n):
		graphCopy = copy.deepcopy(graph)
		cut = karger(graphCopy)
		length = len(cut.values()[0])
		if length < minimum or minimum is None:
			minimum = length
	return minimum

f = open('kargerMinCut.txt', 'r')
graph = buildGraph(f)
print runIteration(graph, 100)