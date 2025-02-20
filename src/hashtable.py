# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'LP({self.key}, {self.value}, {self.next})'

    def __repr__(self):
        return f'LP({self.key}, {self.value}, {self.next})'


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        key_value = LinkedPair(key, value)
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            key_value.next = self.storage[index]
            self.storage[index] = key_value
        else:
            self.storage[index] = key_value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            current = self.storage[index]
            while current is not None:
                if current.key == key:
                    self.storage[index] = current.next
                current = current.next
            print('Key not found.')
        else:
            print("Key not found.")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            current = self.storage[index]
            while current is not None:
                if current.key == key:
                    return current.value
                current = current.next
            return None
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        old_storage = self.storage
        self.storage = new_storage

        for item in old_storage:
            if item is not None:
                # index = self._hash_mod(item.key)
                current = item
                while current is not None:
                    self.insert(current.key, current.value)
                    current = current.next


if __name__ == "__main__":
    ht1 = HashTable(3)
    ht1.insert('key1', 'value1')
    ht1.insert('key2', 'value2')
    ht1.insert('key3', 'value3')
    ht1.insert('key4', 'value4')
    print(ht1.retrieve('key1'))
    print(ht1.retrieve('key2'))
    print(ht1.retrieve('key3'))
    print(ht1.retrieve('key4'))
    print(ht1.storage)
    ht1.resize()
    print(ht1.storage)
    print('after resize')
    print(ht1.retrieve('key1'))
    print(ht1.retrieve('key2'))
    print(ht1.retrieve('key3'))
    print(ht1.retrieve('key4'))
    # ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
