class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            node = self.table[index]
            while node.next:
                node = node.next
            node.next = Node(key, value)

    def search_and_print_values(self, key):
        index = self.hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                print(node.value)
            node = node.next

# Example usage
hash_table = HashTable(10)
hash_table.insert(1, "Restaurant C")
hash_table.insert(1, "Restaurant B")
hash_table.insert(1, "Restaurant A")

print("Values associated with key 1:")
hash_table.search_and_print_values(1)
