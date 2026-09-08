from collections import deque
queue = deque(['nahid', 'sanji', 'shifa', 'rashida'])
queue.append('shozan')
queue.append('jarif')
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)