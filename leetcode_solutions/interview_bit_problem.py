## wt = [20,50,35] ; cap = 50
## val = [60, 100, 140]
def solution(weights, values, capacity):
    n = len(values)
    def score(i):
        return values[i]/weights[i]
    scores = sorted(range(n), key=score, reverse = True)
    optimized = []
    value = 0
    weight = 0
    for i in scores:
        if weight + weights[i] <= capacity:
            optimized += [i]
            weight += weights[i]
            value += values[i]
        elif weight < capacity and weight + weights[i] > capacity:
            optimized += [i]
            value += (capacity - weight) * (values[i]/weights[i])
            weight += (capacity - weight)
    return optimized, weight, value
    

wt = [20,50,35]
val = [60,100,140] 
cap = 50
ans = solution(wt,val,cap)
print(ans)   