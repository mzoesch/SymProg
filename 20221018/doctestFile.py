from stack import Stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
print(stack.is_empty())
print(stack.size())

stack.pop()
stack.pop()
stack.pop()
print(stack.is_empty())
