#Author: Ashley Johnson
#Date: 5/7/2021
#Description: Program adds and removes a node to the linked list, searches the linked list for a
#value, inserts a node into the linked list at a specific value, reverses the linked list, and returns
#the linked list as a regular python list, and returns the node object that is at tbe _head of
# the linked list.

class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def set_data(self):
        data = self.data
        return data
    def get_next(self):
        return self.next
    def set_next(self):
        self.next = None
class LinkedList:
    """
    A linked list implementation of the List ADT
    """
    def __init__(self):
        """initializes head of linked list."""
        self._head = None

    def add(self, val):
        """
        Adds a node containing val to the linked list
        """
        if self.is_empty():  # If the list is empty
            self.set_head(Node(val))
        else:
            current = self.get_head()
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def rec_add(self, val, current=None):
        """recursive version of add function"""

        if self.is_empty():
            self.set_head(Node(val))
            return

        if current is None:
            return self.rec_add(val, self.get_head())

        if current.next is None:
            current.next = Node(val)
            return
        else:
            self.rec_add(val, current.next)

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self.is_empty():  # If the list is empty
            return

        head = self.get_head()
        head_data = head.get_data()
        if head_data == val:  # If the node to remove is the head
            self.set_head(head.next)
        else:
            current = head
            while current is not None and current.data != val:
                previous = current
                current = current.next
            if current is not None:  # If we found the value in the list
                previous.next = current.next

    def rec_remove(self,val, current = None):
        """recursive version of remove function"""

        if self.is_empty():  # If the list is empty
            print("This is an empty list")
            return

        if current is None:
            head = self.get_head()
            head_data = head.get_data
            if head_data == val:
                print("Special case number is at the ead")
                self.set_head(head.next)
            return self.rec_remove(val, self.get_head())

        elif current.next is None:
            print("We are at the end of the list")
            return

        print("val = {}".format(val))
        print("current.data = {}".format(current.data))

        if current.next.data != val:
            print("Nope it doesn't matcvh")
        else:
            print("Yes it matches")
            print("My data = {}".format(current.data))
            next_node = current.next
            print("My neighbors data {}".format(next_node.data))
            next_next_node = next_node.next
            print("My next_next neight {}".format(next_next_node.data))
            current.next = next_next_node
        self.rec_remove(val, current.next)


    def contains(self, key):
        """
        Returns True if the list contains a Node with the value key,
        otherwise returns False
        """
        if self.is_empty():  # If the list is empty
            return False

        current = self.get_head()
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def rec_contains(self, val, previous = None):

        """recursive version of contains function"""

        if self.is_empty():  # If the list is empty
            print("This is an empty list")
            return False

        if previous is None:

            if self.get_head().data == val:
                print("I found it at the head")
                return True
            else:
                return self.rec_contains(val, self.get_head())
        else:
            if previous.data == val:
                print("we found it in previous")
                return True
            else:
                if previous.next == None:
                    print("im at the end of the list")
                    return False
                else:
                    return self.rec_contains(val, previous.next)

    def insert(self, val, pos):
        """
        Inserts a node containing val into the linked list at position pos
        """
        if self.is_empty():  # If the list is empty
            self.add(val)
            return

        if pos == 0:
            temp = self.get_head()
            self.set_head(Node(val))
            self.get_head().next = temp
        else:
            current = self.get_head()
            counter = 0
            for _ in range(pos - 1):
                if current.next is None:
                    current.next = Node(val)
                    return
                current = current.next
            temp = current.next
            current.next = Node(val)
            current.next.next = temp

    def rec_insert(self,val, pos,index = 0, current=None):
        """recursive version of insert function"""
        if self.is_empty():  # If the list is empty
            print("list is empty")
            return
        if pos == 0:
            temp = self.get_head()
            self.set_head(Node(val))
            self.get_head().next = temp
            return
        elif index == 0:
            if current is None:
                return self.rec_insert(val, pos, 0, self.get_head())
        if current is not None:
            if pos - 1 == index:
                next = current.next
                new_node = Node(val)
                new_node.next = next
                current.next = new_node
                return
            else:
                index += 1
                return self.rec_insert(val, pos, index, current.next)
        else:
            print("we got to the end of list. position is too long")

    def reverse(self):
        """"
        Reverses the linked list
        """
        previous = None
        current = self.get_head()

        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
        self.set_head(previous)

    def rec_reverse(self, current = None, previous = None):
        """recursive version of reverse function."""
        if self.is_empty():
            return
        if current is None and previous is None:
            return self.rec_reverse(self.get_head())
        if current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
            return self.rec_reverse(current, previous)
        else:
            self.set_head(previous)
            return

    def to_plain_list(self):
        """
               Returns a regular Python list containing the same values,
               in the same order, as the linked list
               """
        result = []
        current = self._head
        while current is not None:
            result += [current.data]
            current = current.next
        return result

    def rec_to_plain_list(self, list = None, current = None):
        """recursive version of to_plain_list function"""
        if self.is_empty():
            return []
        if list is None:
            return self.rec_to_plain_list([],self.get_head())
        if current is not None:
            data = current.data
            list.append(data)
            return self.rec_to_plain_list(list, current.next)
        else:
            return list
##
    def get_head(self):
        """function returns the node object that is at the _head of the linked list"""
        head = self._head
        return head

    def set_head(self, new_head):
        """function sets head"""
        self._head = new_head

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    #def rec_display(self, a_node):
        """recursive display method"""
       # if a_node is None:
       #     return
       # print(a_node.get_data(), end=" ")
       # self.rec_display(a_node.get_next())

    #def display(self):
        """recursive display helper method"""
        #self.rec_display(self.get_head())

def main():
    print("in main")

    ll = LinkedList()
    ll.rec_add(3)
    ll.rec_add(4)
    ll.rec_add(5)
    ll.display()
    ll.reverse()
    ll.display()
    if ll.rec_contains(99):
        print("list contains 99")
    else:
        print("didn't find it")
    ll.rec_insert(99, 0)
    ll.display()
    list = ll.rec_to_plain_list()
    print(list)
    ll.rec_reverse()
    ll.display()

if __name__ == "__main__":


    main()