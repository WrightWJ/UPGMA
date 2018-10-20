class Node:
    # This was given to me in Bioinformatics by Louis Oliphant
    # Used by WrightWJ
    "A class representing a node in a phylogenetic tree"

    def __init__(self, name="", dist=0, left=None, right=None, height=0):
        self.name = name
        self.left = left
        self.right = right
        self.dist = dist
        self.height = height

    def setName(self, newName):
        self.name = newName

    def setDistance(self, newDist):
        self.dist = newDist

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def getName(self):
        return self.name

    def getDistance(self):
        return self.dist

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right
    def getHeight(self):
        return self.height

    def printNode(self):
        # base case
        if self.left == None and self.right == None:
            out = self.name + ":" + str(self.dist)
            return out
        out = "(" + self.left.printNode() + "," + self.right.printNode() + ")" + \
              self.name + ("" if self.dist == 0 else ":" + str(self.dist))
        return out
