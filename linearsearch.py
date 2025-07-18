# # Linear search (or sequential search) is the simplest search algorithm. It checks each element one by one.

# # Search for the value 4
 

# # 0123456789101112131415161718192021
# # Run the simulation above to see how the Linear Search algorithm works.

# # This algorithm is very simple and easy to understand and implement
# Implement Linear Search in Python
# # In Python, the fastest way check if a value exists in a list is to use the in operator.
mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]

if 4 in mylist:
  print("Found!")
else:
  print("Not found!")
# To implement the Linear Search algorithm we need:

# An array with values to search through.
# A target value to search for.
# A loop that goes through the array from start to end.
# An if-statement that compares the current value with the target value, and returns the current index if the target value is found.
# After the loop, return -1, because at this point we know the target value has not been found.
# Linear Search Time Complexity
# If Linear Search runs and finds the target value as the first array value in an array with 
# n
#  values, only one compare is needed.

# But if Linear Search runs through the whole array of 
# n
#  values, without finding the target value, 
# n
#  compares are needed.

# This means that time complexity for Linear Search is: 
# O(n)
class Linearsearch:
    def __init__(self,target):
        self.target=target
    def linear(self):
        l=[1,2,3,4,5]
        # target=self.target
        for i in range(0,5):
            if l[i]==self.target:
                return i
        return -1
l=Linearsearch(6)
r=l.linear()
if r!=-1:
    print("element found")
else:
    print("element not found")
            
