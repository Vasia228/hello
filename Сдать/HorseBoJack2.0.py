
from copy import *
# In[1]:

size=8
bomb=0
origin=[[2,1,1,1,0,1,1,1],
        [0,1,1,1,1,1,1,1],
        [1,0,1,0,1,0,1,1],
        [1,1,1,1,1,1,1,0],
        [1,1,0,1,1,1,1,1],
        [1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1],
        [0,0,0,0,1,1,1,3]] #1-wall,2-horse,3-food
for i in range(len(origin)):
    for j in range(len(origin[i])):
        if origin[i][j]==2:
            horse=(i,j)
        elif origin[i][j]==3: 
            food=(i,j)

# In[2]:


fields=[]
#fields[food[0]][food[1]]=1
#fields[horse[0]][horse[1]]="h"
for i in range(bomb+1):
    fields.append([])
    for j in range (size) :
        fields[i].append([0]*size)
    fields[i][horse[0]][horse[1]]=1


ways={(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)}

# In[3]:


cur=1
flag=1
flag2=1
element=[]
element2=[]
for i in range(bomb+1):
    element.append([])
    element2.append([[horse[0],horse[1]]])

while(flag==1 and flag2!=0):
    flag2=0
    
    tmp=element.copy()
    element=element2.copy()
    element2=tmp.copy()

    for b in range(len(fields)):
        for data in element[b]:
            if fields[b][data[0]][data[1]]==cur:
                for direction in ways:
                    Y,X=data[0]+direction[0],data[1]+direction[1]
                    if 0<=Y<size and 0<=X<size:
                        if fields[b][Y][X]==0 and origin[Y][X]!=1:
                            flag2=1
                            fields[b][Y][X]=cur+1
                            element2[b].append([Y,X])
                        elif b!=bomb and origin[Y][X]==1:
                            flag2=1
                            fields[b+1][Y][X]=cur+1
                            element2[b+1].append([Y,X])
                        if origin[Y][X]==3:
                            flag=0

    cur+=1


# In[4]:
counter=[size*size,size*size]
for i in range(len(fields)):
    if 0 < fields[i][food[0]][food[1]] <= counter[1]:
            if i<counter[0]:
                counter[0]=i
if flag2!=0:
    fields.reverse()
    for i in range(len(fields)):
        for j in fields[len(fields)-i-1]:
            for x in j:
                if x !=0:
                    print(x-1,end=" ")
                else:
                    print(x,end=" ")
            print()
        print("------------------------")
    print("Необходимо {0} ходов и {1} из {2} бомб".format(cur-1,counter[0],bomb))
else:
    print("Путь не найден")

