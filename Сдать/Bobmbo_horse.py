import copy

def bombo_check(data):
    num=list(data)
    b=0
    while(field_trace[num[0]][num[1]]!=0):
        if num in walls:
            b+=1;
        num=field_trace[num[0]][num[1]]
    return b
food=(7,0)
horse=(0,0)
size=8
bombs=1


fields=[[0]*size for i in range(size)]
fields[food[0]][food[1]]=1
fields[horse[0]][horse[1]]="h"
ways={(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)}

field_trace=copy.deepcopy(fields)
field_trace[food[0]][food[1]]=0

walls=[[2,1],[2,0],[4,2],[1,2]]

cur=1
flag=1
element=[]
b=[]
element2=[(food[0],food[1])]
while(flag and cur<20):
    element=element2.copy()
    element2.clear()
    b.clear()
    for data in element:
        for direction in ways:
            Y,X=data[0]-direction[0],data[1]-direction[1]
            if 0<=Y<size and 0<=X<size:
                if fields[Y][X]==0: 
                    fields[Y][X]=cur+1
                    field_trace[Y][X]=[data[0],data[1]]
                    element2.append((Y,X))
                elif fields[Y][X]=="h":
                    i=bombo_check(data)
                    if bombs-i >= 0:
                        flag=0
                        b.append(i)
    cur+=1
    
fields.reverse()
for i in fields:
    for j in i: 
        print(j,end=" ")
    print()
print("Необходимо {0} ходов и {1} из {2} бомб".format(cur-1,min(b),bombs))
