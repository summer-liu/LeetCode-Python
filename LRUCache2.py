class Node:　　　　　　　　　　　　　　　　　　　　　　　　　　#双向链表中节点的定义
    def __init__(self,k,x):
        self.key=k
        self.val=x
        self.prev=None
        self.next=None

class DoubleLinkedList:　　　　　　　　　　　　　　　　　　　#双向链表是一个表头，head指向第一个节点，tail指向最后一个节点
    def __init__(self):
        self.tail=None
        self.head=None
        
    def isEmpty():　　　　　　　　　　　　　　　　　　　　　　#如果self.tail==None，那么说明双向链表为空
        return not self.tail
    def removeLast(self):　　　　　　　　　　　　　　　　　　#删除tail指向的节点
        self.remove(self.tail)
        
    def remove(self,node):　　　　　　　　　　　　　　　　　 #具体双向链表节点删除操作的实现
        if self.head==self.tail:
            self.head,self.tail=None,None
            return
        if node == self.head:
            node.next.prev=None
            self.head=node.next
            return
        if node ==self.tail:
            node.prev.next=None
            self.tail=node.prev
            return
        node.prev.next=node.next
        node.next.prev=node.prev
        
    def addFirst(self,node):　　　　　　　　　　　　　　　　  #在双向链表的第一个节点前面再插入一个节点　　
        if not self.head:
            self.head=self.tail=node
            node.prev=node.next=None
            return
        node.next=self.head
        self.head.prev=node
        self.head=node
        node.prev=None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):　　　　　　　　　　　　　　#初始化LRU Cache
        self.capacity=capacity　　　　　　　　　　　　　　　 #LRU Cache的容量大小　　　　　　　　　　　　　
        self.size=0　　　　　　　　　　　　　　　　　　　　　　#LRU Cache目前占用的容量
        self.P=dict()　　　　　　　　　　　　　　　　　　　　　#dict为文章中提到的hashmap，加快搜索速度，{key：对应节点的地址}
        self.cache=DoubleLinkedList()
    # @return an integer
    def get(self, key):　　　　　　　　　　　　　　　　　　　　#查询操作
        if (key in self.P) and self.P[key]:　　　　　　　　#如果key在字典中
            self.cache.remove(self.P[key])　　　　　　　　　#将key对应的指针指向的节点删除
            self.cache.addFirst(self.P[key])　　　　　　　　#然后将这个节点添加到双向链表头部
            return self.P[key].val　　　　　　　　　　　　　　#并返回节点的value
        else: return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):　　　　　　　　　　　　　　　　#设置key对应的节点的值为给定的value值
        if key in self.P:　　　　　　　　　　　　　　　　　　　#如果key在字典中
            self.cache.remove(self.P[key])　　　　　　　　  #先删掉key对应的节点
            self.cache.addFirst(self.P[key])　　　　　　　　#然后将这个节点插入到表的头部
            self.P[key].val=value　　　　　　　　　　　　　　 #将这个节点的值val改写为value
        else:　　　　　　　　　　　　　　　　　　　　　　　　　　#如果key不在字典中
            node=Node(key,value)　　　　　　　　　　　　　　　#新建一个Node节点，val值为value
            self.P[key]=node　　　　　　　　　　　　　　　　　 #将key和node的对应关系添加到字典中
            self.cache.addFirst(node)　　　　　　　　　　　　#将这个节点添加到链表表头
            self.size +=1　　　　　　　　　　　　　　　　　　　#容量加1
            if self.size > self.capacity:　　　　　　　　   #如果链表的大小超过了缓存的大小，删掉最末尾的节点，
                self.size -=1　　　　　　　　　　　　　　　　 #并同时删除最末尾节点key值和末节点在字典中的对应关系
                del self.P[self.cache.tail.key]
                self.cache.removeLast()