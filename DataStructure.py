class ArrayStack:
    capacity = int
    array = list
    top = int

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def isFull(self):
        return self.top == self.capacity - 1

    def isEmpty(self):
        return self.top == -1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        
    def __str__(self):
        return f"{self.array}"
    
def normalization(target:str):
    target.strip()
    if "," in target:
        target.replace(",", "")
    if "'" in target:
        target.replace("'", "")

    return target

def palindromeExam(target):
    s = ArrayStack(100)
    n = len(target)
    halfway = n//2
    normallizedTarget = normalization(target)

    if n%2 == 0 : return False
    
    for i in range(n):
        if i < halfway:
            s.push(normallizedTarget[i])
        elif i > halfway:
            if s.pop() != normallizedTarget[i] : return False

    return s.isEmpty()
            
# PalindromeExam
# String = " eye "
# print(palindromeExam(normalization(String)))
        
def CheckBracketExam(file):
    
    s = ArrayStack(100)
    target = CBE_ReadFile(file)
    CBE_Normalization(target)

    columnTemp = 0
    charTemp = ""
    available = True

    for row, line in enumerate(target):
        for column, ch in enumerate(line):
            
            if ch == "\"" and available: 
                available = False

            elif ch == "\"" and not available:
                available = True

            if available:

                if ch in "({[" : 
                    s.push(ch)
                    columnTemp = column
                    charTemp = ch

                elif ch in "]})":
                    if s.isEmpty() : 
                        print(f"{row + 1} : {target[row]}\n({row + 1}, {column + 1})에서 {ch}가 먼저 발생함")
                        return 1
                
                    else : 
                        top = s.pop()
                        if (ch == "}" and top != "{") or (ch == ")" and top != "(") or (ch == "]" and top != "["):
                            print(f"{row + 1} : {target[row]}\n({row + 1}, {column + 1})에서 {ch, top}이 일치하지 않음")
                            return 2
            
        if not s.isEmpty():
            print(f"{row + 1} : {target[row]}\n({row + 1}, {columnTemp + 1})에서 열린 {charTemp} 가 닫히지 않음")
            return 3

    return 0
    
def CBE_ReadFile(file) -> list:
    target = str

    with open(file, "r", encoding="utf-8") as f:
        target = list(f.readlines())

    return target

# CBE : CheckBracketExam
def CBE_Normalization(target:list):
    newline = ""
    
    for row, line in enumerate(target):

        for ch in line:
            if ch in "{([])}": newline += ch
            elif ch == "\n" : pass
            elif ch in "\"" : newline += "\"" 
            else : newline += "."

        target[row] = newline
        newline = ""

# CheckBracketExam
# CheckBracketExam("hello.txt")

class CircularQueue:
    capacity = int
    front = int
    rear = int
    array = list

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def isEmpty(self):
        return self.rear == self.front
    
    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = e

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def __str__(self):
        if self.rear >= self.front:
            f"{self.array[self.front + 1:self.rear + 1]}"
        else :
            f"{self.array[self.front + 1:self.capacity] + self.array[0:self.rear + 1]}"

# Queue and recursion
def QueueFib(n):
    q = CircularQueue(10)
    q.enqueue(1)
    for i in range(2, n + 1):    
        q.enqueue(q.dequeue() * i)
    return q.dequeue()

def recursionFib(n):
    if n == 1 : return 1
    else : return recursionFib(n-1) * n

class TNode:
    left = None
    right = None
    data = None

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# Tree and recursion (feat. queue)

def preorder(n):
    print(n.data, end=" ")
    preorder(n.left)
    preorder(n.right)

def inorder(n):
    inorder(n.left)
    print(n.data, end= " ")
    inorder(n.right)

def postorder(n):
    postorder(n.left)
    postorder(n.right)
    print(n.data, end=" ")

def levelorder(n):
    q = CircularQueue(100)
    q.enqueue(n)

    while n is not None:
        n = q.dequeue()
        if q.isEmpty():
            print(q.data, end=" ")
            q.enqueue(n.left)
            q.enqueue(n.right)

def count_node(n):
    if n == None : return 0
    else : count_node(n.left) + count_node(n.right) + 1

def count_leaf(n):
    if n is None : return 0
    elif n.left is None and n.right is None : return 1
    else : count_leaf(n.left) + count_leaf(n.right)

