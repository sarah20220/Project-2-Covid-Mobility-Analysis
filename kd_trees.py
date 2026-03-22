import numpy as np
import sys



class KDNode:
    def __init__(self,point,k,left=None,right=None):
        self.point = point
        self.left = left
        self.right = right
        self.k = k


class KDTree:
    def __init__(self, dataPoints=None):
        self.root = None
        if dataPoints:
            self.root = self.buildTree(dataPoints,0)

    @staticmethod
    def getDistance(target,point):
        result = 0
        for i in range(len(target)):
            result += (target[i] - point[i])**2
        return np.sqrt(result)
    
# Operations: Insert, InsertMany, Delete, FindNearestK, FindNode, Construction?

    def buildTree(dataPoints, depth):
        if not dataPoints:
            return None
        
        k = len(dataPoints[0])
        axis = depth % k
        sortedData = sorted(dataPoints, key=lambda p: p[axis])
        #print(sortedData)
        medianIndex = len(sortedData) // 2
        medianData = sortedData[medianIndex]
        #print("Dimension:",axis,medianData)

        node = KDTree(medianData, axis)
        node.left = KDTree.buildTree(sortedData[:medianIndex], depth + 1)
        node.right = KDTree.buildTree(sortedData[medianIndex + 1:], depth + 1)

        return node

    def kNearestNeighbors(target,dataPoints,k):
        distances = []

        for point in dataPoints:
            distances.append((getDistance(target,point),point))
        sortedDistances = sorted(distances)

        if target in dataPoints:
            return sortedDistances[:k]
        
        return sortedDistances[1:k+1]


def main():
    data = ([1,2,3,4,5,6],[2,3,4,5,6,7],[-1,-2,-3,-4,-5,-6],[-2,-3,-4,-5,-6,-7],[3,4,5,6,7,8])
    myKDTree = KDTree.buildTree(data,1)

    return 0

if __name__ == "__main__":
    sys.exit(main())