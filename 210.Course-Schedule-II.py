from typing import List


class Solution:
    def findOrder(self, numCourses: int, prereqisites: List[List[int]]) -> List[int]:
        prereq = {course: [] for course in range(numCourses)}
        for course, pre in prereqisites:
            prereq[course].append(pre)
        result = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False
            visited.add(course)
            cycle.remove(course)
            result.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return result
