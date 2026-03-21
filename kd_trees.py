def dimensionCheck(k):
    if 6 >= k >= 1:
        return k


class Node:
    def _init_(self,point,k,left=None,right=None):
        self.point = point
        self.left = left
        self.right = right
        self.k = dimensionCheck(k)


# Operations: Insert, Delete, Find, Construction?