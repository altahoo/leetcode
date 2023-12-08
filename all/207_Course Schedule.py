# 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_prerequisites = collections.defaultdict(int)
        prerequisite_courses = collections.defaultdict(set)
        for course, prerequisite in prerequisites:
            course_prerequisites[course] += 1
            prerequisite_courses[prerequisite].add(course)
        
        queue = collections.deque()
        for i in range(numCourses):
            if i not in course_prerequisites:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            for course in prerequisite_courses[cur]:
                course_prerequisites[course] -= 1
                if course_prerequisites[course] == 0:
                    del course_prerequisites[course]
                    queue.append(course)
        return not course_prerequisites
