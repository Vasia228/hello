import copy
#########################################################
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))
#
def print_2d(myList):
    for i in range(len(myList)):
        for j in range(len(myList[i])):
            print(myList[i][j], end = ' ')
        print()
    print("__________")
#
def printTrue_2d(myList):
    for i in range(len(myList)):
        for j in range(len(myList[i])):
            if myList[i][j]==0:
                print('  ', end='')
            else:
                print(KEY[myList[i][j]], end = ' ')
        print()
    print("__________")
#
def s_calculation(myList):
    s=0
    for i in range(len(myList)):
        for j in range(len(myList[i])):
            if myList[i][j]!=0:
                NeedCord=[(myList[i][j]-1)//3,(myList[i][j]-1)%3]
                s+=abs(NeedCord[0]-i)
                s+=abs(NeedCord[1]-j)
    return s
#
class position():
    def __init__(self,field,mother):
        self.Field=field
        self.Mother=mother
        if mother==0:
            self.H=0
        else:
            self.H=mother.H+1
        self.S=s_calculation(field)
        self.W=self.S+self.H
#
def Add_and_Check(Field,mother):
    for e in list_of_checked:
        if Field==e.Field:
            return 0
    tmp=position(Field,mother)
    if tmp.S==0:
        list_of_search.append(tmp)
        return 1
    for e in range(len(list_of_search)):
        if tmp.S==list_of_search[e].S and tmp.Field==list_of_search[e].Field:
            if tmp.H<list_of_search[e].H:
                del list_of_search[e]
                return 0
            else:
                return 0
    list_of_search.append(tmp)
    return 0
##################################################
start=[]
File=open('Data.txt','r')
tmp=0
SIZE=3
for l in range(SIZE):
    start.append([])
    line=File.read(SIZE+1)
    for letter in line:
        if letter!='\n':
            start[tmp].append(letter)
    tmp+=1
KEY=File.read(SIZE*SIZE-1)
File.close()
KEY='0'+KEY[:]
CheckCollision=[0]*len(KEY)
for l in range(SIZE):
    for e in range(SIZE):
        tmp=KEY.index(start[l][e])
        while CheckCollision[tmp]!=0:
            tmp=tmp+1+KEY[tmp+1:].index(start[l][e])
        start[l][e]=tmp
        CheckCollision[tmp]=1
CheckCollision=line=tmp=None
##################################################
list_of_search=[]
list_of_checked=[]
list_of_search.append(position(start,0))
start=0
f=0
print('#',end='')
while(len(list_of_search)!=0):
    f+=1
    min_w=[list_of_search[0].W,0]
    for i in range(len(list_of_search)):
        if min_w[0]>=list_of_search[i].W:
            min_w[0]=list_of_search[i].W
            min_w[1]=i
    currentCheck=list_of_search[min_w[1]]
    list_of_checked.append(list_of_search[min_w[1]])
    del list_of_search[min_w[1]]

    cords=index_2d(currentCheck.Field,0)

    if cords[0]>0:#possible to move top element
        newField=copy.deepcopy(currentCheck.Field)
        newField[cords[0]][cords[1]],newField[cords[0]-1][cords[1]]=newField[cords[0]-1][cords[1]],newField[cords[0]][cords[1]]
        if Add_and_Check(newField,currentCheck)==1:
            break
    if cords[0]<2:#possible to move bottom element
        newField=copy.deepcopy(currentCheck.Field)
        newField[cords[0]][cords[1]],newField[cords[0]+1][cords[1]]=newField[cords[0]+1][cords[1]],newField[cords[0]][cords[1]]
        if Add_and_Check(newField,currentCheck)==1:
            break
    if cords[1]>0:#possible to move left element
        newField=copy.deepcopy(currentCheck.Field)
        newField[cords[0]][cords[1]],newField[cords[0]][cords[1]-1]=newField[cords[0]][cords[1]-1],newField[cords[0]][cords[1]]
        if Add_and_Check(newField,currentCheck)==1:
            break
    if cords[1]<2:#possible to move right element
        newField=copy.deepcopy(currentCheck.Field)
        newField[cords[0]][cords[1]],newField[cords[0]][cords[1]+1]=newField[cords[0]][cords[1]+1],newField[cords[0]][cords[1]]
        if Add_and_Check(newField,currentCheck)==1:
            break
    if f==50:
        f=0
        print('*',end='')
print('#')
list_of_checked.append(list_of_search[-1])        
list_of_search.clear()
tmp=list_of_checked[-1]
path=[]
while(tmp.Mother!=0):
    path.append(list_of_checked.index(tmp))
    tmp=tmp.Mother
path.append(list_of_checked.index(tmp))
path.reverse()
print("Миниммальное число ходов={}".format(len(path)-1))
input("Нажать чтобы вывести")
for e in range(len(path)):
    print('Ход ',format(e))
    printTrue_2d(list_of_checked[path[e]].Field)
##################################################
