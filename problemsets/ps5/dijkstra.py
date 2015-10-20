def buildGraph(f):
	graph = {}
	for line in f:
		split = line.strip().split()
		node, edges = int(split[0]), split[1:]
		store = []
		for e in edges:
			esplit = e.split(',')
			store.append((int(esplit[0]), int(esplit[1])))
		graph[node] = store
	return graph

def dijkstra(source, graph):
	X = [source]
	A, B = {}, {}
	A[source] = 0
	B[source] = []
	while sorted(X) != graph.keys():
		minimum = None
		w = None
		source = None
		for v in X:
			for edge in graph[v]:
				if edge[0] not in X:
					if minimum == None or A[v] + edge[1] < minimum:
						minimum = A[v] + edge[1]
						w = edge[0]
						source = v
		X.append(w)
		A[w] = minimum
		B[w] = B[source] + [w]
	return A, B

def main():
	f = open('dijkstraData.txt', 'r')
	graph = buildGraph(f)
	source = 1
	A, B =  dijkstra(source, graph)
	vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
	for v in vertices:
		print A[v], B[v]

main()