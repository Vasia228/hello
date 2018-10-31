class node():
    def __init__(self,data,left,right,mother):
        self.Data=data
        self.Left=left
        self.Right=right
        self.Mother=mother

def inputNode(root,data):
    curCheck=root
    while(1):
        if data>curCheck.Data:
            if curCheck.Right==0:
                curCheck.Right=node(data,0,0,curCheck)
                return 1
            curCheck=curCheck.Right
        elif data<curCheck.Data:
            if curCheck.Left==0:
                curCheck.Left=node(data,0,0,curCheck)
                return 1
            curCheck=curCheck.Left

def printTree(root):
    if root.Left!=0:
        printTree(root.Left)
    print(root.Data)
    if root.Right!=0:
        printTree(root.Right)

def elementInTree(root,element):
    if root.Data==element:
        return 1
    else:
        if element<root.Data:
            if root.Left!=0:
                if elementInTree(root.Left,element)==1:
                    return 1
                else:
                    return 0
            else:
                return 0
        elif element>root.Data:
            if root.Right!=0:
                if elementInTree(root.Right,element)==1:
                    return 1
                else:
                    return 0
            else:
                return 0

def searchNode(root,e):
    curCheck=root
    while e!=curCheck.Data:
        if e>curCheck.Data:
            if curCheck.Right!=0:
                curCheck=curCheck.Right
            else:
                return 0
        elif e<curCheck.Data:
            if curCheck.Left!=0:
                curCheck=curCheck.Left
            else:
                return 0
    return curCheck

def deleateNode(root,e):
    aimElement=searchNode(root,e)
    if aimElement==0:
        return 0
    if aimElement.Right==0 and aimElement.Left==0:
        if aimElement.Data>aimElement.Mother.Data:
            aimElement.Mother.Right=0
        else:
            aimElement.Mother.Left=0
        aimElement=None
        return 1
    elif aimElement.Right==0 and aimElement.Left!=0:
        if aimElement.Data>aimElement.Mother.Data:
            aimElement.Mother.Right=aimElement.Left
        else:
            aimElement.Mother.Left=aimElement.Left
        aimElement=None
        return 1
    elif aimElement.Right!=0 and aimElement.Left==0:
        if aimElement.Data>aimElement.Mother.Data:
            aimElement.Mother.Right=aimElement.Right
        else:
            aimElement.Mother.Left=aimElement.Right
        aimElement=None
        return 1
    elif aimElement.Right!=0 and aimElement.Left!=0:
        changeElement=aimElemental.Left
        while(changeElement.Right!=0):
            changeElement=changeElement.Right
        if changeElement.Mother==aimElement.Left:
            changeElement.Right=aimElement.Right
            aimElement.Right.Mother=changeElement
            changeElement.Mother=aimElement.Mother
            if aimElement.Data>aimElemnt.Mother.Data:
                aimElement.Mother.Right=changeElement
            else:
                aimElement.Mother.Left=changeElement
            aimElement=None
            return 1
        else:
            if changeElement.Left!=0:
                changeElement.Mother.Right=changeElement.Left
                changeElement.Left.Mother=changeElement.Mother
            changeElement.Right=aimElement.Right
            aimElement.Right.Mother=changeElement
            changeElement.Left=aimElement.Left
            aimElement.Left.Mother=changeElement
            changeElement.Mother=aimElement.Mother
            if aimElement.Data>aimElement.Mother.Data:
                aimElement.Mother.Right=changeElement
            else:
                aimElement.Mother.Left=changeElement
            aimElement=None
            return 1
def rangeTree(a,b,root):
    flag=1
    prev=root
    while (flag):
        if root.Data==a:
            flag=0
        elif a < root.Data:
            if root.Left != 0:
                root=root.Left
            else:
                flag=0;
        elif a > root.Data:
            if root.Right != 0:
                root=root.Right
            else:
                flag=0;
    flag=1
    prev="left"
    while(flag):
        if a <= root.Data < b:
            print(root.Data)
            if prev=="right":
                if root.Left!=0:
                    rangeHelp(root.Left,a,b)
            elif prev=="left":
                if root.Right!=0:
                    rangeHelp(root.Right,a,b)
        elif root.Data == b:
            print(root.Data)
            flag=0
        elif root.Data < a or root.Data > b:
            flag=0

        if root.Mother==0:
            flag=0
        elif root.Mother.Data > root.Data:
            prev="left"
        elif root.Mother.Data < root.Data:
            prev="right"
        root=root.Mother

        
def rangeHelp(root,a,b):
    if root.Data < a:
        if root.Right!=0:
            rangeHelp(root.Right,a,b)
    elif root.Data > b:
        if root.Left!=0:
            rangeHelp(root.Left,a,b)
    elif a <= root.Data <= b:
        print(root.Data)
        if root.Left!=0:
            rangeHelp(root.Left,a,b)
        if root.Right!=0:
            rangeHelp(root.Right,a,b)
            
######
root=node(4,0,0,0)
input=[9,3,2,6,7,5]
for e in input:
    inputNode(root,e)
print("------Tree------")
printTree(root)
print("------range[3,7]------")
rangeTree(3,7,root)
