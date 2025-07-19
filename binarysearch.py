# # Binary Search (Recursive and Iterative) - Python
# # Last Updated : 21 Feb, 2025
# # Binary Search Algorithm is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 

# # Below is the step-by-step algorithm for Binary Search:

# # Divide the search space into two halves by finding the middle index “mid”. 
# # Compare the middle element of the search space with the key. 
# # If the key is found at middle element, the process is terminated.
# # If the key is not found at middle element, choose which half will be used as the next search space.
# # If the key is smaller than the middle element, then the left side is used for next search.
# # If the key is larger than the middle element, then the right side is used for next search.
# # This process is continued until the key is found or the total search space is exhausted.
# # How does Binary Search Algorithm work?
# # To understand the working of binary search, consider the following illustration:

# # Consider an array arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91}, and the target = 23.

# # Binary-Search-2.webpBinary-Search-2.webp
# # Code Implementation
# # 1. Python Program for Binary Search Using Recursive
# # Create a recursive function and compare the mid of the search space with the key.
# And based on the result either return the index where the key is found or call the recursive function for the next search space.
def binary_search(arr,target,low,high):
    # low=0
    # high=len(arr)
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,target,low,mid-1)
    else:
        return binary_search(arr,target,mid+1,high)
arr=[1,2,3,4,5]
target=6
n=binary_search(arr,target,0,len(arr)-1)
if n!=-1:
    print("element found at",n,"position")
else:
    print("element not found")
