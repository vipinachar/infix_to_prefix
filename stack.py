top = -1
n= 5
stack = [None] * n

def push():
    global top, stack , n
    number = int(input("Enter element to push:"))
    if top == n-1:
        print("Overflow")
    else:
        top += 1
        stack[top] = number
        
def pop():
    global top, stack 
    if top == -1:
        print("Underflow")
    else:
        print("popped element is ", stack[top])
        top = top -1 

def peek():
    global stack, top 
    if top == -1:
        print("empty")
    else:
        print(stack[top])

def display():
    global top, stack , n
    if top == -1:
        print("No elements")
    else:
        for i in range(top, -1, -1):
            print(stack[i], end=" ")
        print()
        
def main():
    while True:
        choice = int(input("1) push 2) Pop 3) peek 4) display \n"))
        if choice == 1:
            push()
        elif choice == 2:
            pop()
        elif choice == 3:
            peek()
        elif choice == 4:
            display()
        
    

if __name__ == "__main__":
    main()
    



