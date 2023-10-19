def create_stack():
    stack = list()
    return stack

def Isempty(stack):
    return len(stack) == 0

def push(stack,n):
    stack.append(n)
    print("push item:" + n)

def pop(stack):
    if(Isempty(stack)):
        return "stack is empty"
    else:
        return stack.pop()

def Display(stack):
    print("The stack elements are:")
    for i in stack:
        print(i)

def size(stack):
        return stack.top + 1

def isFull(stack):
        return stack.size() == stack
        
stack = create_stack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print("poped item:" + pop(stack))
Display(stack)

