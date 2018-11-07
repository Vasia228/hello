MAX=1500
COLLISION=0
from random import randint
class helem:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next_h=None

def hashFun(k):
    h=k%MAX
    return h

def search(k):
    h=hashFun(k)
    if index[h] != None:
        p = index[h]
        while (1):
            if p.key == k:
                return p
            else:
                p = p.next_h

            if p==None: #end 
                break
    return h

def insert(k,v):
    h=search(k)
    if type(h) is not int:
        return 0
    if index[h]==None:
        index[h]=helem(k,v)
        return 1
    else:
        global COLLISION
        COLLISION+=1
        prev=index[h]
        while(prev.next_h!=None):
            prev=prev.next_h
        prev.next_h=helem(k,v)
        return 1
    return 0

        
COLLISION2=0

class entry:
    def __init__(self,k,v):
        self.key=k
        self.value=v
        
def insertentry(k,v):
    h=hashFun(k)
    if buckets[h]==None:
        buckets[h]=entry(k,v)
        return 1
    else:
        global COLLISION2
        COLLISION2+=1
        while(buckets[h]!=None):
            h+=1
            if h==MAX:
                h=0
        buckets[h]=entry(k,v)
        return 1
    
def getentry(k):
    h=hashFun(k)
    if buckets[h]==None:
        return 0
    while(1):
        if buckets[h].key==k:
            return buckets[h]
        else:
            h+=1
            
index=[None for i in range(MAX)]
buckets=[None for i in range(MAX)]
keys=[]
for i in range(1000):
    while (1):
        k=randint(0,10000)
        if k not in keys:
            break
    keys.append(k)
    value="v"*randint(0,3)+"a"*randint(0,3)+"s"*randint(0,3)
    insert(k,value)
    insertentry(k,value)


print(COLLISION)
print(COLLISION2)



