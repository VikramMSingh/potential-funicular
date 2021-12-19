def greedy_knapsack(values,weights,capacity):
    n = len(values)
    def score(i):
        return  values[i]/weights[i]
    items = sorted(range(n), key=score, reverse = True)
    optimized = []
    value = 0 
    weight = 0
    for i in items:
        if weight + weights[i] <= capacity:
            optimized += [i]
            weight += weights[i]
            value += values[i]
        elif weight < capacity and weight + weights[i] > capacity:
            optimized += [i]
            value += (capacity - weight) * (values[i]/weights[i])
            weight += capacity - weight
    return optimized, value, weight
    

wt = [5,10,15,22,25]
vl = [30,40,45,77,90]
capacity = 60

print(greedy_knapsack(vl, wt, capacity))
