from collections import deque

stack = [1,2,3,4,5,6]
print(stack.pop()) #reutnrs 6

queue = deque([1,2,3,4])
print(queue)

queue.append(5)
queue.append(6)
queue.append(7)
print(queue)

print(queue.popleft()) #reverse a usual pop
