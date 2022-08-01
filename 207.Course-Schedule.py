from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visitSet = set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs] = []
            visitSet.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


numCourses = 2
prerequisites = [[1, 0]]
solution = Solution()
print(solution.canFinish(numCourses, prerequisites))
