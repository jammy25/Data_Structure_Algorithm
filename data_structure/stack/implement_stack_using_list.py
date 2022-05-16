stack = []
def push():
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("Stack is empty.")
    else:
        e = stack.pop()
        print("removed element: ", e)

while True:
    print("Select the operation 1. Push 2. Pop 3. Quit")
    choice  = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation!")