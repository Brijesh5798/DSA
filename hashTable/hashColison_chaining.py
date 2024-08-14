class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]
    
    def getHash(self, key):
        hash = 0
        for i in key:
            hash = hash + ord(i)
        index = hash%10
        return index
    
    def __getitem__(self, key):
        index = self.getHash(key)
        for i in self.arr[i]:
            if i[0] == key:
                return i[1]
    
    def __setitem__(self, key, value):
        index = self.getHash(key)
        found = False
        for idx, element in enumerate(self.arr[index]):
            if len(element) == 2 and element[0] == key:
                self.arr[index][idx] = (key,value)
                found = True
                
        if not found:
            self.arr[index].append((key, value))
            
    def __delitem__(self, key):
        index = self.getHash(key)
        for idx, element in enumerate(self.arr[index]):
            if element[0] == key:
                del self.arr[index][idx]
                
t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
print(t.arr)
print(t["march 6"])
print(t["march 17"])
print(t.arr)
t["march 6"] = 11
print(t.arr)
print(t["march 6"])
del t["march 6"]