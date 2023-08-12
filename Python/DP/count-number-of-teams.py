'''
n <= 1000 이므로 combinations 사용 불가능

'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0

        up = [0] * n    # 나보다 큰 개수
        down = [0] * n  # 나보다 작은 개수
        ans = 0

        for i in range(n-1):
            for j in range(i+1, n):
                if rating[j] > rating[i]:
                    up[i] += 1
                else:
                    down[i] += 1
       
        for i in range(n-2):
            for j in range(i+1, n):
                if rating[j] > rating[i]:   # i 위치에서 j위치가 오름차순인 경우 ~> up[j]를 더해주면 됨
                    ans += up[j]
                else:                       # i 위치에서 j위치가 내림차순인 경우 ~> down[j]를 더해주면 됨
                    ans += down[j]

        return ans
