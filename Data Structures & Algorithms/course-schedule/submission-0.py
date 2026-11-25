class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph = {node: [] for node in range(n)}
        in_degree = [0] * n

        for pre, course in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        queue = deque([node for node in range(n) if in_degree[node] == 0])

        num_taken = 0
        while queue:
            course = queue.popleft()
            num_taken += 1
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        # if the number of courses able to be taken is not equal to n,
        # it is impossible to complete the courses (graph cycle)
        return num_taken == n


