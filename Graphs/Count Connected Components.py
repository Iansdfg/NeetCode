from collections import deque 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1 
        if edges == []:
            return n
        visited = [0 for i in range(n)]
        if not edges:
            return 0
        head_tails = dict()
        for head, tail in edges:
            if head in head_tails:
                head_tails[head].append(tail)
            else:
                head_tails[head] = [tail]

            if tail in head_tails:
                head_tails[tail].append(head)
            else:
                head_tails[tail] = [head]

        components = 0
        while 0 in visited:
            for i in range(len(visited)):
                if visited[i] == 0:
                    print('next node ', i)
                    queue = deque([i])
                    visited[i] = 1 
                    components += 1 
                    break

            while queue: 
                curr = queue.popleft()
                print(curr)
                if curr not in head_tails:
                    continue
                for next_node in head_tails[curr]:
                    if visited[next_node] == 1:
                        continue
                    visited[next_node] = 1 
                    queue.append(next_node)
        return components

########################################################################################################
##################################################  union find  ########################################
########################################################################################################
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root_of_i = [i for i in range(n)]

        for edge in edges:
            sm_node = min(edge)
            lg_node = max(edge)
            
            root_sm_node = root_of_i[sm_node]
            if root_of_i[lg_node] == root_sm_node:
                continue
            root_of_i[lg_node] = root_sm_node
            n -= 1
        return n
     

