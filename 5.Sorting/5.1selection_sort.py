# Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.


class Solution: 
    # Function to find the minimum element in the unsorted array
    def select(self, arr, i):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        return min_index
    
    # Function to perform selection sort
    def selectionSort(self, arr, n):
        for i in range(n):
            # Find the minimum element in the unsorted part of the array
            min_index = self.select(arr, i)
            # Swap the found minimum element with the element at position i
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
n = len(arr)
solution = Solution()
solution.selectionSort(arr, n)
print("Sorted array:", arr)
