class Solution:
    def trap(self, height) -> int:
        stack = []
        water = 0
        for idx, item in enumerate(height):
            # 스택 pop 과정
            while stack and stack[-1][1] < item:
                cache = stack.pop()
                if not stack:
                    break
                water += ((idx - stack[-1][0] - 1) *
                          (min(stack[-1][1], item)-cache[1]))

            stack.append((idx, item))
        return water


sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
