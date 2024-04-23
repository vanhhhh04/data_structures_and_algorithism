class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertthenewnodebetweentwonode(self, newNode, position):
        currentnode = self.head
        currentposition = 0
        while True :
            if currentposition == position :
                previousnode.next = newNode
                newNode.next = currentnode
                break
            else :
                previousnode = currentnode
                currentnode = currentnode.next
                currentposition += 1


    def deletethenodeinposition(self, position):
        currentnode = self.head
        currentposition = 0
        while True :
            if currentposition == position :
                previousnode.next = nextnode
                break
            else :
                previousnode = currentnode
                currentnode = currentnode.next
                nextnode = currentnode.next
                currentposition += 1


    def deletethelastnode(self):
        if self.head == None :
            print('linked list does not have any elements')
        else :
            lastnode = self.head
            while True :
                if lastnode.next is None :
                    previousnode.next = None
                    break
                else :
                    previousnode = lastnode
                    lastnode = lastnode.next

    

    def insertend(self, newNode):
        if self.head is None :
            self.head = newNode
        else :
            lastnode = self.head
            while True :
                if lastnode.next is None :
                    break
                lastnode = lastnode.next
            lastnode.next = newNode


    # def inserttop(self, newNode):
    #     if self.head is None :
    #         self.head = newNode
    #     else :
    #         newNode.next = self.head
    #         self.head = newNode



    # def deletethenodeinposition(self, position):
    #     currentnode = self.head
    #     current_position = 0
    #     while True :
    #         if current_position == position :
    #             previousnode.next = nextnode
    #             break
    #         else :
    #             previousnode = currentnode
    #             currentnode = currentnode.next
    #             nextnode = currentnode.next
    #             current_position += 1



    def printlist(self):
        if self.head is None :
            print("list is empty")
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data,end=' ')
            currentnode = currentnode.next

l = LinkedList()
node1 = Node('vanh')
node2 = Node('vanh1')
# node3 = Node('vanh2')
# node4 = Node('vanh3')
# node5 = Node('vanh4')
# node6 = Node('vanh5')
l.insertend(node1)
l.insertend(node2)
l.printlist()
print("/n")
# l.insertend(node3)
# l.insertend(node5)
# # l.insertthenewnodebetweentwonode(node6,1)
# l.deletethelastnode()
l.deletethenodeinposition(0)
l.printlist()

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self,data):
#         new_node = Node(data)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None :
#             print(temp.data,end=' ')
#             temp = temp.next

#     def append(self,data):
#         node = Node(data)
#         if self.length == 0 :
#             self.head = node
#             self.tail = node
#         else :
#             self.tail.next = node
#             self.tail = node
#         self.length += 1
#         return True


# head ,
# 4 5 None
# 4


# my_linked_list = LinkedList(4)
# print('head:',my_linked_list.head.data)
# print('Tail:', my_linked_list.tail.data)
# print('Length:', my_linked_list.length)
# my_linked_list.append(5)
# my_linked_list.print_list()