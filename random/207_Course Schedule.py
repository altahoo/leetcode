# 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_to_courses = collections.defaultdict(set)
        course_pre_count = [0] * numCourses
        for course, prerequisite in prerequisites:
            pre_to_courses[prerequisite].add(course)
            course_pre_count[course] += 1

        queue = collections.deque([])
        for i in range(numCourses):
            if course_pre_count[i] == 0:
                queue.append(i)  
        while queue:
            course = queue.popleft()
            for next_course in pre_to_courses[course]:
                course_pre_count[next_course] -= 1
                if course_pre_count[next_course] == 0:
                    queue.append(next_course)

        course_pre_count = set(course_pre_count)
        return course_pre_count == set([0])