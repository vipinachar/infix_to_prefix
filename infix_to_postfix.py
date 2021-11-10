class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def push(val):
    global top 
    n = Node(val)
    if top == None:
        top = n 
    else:
        n.next = top 
        top = n 
    
def pop():
    global top 
    if top==None:
        print('empty')
    else:
        tmp = top 
        value = tmp.data
        top = top.next 
        del tmp
        return value

def disp():
    global top 
    if top == None:
        print('empty')
    else:
        tmp = top 
        while tmp!=None:
            print(tmp.data,end=' ')
            tmp=tmp.next 
        print()

prece = {'^':3,'/':2,'*':2,'+':1,'-':1}
def infix(exp):
    global top 
    postfix = ''
    for i in exp:
        print(i)
        if i.isalpha() or i.isdigit():
            postfix += i 
        else:
            if top == None or i=='(':
                push(i)
            elif i==')':
                while top.data!='(':
                    val = pop()
                    postfix+=val
                pop()
            else:
                while True:
                    if top == None:
                        push(i)
                        break
                    elif top.data == '^' and i == '^':
                        push(i)
                        break
                    elif top.data=='(':
                        push(i)
                        break 
                    elif prece[i]>prece[top.data]:
                        push(i)
                        break
                    else:
                        val = pop()
                        postfix+=val
        print('###########',postfix,'#################')
        
    while top!=None:
        postfix+=pop()
    print(postfix)

if __name__ == '__main__':
    top = None 
    print('Infix to Postfix: ')
    exp = input("Enter the Infix expression: ")
    infix(exp)
    # k+l-m*n+(o^p)*w/u/v*t+q