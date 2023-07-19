A=list(map(int,input().split()))
A.sort()
total_cost = 0
for i in range(len(A)):
    total_cost += sum(A[:i + 1])
print(total_cost)
