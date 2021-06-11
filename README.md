# CS162Python-Project7
Write a LinkedList class that has **recursive** implementations of the `add` and `remove` methods described in the Exploration.  It should also have **recursive** implementations of the `contains`, `insert`, and `reverse` methods described in the exercises.  The reverse method should **not** change the _data_ value each node holds - it must rearrange the order of the nodes in the linked list (by changing the _next_ value each node holds).

It should have a **recursive** method named `to_plain_list` that takes no parameters and returns a regular Python list that has the same values (from the `data` attribute of the Node objects), in the same order, as the current state of the linked list.

It should have a method named `get_head` that takes no parameters and returns the Node object (_not_ the value inside it) that is at the `_head` of the linked list.

The `head` data member of the LinkedList class, as well as the `data` and `next` members for the Node class must be private and have getters and setters defined.

All the methods should have the arguments in the same order as you saw in the Lesson. You may use default arguments and/or helper functions. 

Your recursive functions must **not**:
* use any loops
* use any variables declared outside of the function
* use any mutable default arguments

Here's an example of how a recursive version of the display() method from the lesson could be written:
```
    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.get_data(), end=" ")
        self.rec_display(a_node.get_next())

    def display(self):
        """recursive display helper method"""
        self.rec_display(self.get_head())
```

All your classes must be in a single file named: **LinkedList.py**

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
