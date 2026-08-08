class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereq = {c:[] for c in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)
        
        output = []
        visit, cycle = set(),set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return output