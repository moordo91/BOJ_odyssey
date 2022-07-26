def solution(nums):
    n = len(nums)
    nums2 = set(nums)
    answer = min(len(nums2), n//2)    
    return answer