from node import Node
from collections import deque
class Tree:

    def __init__(self):
        self.root = None
    #}__init__

    def insert(self, value):
        position = self.root
        previous = None
        while position != None:
            previous = position
            if value < position.value:
                position = position.childLeft
            else:
                position = position.childRight
        if self.root == None:
            self.root = Node(value)
        elif value < previous.value:
            previous.childLeft = Node(value)
        else:
            previous.childRight = Node(value)

        
    def _deleteByMerging(self, node:Node):
        tmp = node
        if node != None:
            if node.childRight == None:
                node = node.childLeft
            elif node.childLeft == None:
                node = node.childRight
            else:
                tmp = node.childLeft
                while tmp.childRight != None:
                    tmp = tmp.childRight
                tmp.childRight = node.childRight
                node.value = node.childLeft.value
                node.childRight = node.childLeft.childRight
                node.childLeft = node.childLeft.childLeft


    def findAndDeleteByMerging(self, value):
        position = self.root
        previous = None
        while position != None:
            if position.value == value:
                break
            previous = position
            if value < position.value:
                position = position.childLeft
            else:
                position = position.childRight  
        if position != None and position.value == value:
            if position.childLeft == None and position.childRight == None:
                if position == self.root:
                    self.root = None
                elif position == previous.childLeft:
                    previous.childLeft = None
                else:
                    previous.childRight =None
            else:    
                self._deleteByMerging(position)
        elif self.root != None:
            print(f"Elemento {value} não está na árvore")
        else:
            print("Árvore está vazia")
            
    

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