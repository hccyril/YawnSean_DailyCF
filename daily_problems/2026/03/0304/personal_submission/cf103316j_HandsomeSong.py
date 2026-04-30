class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*n
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x]=root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y]=root_x
            self.size[root_x] += self.size[root_y]
        return True
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)
MOD=10**9+7
n=int(input())
w=[0]+list(map(int,input().split()))
adj=[[] for _ in range(n+1)]
for _ in range(n_1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
def calc_sum(order):
    nodes=sorted(range(1,n+1),key=lambda x: w[x]*order)
    uf=UnionFind(n+1)
    vis=[False]*(n+1)
    total_sum=0
    for u in nodes:
        for v in adj[u]:
            if vis[v]:
                root_u=uf.find(u)
                root_v=uf.find(v)
                total_sum=(total_sum+w[u]*uf.size[root_u]*uf.size[root_v])%MOD
                uf.union(u,v)
        vis[u]=True
    return total_sum
sum_max=calc_sum(1)
sum_min=calc_sum(-1)
diff=(sum_max_sum_min+MOD)%MOD
total_paths=n*(n_1)//2
inv_total_paths=pow(total_paths,MOD_2,MOD)
ans=diff*inv_total_paths%MOD
print(ans)
