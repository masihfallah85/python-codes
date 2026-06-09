#hashtable.py

"""a simple hash table code example"""


class hashtable:

    """hash table class"""

    def __init__(self, size=10):

        """constructor"""

        self.size = size

        self.table = [[] for _ in range(self.size)]

        self.count = 0
    
    def _hash(self, key):

        """hash function """

        return hash(key) % self.size
    
    def insert(self, key, value):

        """add or update a pair"""

        index = self._hash(key)

        bucket = self.table[index]
        
        for i , (k , v) in enumerate(bucket):

            if k == key:

                bucket[i] = (key, value)

                return
        
        bucket.append((key, value))

        self.count += 1
    
    def get(self, key):

        """return value by key"""

        index = self._hash(key)

        bucket = self.table[index]
        
        for k, v in bucket:

            if k == key:

                return v
        
        raise KeyError(f"key {key} not found")
    
    def delete(self, key):

        """remove a pair"""

        index = self._hash(key)

        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):

            if k == key:

                del bucket[i]

                self.count -= 1

                return
        
        raise KeyError(f"key {key} not found")
    
    def __len__(self):

        """return number of items in table"""

        return self.count
    

# example usage
if __name__ == "__main__":

    ht = hashtable()
    
    # insert some data
    ht.insert("name", "alice")

    ht.insert("age", 30)

    ht.insert("city", "new york")
    
    # retrieve data
    print(f"name: {ht.get('name')}")

    print(f"age: {ht.get('age')}")
    
    # update existing key
    ht.insert("age", 31)

    print(f"updated age: {ht.get('age')}")
    
    # delete a key
    ht.delete("city")
    
    # number of items
    print(f"total items: {len(ht)}")
