# 1570. Dot Product of Two Sparse Vectors

# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx_val = {i: num for i, num in enumerate(nums) if num}   

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, num in self.idx_val.items():
            if vec.idx_val.get(i):
                result += num * vec.idx_val.get(i)
        return result

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)