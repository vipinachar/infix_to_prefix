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
    prefix = ''
    exp = exp[::-1]
    for i in exp:
        if i == ' ':
            pass
        elif i.isalpha() or i.isdigit():
            prefix += i 
        else:
            if top == None or i==')':
                push(i)
            elif i=='(':
                while top.data!=')':
                    val = pop()
                    prefix+=val
                pop()
            else:
                while True:
                    if top == None:
                        push(i)
                        break
                    elif top.data == '^' and i == '^':
                        prefix+=pop()
                        break
                    elif top.data==')':
                        push(i)
                        break 
                    elif prece[i]>prece[top.data]:
                        push(i)
                        break
                    elif prece[i] == prece[top.data]:
                        push(i)
                        break 
                    else:
                        val = pop()
                        prefix+=val
        
    while top!=None:
        prefix+=pop()
    print(prefix)

    ##Evaluates Post Fix 

    for i in prefix:
        if i.isalpha():
            print('Can only include numbers')
            return 
        elif i.isdigit():
            push(i)
        else:
            a = int(pop())
            b = int(pop())
            val=0
            if i=='+':
                val=a+b
            elif i=='-':
                val=a-b
            elif i=='*':
                val=a*b
            elif i=='/':
                val=a/b
            elif i=="^":
                val=a**b 
            push(val)
    
    disp()

if __name__ == '__main__':
    top = None 
    print('Infix to Postfix: ')
    exp = input("Enter the Infix expression: ")
    infix(exp)
    # k+l-m*n+(o^p)*w/u/v*t+q