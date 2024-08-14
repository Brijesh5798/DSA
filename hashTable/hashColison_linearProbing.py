class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]
    
    def getHash(self, key):
        hash = 0
        for i in key:
            hash = hash + ord(i)
        index = hash%10
        return index
    
    def increaseList(self):
        self.arr = self.arr + [None] * (len(self.arr)*2)
    
    def __setitem__(self, key, value):
        h = self.getHash(key)
        if self.arr[h] == None:
            self.arr[h] = (key,value)    
        else:
            new_h = self.find_slot(key,h)
            self.arr[new_h] = (key,value)
            
    def find_slot(self,key,h):
        prob_range = self.get_prob_range(h)
        for i in prob_range:
            if self.arr[i] is None:
                return i
            if self.arr[i][0] == key:
                return i
        raise Exception("Hashmap full")
                
    def get_prob_range(self,index):
        return [*range(index , len(self.arr))] + [*range(0,index)]
    
    def __getitem__(self,key):
        h = self.getHash(key)
        if self.arr[h] is None:
            return 
        if self.arr[h][0] == key:
            return self.arr[h][1]
        prob_range = self.get_prob_range(h)
        for i in prob_range:
            if self.arr[i] is None:
                return
            if self.arr[i][0] == key:
                return self.arr[i][0]
    
    def __delitem__(self,key):
        h = self.getHash(key)
        if self.arr[h] is None:
            return
        if self.arr[h][0] == key:
            self.arr[h] = None
            print(self.arr)
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index]=None
        print(self.arr)
        
t = HashTable()
t["march 6"] = 20
print(t.arr)
t["march 17"] =  88
t["march 17"] = 29
t["nov 1"] = 1
t["march 33"] = 234
print(t.arr)
print(t["dec 1"])
print(t["march 33"])