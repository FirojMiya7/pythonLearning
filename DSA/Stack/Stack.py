# Program for Stack


stack = [0] * 5  # Fixed-size stack
maxSize = 5
top = -1

def push(data):
    global top
    if top >= maxSize-1:
        print("Stack Overflow\n")
    else:
        top += 1
        stack[top] = data
        print("Inserted Element Successfully.", data)

def pop():
    global top
    if top == -1:
        print("Stack Underflow.\n")
    else:
        top -= 1
        print("Deleted Element Successfully.", stack[top])

def show():
    if top == -1:
        print("Stack is empty.\n")
    else:
        for i in range(top, -1, -1):            # in range(start , stop, step) --> start include and stop ko last exclude hunxa and step tw steps naii bhaii halyo
            print(stack[i])


while True:
    ch = int(input("\n1.Push\t2.Pop\t3.Show\t4.Exit\t: "))

    if ch == 1:
        data = int(input("Enter data to insert: "))
        push(data)
    elif ch == 2:
        pop()
    elif ch ==3:
        show()
    elif ch == 4:
        print("Thanks for using stack program.\n")
        break
    else:
        print("Error! Invalid Choice.")
        