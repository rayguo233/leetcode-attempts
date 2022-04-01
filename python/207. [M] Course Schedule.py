from typing import List, Tuple, Optional, Dict
from collections import defaultdict, deque, Counter


class Solution:

    def canFinish(self, num_courses: int,
                  prerequisites: List[List[int]]) -> bool:
        num_course_taken = 0
        course_to_satisfy = [[] for _ in range(num_courses)]
        course_to_num_need = [0 for _ in range(num_courses)]
        for prereq, course in prerequisites:
            course_to_satisfy[prereq].append(course)
            course_to_num_need[course] += 1

        available_courses = [
            course for course, num_need in enumerate(course_to_num_need)
            if num_need == 0
        ]
        while available_courses:
            course_taken = available_courses.pop()
            num_course_taken += 1
            for course_satisfied in course_to_satisfy[course_taken]:
                course_to_num_need[course_satisfied] -= 1
                if course_to_num_need[course_satisfied] == 0:
                    available_courses.append(course_satisfied)

            course_to_satisfy[course_taken] = []

        return num_course_taken == num_courses


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    pass