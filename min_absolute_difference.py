def minimumAbsDifference(arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """ 
        l = len(arr)
        curr_min=abs(arr[0]-arr[1])
        ans = []
        for i in range(0,l-1):
            curr_min = min(abs(curr_min), abs(arr[i]-arr[i+1]))
        #print(curr_min)
        for i in range(0,l-1):
            for j in range(i+1,l):
                if abs(arr[i]-arr[j]) == curr_min and abs(arr[j]-arr[i]) == curr_min:
                    x = [arr[j],arr[i]]
                    ans.append(sorted(x))
        return sorted(ans)

#Does not work correctly with negative number - attempted without sorting

a = [3,5,4,1,6]
solution = minimumAbsDifference(a)
print(solution)
