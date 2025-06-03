import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        k = len(nums)
        
        min_heap = []
        
        current_max_val = -float('inf')

        for i in range(k):
            
            element = nums[i][0]
            heapq.heappush(min_heap, (element, i, 0))
            current_max_val = max(current_max_val, element)

        ans_start = min_heap[0][0] 
        ans_end = current_max_val
        min_range_diff = ans_end - ans_start


        while True:
    
            val, list_idx, element_idx_in_list = heapq.heappop(min_heap)

            current_diff = current_max_val - val
            if current_diff < min_range_diff:
                min_range_diff = current_diff
                ans_start = val
                ans_end = current_max_val
            elif current_diff == min_range_diff and val < ans_start:
      
                ans_start = val
                ans_end = current_max_val
            
            element_idx_in_list += 1

            if element_idx_in_list == len(nums[list_idx]):
                break # Terminate the loop
            
            next_element_val = nums[list_idx][element_idx_in_list]
            heapq.heappush(min_heap, (next_element_val, list_idx, element_idx_in_list))
            
            current_max_val = max(current_max_val, next_element_val)
            
        return [ans_start, ans_end]