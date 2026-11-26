class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {u: [] for u in range(n)}
        for s, d, w in edges:
            graph[s].append((d, w))
        
        distances = [float('inf')] * n
        distances[src] = 0
        heap = [(0, src)]
        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distances[node]:
                continue            

            for neighbor, weight in graph[node]:
                candidate = dist + weight
                if candidate < distances[neighbor]:
                    distances[neighbor] = candidate
                    heapq.heappush(heap, (candidate, neighbor))
        
        shortest = {}
        for node, distance in enumerate(distances):
            shortest[node] = distance if distance != float('inf') else -1
        return shortest
                