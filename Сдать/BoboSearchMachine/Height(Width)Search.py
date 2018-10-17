import os

START='BoboData'
CheckList=[]
CheckList.append(START)
flag=0
while len(CheckList)>0 and flag==0:
    CurDir=CheckList.pop(0) #(-1) - поиск в глубину, (0) - поиск в ширину
    for e in os.listdir(CurDir):
        if '.' in e:
            if e=='Bobo.txt':
                path=CurDir+'\\'+'Bobo.txt'
                print(path,end=': ')
                Handle=open(path,'r')
                print(Handle.read())
                Handle.close()
                flag=1
                break
        else:
            new=CurDir+'\\'+e
            CheckList.append(new)
    
    
