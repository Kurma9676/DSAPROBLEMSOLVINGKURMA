# stack
# stack is a linear data structure that follows Last In First out
# insertion and deletion can be performed olny at the end of the stack
# the functions associated with stack:
#     empty()
#     size()
#     TOP()
#     peek()
#     push(a)
#     pop()
# implementation:
#     1.list
#     2.collections.deque
#     3.queue.lifoque
# implementation using lists:
#     it is imbuilt datastructure and append is used to insert and pop is used to delete element at end
#     major issue is speed issues
        # program using list
stack=[2,'h']
stack.append(5)
print(stack)
stack.pop()
print(stack)
print(len(stack))#size
# implementation using collections.deque
#     stack can be implemented using deque,it is prefer over the list because it makes fast appends at both ends
#     program
from collections import deque
s=deque()
s.append(1)
s.append(2)
s.append(3)
print(s)
s.pop()
print(s)
s.pop()
print(s)
# implementation using LIFOque modulebut 
# it is same as que but it has some special features
#program
from queue import LifoQueue
st=LifoQueue(maxsize=3)

st.put(1)
st.put(2)
st.put(3)
print(st)
print(st.empty())
print(st.qsize())
print(st.put_nowait(4))
