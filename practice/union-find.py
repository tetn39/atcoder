class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

    def find_root(self, x):
        while self.root[x] >= 0:
            x = self.root[x]
        return x

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def size(self, x):
        return -self.root[self.find_root(x)]
    

def main():
    n, q = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(q):
        p, a, b = map(int, input().split())
        if p == 0:
            uf.unite(a, b)
        else:
            if uf.isSameGroup(a, b):
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    main()