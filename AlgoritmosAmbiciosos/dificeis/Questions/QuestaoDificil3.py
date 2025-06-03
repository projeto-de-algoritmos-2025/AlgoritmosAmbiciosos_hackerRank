import collections

class Solution(object):
    def _prep(self, nums, k_digits):
        """
        Selects k_digits from nums to form the lexicographically largest number,
        preserving relative order.
        """
        if k_digits == 0:
            return []
        
        n = len(nums)
        stack = []
        
        to_drop = n - k_digits 
        
        for digit in nums:
            while stack and digit > stack[-1] and to_drop > 0:
                stack.pop()
                to_drop -= 1
            stack.append(digit)
            
  
        while len(stack) > k_digits:
            stack.pop()
            
        return stack

    def _merge(self, nums1_sub, nums2_sub):
        """
        Merges two lists of digits (maximized subsequences)
        to form the lexicographically largest combined number.
        """
        result = []
        q1 = collections.deque(nums1_sub)
        q2 = collections.deque(nums2_sub)
        
        while q1 or q2:
            if not q1:
                result.append(q2.popleft())
                continue
            if not q2:
                result.append(q1.popleft())
                continue
                      
            use_q1 = False 
            
            idx1, idx2 = 0, 0
            len_q1, len_q2 = len(q1), len(q2)
            determined = False
            while idx1 < len_q1 and idx2 < len_q2:
                if q1[idx1] != q2[idx2]:
                    if q1[idx1] > q2[idx2]:
                        use_q1 = True
                    determined = True
                    break
                idx1 += 1
                idx2 += 1
            
            if not determined: 
                if len_q1 > len_q2 : 
                    use_q1 = True
            
            if use_q1:
                result.append(q1.popleft())
            else:
                result.append(q2.popleft())
        
        return result

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        m, n = len(nums1), len(nums2)
        max_overall_candidate = [] 
        
       
        start_i = max(0, k - n) 
        end_i = min(k, m)     
        
        for i in range(start_i, end_i + 1):
            num_from_nums1 = i
            num_from_nums2 = k - i
            
            sub_nums1 = self._prep(nums1, num_from_nums1)
            sub_nums2 = self._prep(nums2, num_from_nums2)
            
            current_merged_candidate = self._merge(sub_nums1, sub_nums2)
            
            if not max_overall_candidate or current_merged_candidate > max_overall_candidate:
                max_overall_candidate = current_merged_candidate
                
        return max_overall_candidate