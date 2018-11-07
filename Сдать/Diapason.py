import copy
def index_2d(myList, v):
    for i, x in enumerate(myList.Field):
        if v in x:
            return (i, x.index(v))
class position():
    def __init__(self,field,mother):
        self.Field=field
        self.Mother=mother
        if mother==0:
            self.H=0
        else:
            self.H=mother.H+1
start=[["П","А","Д"],["Н","И","А"],["О","З","0"]]
example=[["Д","И","А"],["П","А","З"],["О","Н","0"]]
need_to_check=[]
checked=[]
need_to_check.append(position(start,0))
i=0
while(1):
    currentCheck=need_to_check[0]
    del need_to_check[0]
    if currentCheck.Field in checked:
        continue
    if currentCheck.Field == example:
        break
    cords=index_2d(currentCheck,"0")

    if cords[0]>0:#possible to move top element
        newField=copy.deepcopy(currentCheck.Field)
        newField[cords[0]][cords[1]],newField[cords[0]-1][cords[1]]=newField[cords[0]-1][cords[1]],newField[cords[0]][cords[1]]
        need_to_check.append(position(newField,currentCheck))
        
    if cords[0]<2:#possible to move bottom element
        newField=copy.deepcopy(currentCheck.Field)
        newField[cords[0]][cords[1]],newField[cords[0]+1][cords[1]]=newField[cords[0]+1][cords[1]],newField[cords[0]][cords[1]]
        need_to_check.append(position(newField,currentCheck))

    if cords[1]>0:#possible to move left element
        newField=copy.deepcopy(currentCheck.Field)
        newField[cords[0]][cords[1]],newField[cords[0]][cords[1]-1]=newField[cords[0]][cords[1]-1],newField[cords[0]][cords[1]]
        need_to_check.append(position(newField,currentCheck))

    if cords[1]<2:#possible to move right element
        newField=copy.deepcopy(currentCheck.Field)
        newField[cords[0]][cords[1]],newField[cords[0]][cords[1]+1]=newField[cords[0]][cords[1]+1],newField[cords[0]][cords[1]]
        need_to_check.append(position(newField,currentCheck))

    checked.append(currentCheck.Field)
checked=None
need_to_check=None
line=[]
while currentCheck!=0:
    line.append(currentCheck.Field)
    currentCheck=currentCheck.Mother
print("Done! Need {} move".format(len(line)-1))
line.reverse()
for e in range(len(line)):
    print("------{}------".format(e))
    for i in line[e]:
        print(i)
    print("-------------")
