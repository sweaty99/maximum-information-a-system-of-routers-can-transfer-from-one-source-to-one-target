from heapq import heapify, heappush, heappop
import math
def adj_list(n,newlinks):
    
    ans = [(i,[])  for i in range(0,n)]
    for ((a,b),c) in newlinks:
        
        ans[a][1].append((c,b))
        
    return ans

def newlinks(links):
    ans = {}
    for (a,b,c) in links :
        ans[(a,b)]=0
        ans[(b,a)]=0
    for (a,b,c) in links :
        ans[(a,b)]=min(c,ans[(a,b)])
        ans[(b,a)]= ans[(a,b)]

    return list(ans.items())


def findMaxCapacity(n,links,s,t):
    for i in range(len(links)):
        (a,b,c)= links[i]
        links[i]= (a,b,-c)
    a= newlinks(links)
    adjlist  = adj_list(n,a)
    
    maxcap = [[0,[s]] for i in range(n) ]
    maxcap[s][0]= math.inf
    heap = []
    heapify(heap)
    heappush(heap, (math.inf,s))
    while len(heap)!= 0 :
        (cap , node) = heappop(heap)
        for (edge, nbr) in adjlist[node][1]:
            edge = -edge
            if maxcap[nbr][0]< min(cap,edge) :
                maxcap[nbr][0]= min(cap,edge)
                maxcap[nbr][1]= maxcap[node][1]+[nbr]
                
                heappush(heap,(maxcap[nbr][0],nbr))

    return maxcap[t]
    
