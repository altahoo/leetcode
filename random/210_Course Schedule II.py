# 210. Course Schedule II

# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_courses = collections.defaultdict(set)
        course_pre_count = [0] * numCourses

        for course, pre in prerequisites:
            pre_courses[pre].add(course)
            course_pre_count[course] += 1
        
        result = []
        queue = collections.deque([])
        for course, pre_count in enumerate(course_pre_count):
            if pre_count == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            result.append(course)
            for pre in pre_courses[course]:
                course_pre_count[pre] -= 1
                if course_pre_count[pre] == 0:
                    queue.append(pre)
        
        return result if len(result) == numCourses else []