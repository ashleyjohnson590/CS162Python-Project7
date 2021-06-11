#Author: Ashley Johnson
#Date: 5/7/2021
#Description: Program adds and removes a node to the linked list, searches the linked list for a
#value, inserts a node into the linked list at a specific value, reverses the linked list, and returns
#the linked list as a regular python list, and returns the node object that is at tbe _head of
# the linked list.


#please grade the active submission that I submitted on 5/14/2021 and ignore the excercise
#code.
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

    def add(self, val, current=None):
        """recursive version of add function"""

        if self.is_empty():
            self.set_head(Node(val))
            return

        if current is None:
            return self.add(val, self.get_head())

        if current.next is None:
            current.next = Node(val)
            return
        else:
            self.add(val, current.next)

    def remove(self,val, current = None):
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
            return self.remove(val, self.get_head())

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
        self.remove(val, current.next)

    def contains(self, val, previous = None):

        """recursive version of contains function"""

        if self.is_empty():  # If the list is empty
            print("This is an empty list")
            return False

        if previous is None:

            if self.get_head().data == val:
                print("I found it at the head")
                return True
            else:
                return self.contains(val, self.get_head())
        else:
            if previous.data == val:
                print("we found it in previous")
                return True
            else:
                if previous.next == None:
                    print("im at the end of the list")
                    return False
                else:
                    return self.contains(val, previous.next)

    def insert(self,val, pos,index = 0, current=None):
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
                return self.insert(val, pos, 0, self.get_head())
        if current is not None:
            if pos - 1 == index:
                next = current.next
                new_node = Node(val)
                new_node.next = next
                current.next = new_node
                return
            else:
                index += 1
                return self.insert(val, pos, index, current.next)
        else:
            print("we got to the end of list. position is too long")

    def reverse(self, current = None, previous = None):
        """recursive version of reverse function."""
        if self.is_empty():
            return
        if current is None and previous is None:
            return self.reverse(self.get_head())
        if current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
            return self.reverse(current, previous)
        else:
            self.set_head(previous)
            return

    def to_plain_list(self, list = None, current = None):
        """recursive version of to_plain_list function"""
        if self.is_empty():
            return []
        if list is None:
            return self.to_plain_list([],self.get_head())
        if current is not None:
            data = current.data
            list.append(data)
            return self.to_plain_list(list, current.next)
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


def main():
    print("in main")

    ll = LinkedList()
    ll.add(3)
    ll.add(4)
    ll.add(5)
    if ll.contains(99):
        print("list contains 99")
    else:
        print("didn't find it")
    ll.insert(99, 0)
    list = ll.to_plain_list()
    print(list)
    ll.reverse()


if __name__ == "__main__":


    main()