def calc_hight(n):
    if n is None : return 0

    hLeft = calc_hight(n.left)
    hRight = calc_hight(n.right)

    if hLeft > hRight : 
        return hLeft + 1
    else :
        return hRight + 1

def is_complete_binary_tree(root):
    if root is None : return True

    q = CircularQueue(100)
    q.enqueue(root)
    prevEmptyFlag = False
    
    while not q.isEmpty():
        currentTNode = q.dequeue()

        if prevEmptyFlag and (currentTNode.left is not None or currentTNode is not None) : return False
        if currentTNode.left is not None and currentTNode.right is None : return False
        
        if currentTNode.left is not None : q.enqueue(currentTNode.left)
        else : prevEmptyFlag = True
        if currentTNode.right is not None : q.enqueue(currentTNode.right)
        else : prevEmptyFlag = True

    return True

# def is_complete_binary_tree(root):
    
#     if root is None : return True
    
#     q = CircularQueue(100)
#     q.enqueue(root)
#     prevEmptyFlag = False

#     while not q.isEmpty():

#         curruntTNode = q.dequeue()
        
#         if prevEmptyFlag and (curruntTNode.left != None or curruntTNode.right != None): return False
#         if curruntTNode.left == None and curruntTNode.right != None : return False

#         if curruntTNode.left is not None : q.enqueue(curruntTNode.left)
#         else : prevEmptyFlag = True
#         if curruntTNode.right is not None : q.enqueue(curruntTNode.right)
#         else : prevEmptyFlag = True
    
#     return True
    
# G = TNode("G", None, None)
# F = TNode("F", G, None)
# E = TNode("E", None, None)
# D = TNode("D", None, None)
# C = TNode("C", F, None)
# B = TNode("B", D, E)
# A_root = TNode("A", B, C)

# print(is_complete_binary_tree(A_root))

class Node:
    data = None
    nextNode = None

    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

class LinkedList:
    head = None

    def __init__(self):
        self.head = None

    def getNode(self, pos):
        if pos < 0 : return None

        current = self.head      

        while pos > 0 and current != None:
            current = current.nextNode
            pos -= 1
        
        return current

    def isFull(self):
        return False

    def isEmpty(self):
        return self.head == None

    def insert(self, e, pos):
        if pos < 0 : return -1

        before = self.getNode(pos - 1)
            
        if before == None : 
            self.head = Node(e, self.head)
        else : 
            before.nextNode = Node(e, before.nextNode)

    def delete(self, pos):
        if pos < 0 : return -1

        before = self.getNode(pos - 1)

        if before is None : 
            if self.head != None : 
                self.head = self.head.nextNode

            elif before.nextNode != None:
                before.nextNode = before.nextNode.nextNode

    def reverse(self):
        prevNode = None
        curruntNode = None
        nextNode = self.head
        
        while nextNode != None:
            prevNode = curruntNode
            curruntNode = nextNode
            nextNode = nextNode.nextNode

            curruntNode.nextNode = prevNode

        self.head = curruntNode

    def __str__(self):
        current = self.head
        output = []
        
        while current != None:
            output.append(current.data)
            current = current.nextNode
        
        return f"{output}"

def insertionSort_for(a):
    n = len(a)
    
    for key in range(1, n):
        for recode in range(key):
            if a[recode] > a[key] :
                a[recode], a[key] = a[key], a[recode]
        

def insertionSort_while(array):
    n = len(array)

    for i in range(1, n):
        insertion = array[i]
        j = i - 1

        while j >= 0 and insertion < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = insertion

def bubbleSort_array(array):
    n = len(array)

    for i in range(n-1, 0, -1):
        beChanged = False
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] 

def bubbleSort_linked(lls):
    beChanged = True

    while beChanged:
        current = lls.head
        beChanged = False
        while current.nextNode != None:
            if current.data > current.nextNode.data:
                current.data, current.nextNode.data = current.nextNode.data, current.data
                beChanged = True
            current = current.nextNode            

def selectionSort(array):
    n = len(array)
    index = 0
    for i in range(0, n-1):
        index = i
        for j in range(i+1, n):
            if array[index] > array[j]:
                index = j

        array[index], array[i] = array[i], array[index]

# l = LinkedList()
# l.insert(10, 0)
# l.insert(20, 0)
# l.insert(30, 0)
# l.insert(40, 0)
# print(l)
# bubbleSort_linked(l)
# print(l)
# l.reverse()
# print(l)

