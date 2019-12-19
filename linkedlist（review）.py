#首先定义节点类
class Node :
    def __init__(self,value): #定义一个新节点时要传入这个节点保存的值value
        self.value = value
        self.next = None

    def getData(self) : #得到节点的值
        return self.value

    def setData(self,value) : #设置节点的值value
        self.value = value

    def setNext(self,node) : #设置该节点连接的下一个节点
        self.next = node
    
    def getNext(self) : #得到该节点连接的节点
        return self.next


class linkedlist :
    def __init__(self) : #定义一个链表，设置该链表的头部和尾部
        self.head = None
        self.tail = None

    def getLength (self) : #
        current = self.head
        count = 0
        while current is not None :
            current = current.getNext()
            count += 1
        return count

    def show(self) :
        temp = self.head
        while temp is not None :
            print(temp.getData())
            temp = temp.getNext()

    def append(self,value): #向链表的尾部添加节点
        node = Node(value)
        if self.head == None : #判断该链表是否为空链表，如果是那头尾都指向该链表
            self.head = node
            self.tail = node
        else : #不是的话，尾部指向刚添加的元素，新的尾部就是刚添加的元素。
            self.tail.setNext(node) #这里的尾部不能简单的理解为self.tail == none，因为这是在链表有元素的情况下设定的。
            self.tail = node
            

    def insert(self,i,value) :
        """
        要往链表的第i个位置添加一个节点，其内容是x
        i从0开始
        如果插入的位置大于当前的长度的话，默认是往最后的位置添加一个数
        """
        if i >= self.getLength() or self.head == None :
            self.append(value)
        else :
            node = Node(value)
            if i == 0 :
                node.setNext(self.head)
                self.head = n 
            else :
                temp = self.head
                for index in range(i-1) :
                    temp = temp.getNext()
                node.setNext(temp.getNext())
                temp.setNext(node)
    

li = linkedlist()
li.append(19)
li.append(20)
li.append(30)
li.insert(1,22)
li.show()
li.deleteNode