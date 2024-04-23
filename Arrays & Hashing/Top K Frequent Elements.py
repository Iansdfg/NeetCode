from heapq import(
    heappush,
    heappop
)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnt = {}
        for num in nums:
            num_cnt[num] = num_cnt.get(num, 0) + 1
        
        heap = []
        for num in num_cnt:
            heappush(heap, (-1 * num_cnt[num], num))

        res = []
        for _ in range(k):
            cnt, num = heappop(heap)
            res.append(num)
        return res 


        
