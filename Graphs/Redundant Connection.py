class Solution:
    PARENT = []
    RANK = []
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.PARENT = [i for i in range(len(edges) + 1)]
        self.RANK = [1 for i in range(len(edges) + 1)]

        for sm_node, lg_node in edges:
            if self.union(sm_node, lg_node) == False:
                return[sm_node, lg_node]

    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)

        if p1 == p2:
            return False 

        if self.RANK[p1] >= self.RANK[p2]:
            self.PARENT[p2] = p1
            self.RANK[p1] += 1 
        else:
            self.PARENT[p1] = p2
            self.RANK[p2] += 1 

        return True 

    def find(self, node):
        par = self.PARENT[node]
        while par != self.PARENT[par]:
            par = self.PARENT[par]
        return par 

        
