from collections import deque

stack = deque()
stack.append(2)
stack.append(10)    # push
print(stack[-1])    # peep
print(stack.pop())  # pop