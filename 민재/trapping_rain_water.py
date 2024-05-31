class Solution:
    def trap(self, height: [int]) -> int:

        st = []

        temp_height = height[:]

        prev_idx = -1
        prev_height = -1

        for idx, h in enumerate(height):
            
            while st and st[-1][1] <= h:
                pop = st.pop()
                prev_idx = pop[0]
                prev_height = pop[1]
            
            # stack에 남아있다면 왼쪽이 더 크다.
            if st:
                for j in range(st[-1][0] + 1, idx):
                    temp_height[j] = h # 작은 오른쪽으로 채워줘야함.
            # stack이 비어있다면 '나'가 제일 크다. (오른쪽)
            else:
                for j in range(prev_idx + 1, idx):
                    temp_height[j] = prev_height
                


            st.append((idx, h))



        answer = 0
        for i in range(len(height)):
            answer += temp_height[i] - height[i]

        return answer
        