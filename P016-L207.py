# https://leetcode.com/problems/course-schedule/
# Runtime: 88 ms -> beats 66.57% of users with Python3

class Solution:
    def canTake(self, course: int) -> bool:
        if self.taken[course] == True: return True
        if self.taken[course] == False: return False
        # Here, self.taken[course] is None
        self.taken[course] = False
        if course in self.prereq:
            for req in self.prereq[course]:
                if not self.canTake(req):
                    return False
        self.taken[course] = True
        return True
    # end canTake

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Preprocess prerequisites
        self.prereq: dict[int, list[int]] = {}
        for pair in prerequisites:
            if pair[0] in self.prereq:
                self.prereq[pair[0]].append(pair[1])
            else:
                self.prereq[pair[0]] = [pair[1]]
        # Check if each course can be taken
        self.taken: list[bool] = [None] * numCourses
        for i in range(numCourses):
            if not self.canTake(i):
                return False
        return True
    # end canFinish
# end Solution

if __name__ == "__main__":
    sol = Solution()
    assert sol.canFinish(2, [[1,0]]) == True
    assert sol.canFinish(2, [[1,0],[0,1]]) == False
