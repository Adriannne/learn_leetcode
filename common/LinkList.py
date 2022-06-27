
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        # if self._head : return False
        # else: return True
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next

    def add(self, item):
        # add in head
        # if self._head is not None:
        #     head = self._head
        #     self._head.item = item
        #     self._head.next = head
        # else:
        #     self._head = Node(item)
        node = Node(item)
        node.next = self._head.next
        self._head = node

    def append(self, item):
        # add in tail
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node


    def insert(self, pos, item):
        # add in pos
        # node = Node(item)
        # if self.is_empty():
        #     self._head = node
        # else:
        #     cur = self._head
        #     while cur.next != pos and cur.next is not None:
        #         cur = cur.next
        #     if cur.next == pos:
        #         old_node = cur.next
        #         cur.next = node
        #         cur.next.next = old_node
        #     else:
        #         cur.next = node
        if pos <= 0:
            self.add(item)
        elif pos < self.length() - 1:
            node = Node(item)
            cur = self._head
            while cur != pos:
                cur = cur.next
            node.next = cur.next
            cur.next = node
        else:
            self.append(item)


    # def remove(self, item):
    #     if self.is_empty():
    #





if __name__ == '__main__':
    single_link_list = SingleLinkList()
    node1 = Node(1)
    node2 = Node(2)
    single_link_list._head = node1
    node1.next = node2