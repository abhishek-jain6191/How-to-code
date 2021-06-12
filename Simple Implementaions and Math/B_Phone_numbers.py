from sys import stdin,stdout
from heapq import heapify,heappush,heappop,heappushpop
from collections import defaultdict as dd, deque as dq,Counter as C
from bisect import bisect_left as bl ,bisect_right as br
from itertools import combinations as cmb,permutations as pmb
from math import factorial as f ,ceil,gcd,sqrt,log,inf
mi = lambda : map(int,input().split())
ii = lambda: int(input())
li = lambda : list(map(int,input().split()))
mati = lambda  r : [ li() for _ in range(r)]
lcm = lambda a,b : (a*b)//gcd(a,b) 
MOD=10**9+7
def soe(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return(prime)
def ncr(n,r):
    p,k=1,1
    if (n - r < r):
        r = n - r
    if r!=0:
        while(r):
            p,k=p*n,k*r
            m=gcd(p,k)
            p,k=p//m,k//m
            n,r=n-1,r-1
    else:
            p=1
    return(p)




def solve():
    n=ii()
    s=input()
    if n%2==0:
        print(s[0:2],end="")
        if n!=2:
            print("-",end="")
        cp=0
        for x in range(2,n):
            print(s[x],end="")
            cp+=1
            if cp%2==0 and x!=n-1:
                print("-",end="")
    else:
        print(s[0:3],end="")
        if n!=3:
            print("-",end="")
        cp=0
        for x in range(3,n):
            print(s[x],end="")
            cp+=1
            if cp%2==0 and x!=n-1:
                print("-",end="")
for _ in range(1):
    solve()