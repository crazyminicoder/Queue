# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
class Solution:
    def sandwiches(self, student: list[int], sandwiches: list[int]) -> int:
        sandwichLover = student.count(1)
        burgerLover = student.count(0)

        for i in range(len(sandwiches)):
            food = sandwiches[i]

            if food == 1:
                if not sandwichLover:
                    return burgerLover

                sandwichLover -= 1

            else:
                if not burgerLover:
                    return sandwichLover

                burgerLover -= 1

        return 0


res = Solution()
ans = res.sandwiches([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])
print(ans)
