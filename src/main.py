from node import Node
from tree import Tree

def manualCreationTest():
    #         45
    #    33        77
    # 22         65   88
    n88 = Node(88)

    n65 = Node(65)

    n77 = Node(77)
    n77.childRight = n88
    n88.parent = n77
    n77.childLeft = n65
    n65.parent = n77

    n22 = Node(22)

    n33 = Node(33)
    n33.childLeft = n22
    n22.parent = n33

    n45 = Node(45)
    n45.childLeft = n33
    n33.parent = n45
    n45.childRight = n77
    n77.parent = n45

    t = Tree()
    t.root = n45
    return t

def bstInsertionTest():
    #         45
    #    33        77
    # 22         65   88
    t = Tree()
    t.insert(45)
    t.insert(33)
    t.insert(77)
    t.insert(22)
    t.insert(65)
    t.insert(88)
    return t


myTree = manualCreationTest()
print(myTree)
find = myTree.bfs(88)
print(find)

myTree2 = bstInsertionTest()
print(myTree2)
find2 = myTree2.bfs(88)
print(find2)

myTree2.findAndDeleteByMerging(88)
print(myTree2)