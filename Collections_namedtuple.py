from collections import namedtuple
n = int(input())
marks = input().split().index('MARKS')
print(f"{sum(float(input().split()[marks]) for _ in range(n)) / n:.2f}")