from collections import deque
class Tree:

    def __init__(self):
        self.root = None
    #}__init__

    def dfs(self, valor): #Busca em Profundidade
        pass
    #}dfs

    def bfs(self, valor): #Busca em Largura
        fila = deque()
        if self.root is not None:
            fila.append(self.root)
        
        while len(fila) > 0:
            node_atual = fila.popleft()
            if node_atual.value == valor:
                return node_atual
            else:
                if node_atual.childLeft is not None:
                    fila.append(node_atual.childLeft)
                if node_atual.childRight is not None:
                    fila.append(node_atual.childRight)
        return None
    #}bfs

    def __str__(self):
        return f"{self.root}"
    #}__str__

    def __repr__(self):
        return f"{self}"
    #}__repr__
    
#}class Tree