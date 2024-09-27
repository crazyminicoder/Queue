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
