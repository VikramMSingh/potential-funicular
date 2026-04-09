# ...existing code...
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # left: start index of the current sliding window
        left = 0 
        # zero: how many zeros are inside the current window
        zero = 0

        # iterate over each index to expand the window to the right
        for i in range(len(nums)):
            # if we see a zero, increase zero count
            if nums[i] == 0:
                zero += 1

            # if more than one zero in window, move left forward until window has <= 1 zero
            if zero > 1:
                # when moving left, if we remove a zero from the window, decrement zero
                if nums[left] == 0:
                    zero -= 1
                left += 1

        # i - left is the size of the final window minus one (delete one element).
        # NOTE: this returns the value for the final window only. To get the correct
        # answer across the whole array, you should track the maximum (e.g. max_len)
        # inside the loop. Also this will raise an error if nums is empty because
        # `i` would be undefined.
        return i - left
#