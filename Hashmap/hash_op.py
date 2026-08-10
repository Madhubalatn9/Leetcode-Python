class simpleHashmap:
    def __init__(self):
        self.size=100
        self.hash_table=[[] for _ in range(self.size)]
    def put_val(self,key,value):
        hash_key=hash(key)%self.size
        bucket=self.hash_table[hash_key]
        for index,(record_key,_) in enumerate(bucket):
              if(record_key==key):
                    bucket[index]=(key,value)
                    return
        bucket.append((key,value))
    def get_val(self,key):
            hash_key=hash(key)%self.size
            bucket=self.hash_table[hash_key]
            for record_key,record_val in bucket:
                  if(record_key==key):
                        return record_val

            return -1
    def del_val(self,key):
            hash_key=hash(key)%self.size
            bucket=self.hash_table[hash_key]
            for index,(record_key,_) in enumerate(bucket):
                  if(record_key==key):
                        bucket.pop(index)
                        return
    

myhash=simpleHashmap()

# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

print(myhash.put_val(1,1))
print(myhash.put_val(2,2))
print(myhash.get_val(1))
print(myhash.get_val(3))
print(myhash.put_val(2,1))
print(myhash.get_val(2))
print(myhash.del_val(2))
print(myhash.get_val(2))


