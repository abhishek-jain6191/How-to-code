"""
https://www.codechef.com/LTIME95B/problems/ARRROT
"""
from sys import stdin
input = stdin.readline
from heapq import heapify,heappush,heappop,heappushpop
from collections import defaultdict as dd, deque as dq,Counter as C
from math import factorial as f ,ceil,gcd,sqrt,log
from bisect import bisect_left as bl ,bisect_right as br
from itertools import combinations as c,permutations as p
from math import factorial as f ,ceil,gcd,sqrt,log
mi = lambda : map(int,input().split())
ii = lambda: int(input())
li = lambda : list(map(int,input().split()))
mati = lambda  r : [ li() for _ in range(r)]
lcm = lambda a,b : (a*b)//gcd(a,b) 




def solve():
    MOD=10**9+7
    n=ii()
    arr=li()
    q=ii()
    s=sum(arr)
    for x in range(q):
        p=li()
        s*=2
        s%=MOD
        print(s)
for _ in range(1):
    solve()