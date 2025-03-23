class Solution:
    def helper(self, node, visited):
        if node is None: 
            return None
        newNode = Node(node.val) 
        visited[node.val] = newNode
        for adjNode in node.neighbors:
            if adjNode.val not in visited:
                newNode.neighbors.append(self.helper(adjNode, visited)) 
            else:
                newNode.neighbors.append(visited[adjNode.val]) 
        return newNode

    def cloneGraph(self, node: 'Node') -> 'Node': 
        if not node:
          return None
        return self.helper(node, {})
