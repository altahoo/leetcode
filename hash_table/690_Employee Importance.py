# 690. Employee Importance

# You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

# You are given an array of employees employees where:

# employees[i].id is the ID of the ith employee.
# employees[i].importance is the importance value of the ith employee.
# employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
# Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_to_employee = {employee.id: employee for employee in employees}
        queue = collections.deque([id_to_employee[id]])
        result = 0
        while queue:
            cur = queue.popleft()
            result += cur.importance
            for subbordinate_id in cur.subordinates:
                queue.append(id_to_employee[subbordinate_id])
        return result