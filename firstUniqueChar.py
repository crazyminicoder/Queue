# Example 1:
# Input: s = "leetcode"
# Output: 0

# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

class Solution:
    def uniqueChar(self, s: str):
        unique = set()
        queue = []
        for i in s:
            if i not in unique:
                queue.append(i)
                unique.add(i)
            else:
                if i in queue:
                    queue.remove(i)

        if queue:
            return s.index(queue[0])
        else:
            return -1


res = Solution()
ans = res.uniqueChar('leelcode')
print(ans)
