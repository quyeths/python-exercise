from typing import List


class Solution:
    """
    @param n: An interger
    @param edges: a list of undirected edges
    return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {i: [] for i in range(n)}
        visit = set()

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if dfs(j, i) == False:
                    return False

            return True

        return dfs(0, -1) and n == len(visit)
