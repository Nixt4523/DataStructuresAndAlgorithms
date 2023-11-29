# Hashmap in Python
"""
A Hashmap is a Data structure that uses
pair of Keys and Values
Each value is given one of a kind Key created by Hash Function
A good Hashing function has minimalistic Collision
Hashmap is called Dictionary in Python
"""

hashmap = {'name': 'Nikhil', 'age': 19, 'Programmer': True}

# Hashmap Functions in Python

# Accessing element from Hashmap
name = hashmap['name']
'''
Gets the value of the Key 'name' in hashmap i.e 'Nikhil'
The time complexity of this Function is O(1)
'''

# Adding Key Value pairs in Hashmap
hashmap['Coffee'] = True
'''
Inserts the given Key and Value in the hashmap i.e 'Coffee': True
The time complexity of this Function is O(1)
'''

# Updating Values of the Key in Hashmap
hashmap['name'] = 'Nikhil Thorat'
'''
Updates the value of given Key in hashmap i.e 'name': 'Nikhil Thorat'
The time complexity of this Function is O(1)
'''

# Removing Key Value pairs from Hashmap
del hashmap['age']
'''
Deletes the given Key and its value from the Hashmap
The time complexity of this Function is O(1)
'''


# Implementing the Hashmap in Python
class Hashmap:
    def __init__(self, size):
        self.size = size
        self.hashmap = [[] for _ in range(0, self.size)]

    def hash_function(self, key):
        hashed_key = hash(key) % self.size
        '''
        In the above line we are using in-build Python hash Function
        This function hashes the given Key 
        After the given Key is hashed it is divided by size of hashmap
        So that the Key will be stored in the range of our hashmap size
        '''
        return hashed_key

    def set(self, key, val):
        hash_key = self.hash_function(key)
        key_exists = False
        slot = self.hashmap[hash_key]

        for i, k_v in enumerate(slot):
            k, v = k_v
            if key == k:
                key_exists = True
                break

        if key_exists:
            slot[i] = ([key, val])
        else:
            slot.append([key, val])

    def get(self, key):
        hash_key = self.hash_function(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                return 'Key does not Exist!'

    def __setitem__(self, key, val):
        return self.set(key, val)

    def __getitem__(self, key):
        return self.get(key)


'''
We can initialize the Hashmap class i.e Hashmap()
We can use the methods in the Hashmap class to add or remove elements
'''

# Hashmap Questions

# Question 1
'''
You're given a String 'stones' that contains stones
Each character in a stone is a type of stone we have
You're also given a String 'jewels' that represents types of stones that are also jewels
Find out how many stones you have are also jewels
Input : stones = 'aAAbbbb', jewels = 'aA'
Output : 3
'''


def num_of_jewels_in_stones(jewels, stones):
    jewels_hashmap = {}

    for i in range(0, len(jewels)):
        jewels_hashmap[i] = jewels[i]

    answer = 0

    for stone in stones:
        if stone in jewels_hashmap.values():
            answer += 1

    return answer

