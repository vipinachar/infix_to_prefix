head = None 

class Node():
    def __init__(self):
        self.data = None
        self.next = None 
        
def push():
    global head
    number = int(input("enter number:"))
    new_node = Node()
    new_node.data = number
    new_node.next = head 
    head = new_node
    
def pop():
    global head
    if head == None:
        print("Underflow")
    else:
        print(f"Popped {head.data}")
        head = head.next 
def peek():
    global head 
    if head == None:
        print("empty")
    else:
        print(head.data)
        
def display():
    global head 
    if head == None:
        print("stack is empty")
    else:
        tmp = head
        while tmp != None:
            print(tmp.data, end=" ")
            tmp=tmp.next 
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
    