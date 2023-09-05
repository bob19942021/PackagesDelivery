# Class to make a hashMap and insert, delete or lookup info in that hashMap
# over all class Space and Time-complexity are O(n)


class HashMap:

    # Time and Space-complexity are O(1)
    def __init__(self, size=30):
        self.table = []
        for i in range(size):
            self.table.append([])

        # method to add new items into the existing Hash Tabel and update the table afterwards
        # Time-complexity and Space-complexity are O(n)
    def insert(self, key, item):
        pool = hash(key) % len(self.table)
        pool_list = self.table[pool]

        for value in pool_list:
            if value[0] == key:
                value[1] = item
                return True

        key_value = [key, item]
        pool_list.append(key_value)
        return True

# method to look-up an item from the HashTable
    # Time-complexity and Space-complexity are O(n)
    def lookup(self, key):
        pool = hash(key) % len(self.table)
        pool_list = self.table[pool]
        for pair in pool_list:
            if key == pair[0]:
                return pair[1]
        return None

# method to remove an item from the hashTable
    # Time-complexity: O(n)
    # Space-complexity: O(1)
    def hash_remove(self, key):
        place = hash(key) % len(self.table)
        location = self.table[place]

        # If the key is found in the hash table then remove the item
        if key in location:
            location.remove(key)
