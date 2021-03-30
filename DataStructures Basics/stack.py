# Basic Python program to dispaly all the operations of the stack

def create_stack():
    stack = []
    return stack

def isEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

def push(stack,ele):
    stack.append(ele)
    print("{0} - element pushed onto the stack".format(ele))


def pop(stack):
    if (isEmpty(stack)):
        print("The stack is underflow")
    else:
        print("Element {0} poped from the stack".format(stack.pop()))

def peek(stack):
    if (isEmpty(stack)):
        print("The stack is underflow")
    else:
        print("The peek element of the stack is : ", stack[len(stack)-1])

def display_stack(stack):
    if (isEmpty(stack)):
        print("The stack is underflow")
    else:
        print("The elements of the stack are : ",stack[::-1])

stack = create_stack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
push(stack,str(40))
push(stack,str(50))
pop(stack)
display_stack(stack)
pop(stack)
display_stack(stack)
pop(stack)
display_stack(stack)
peek(stack)







