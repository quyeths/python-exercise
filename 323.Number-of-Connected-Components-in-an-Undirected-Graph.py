from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        result = n

        def find(n):
            if par[n] != n:
                return find(par[n])
            return n

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        for node1, node2 in edges:
            result -= union(node1, node2)

        return result


edges = [[0, 1], [1, 2], [3, 4]]
n = 5
sol = Solution()
print(sol.countComponents(n, edges))
