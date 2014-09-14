import collections
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        LRUCache.capacity = capacity
        LRUCache.Dict = collections.OrderedDict()
        LRUCache.numItems = 0
        

    # @return an integer
    def get(self, key):
        try:
            val = LRUCache.Dict[key]
            del LRUCache.Dict[key]
            LRUCache.Dict[key] = val
            return val
        except:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            del LRUCache.Dict[key]
            LRUCache.Dict[key] = value
            return
        except:
            if LRUCache.numItems == LRUCache.capacity:
                LRUCache.Dict.popitem(last = False)
                LRUCache.numItems -= 1
            LRUCache.Dict[key] = value
            LRUCache.numItems +=1
        return
s = LRUCache(2)
s.set(2,8)  
s.set(3,2)
s.set(4,9)
print s.get(2)     