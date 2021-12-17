fib = [0,1]
n = int(input("Enter a number: "))
mincount = 0
for i in range(2,n):
    fib.append(fib[i-1] + fib[i-2])
j = 0
for j in range(n-1):
    if fib[j] <= n and fib[j+1] >= n+1:
        break;
mincount = min(n - fib[j], fib[j+1] - n)
print(mincount) 
    
