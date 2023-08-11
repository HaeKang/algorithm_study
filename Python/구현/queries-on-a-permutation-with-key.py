'''
https://leetcode.com/problems/queries-on-a-permutation-with-key/description/
처음엔 딕셔너리를 통해 풀었는데 생각보다 성능이 좋지않다 ㅎ;
다른 답을 보니 insert, index, remove를 통해 풀었더라. 이 방법이 시간이 더 짧다!
'''

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        # 1번 
        ans = []
        dic = {i : i - 1 for i in range(1, m+1)} # key : 값, value : idx

        for q in queries:
            ans.append(dic[q])

            for key in dic: 
                if dic[key] < dic[q]:
                    dic[key] += 1
            
            dic[q] = 0

        # 2번 
        ans = []
        arr = [i for i in range(1, m+1)]

        for q in queries:
            ans.append(arr.index(q))
            arr.remove(q)
            arr.insert(0, q)
        
        return ans
