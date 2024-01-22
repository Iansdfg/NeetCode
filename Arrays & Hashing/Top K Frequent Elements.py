import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_cnt = {}
        for i in range(len(nums)):
            if nums[i] not in num_cnt:
                num_cnt[nums[i]] = 1 
            else:
                num_cnt[nums[i]] += 1 

        heap = []
        for num in num_cnt:
            pair = (num_cnt[num] * -1, num)
            heapq.heappush(heap, pair)

        res = []
        for _ in range(k):
            cnt, num = heapq.heappop(heap)
            res.append(num)

        return res 




            
