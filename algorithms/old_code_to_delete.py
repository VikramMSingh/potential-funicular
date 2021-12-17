 for i in range(l):
            if nums[i] == target:
                return i 
            elif target not in nums:
                mid = l//2
                if target < nums[mid]:
                    for j in range(0,mid):
                        if target < nums[j]:
                            return j 
                            break;
                elif target > nums[mid]:
                    for j in range(mid, l):
                        if target > max(nums):
                            return l
