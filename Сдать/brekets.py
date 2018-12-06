#origin="????????????????????????????????????????"
#origin="??????????????????????????????"
origin="????????????????????"
#origin="????"
print(origin)

if len(origin)%2!=0 or origin[0]==")" or origin[-1]=="(":
    print("Не корректные входные данные")
    raise SystemExit

origin="("+origin[1:-1]+")"

counters=[0]
remaining=len(origin)
deadlist=[]
tmp=[]

for elem in origin:
    print(remaining)
    remaining-=1

    if elem == "(" or elem==")":
        data=-1
        if elem=="(":
            data=1
        for index in range(len(counters)):
            counters[index]+=data
            if counters[index] < 0 or counters[index]>remaining:
                deadlist.append(index)

    else:
        for index in range(len(counters)):
            if (counters[index]-1)>=0:
                counters.append(counters[index]-1)
            if counters[index]+1<=remaining:
                counters[index]+=1
            else:
                deadlist.append(index)
    
    for e in deadlist:
        counters[e]=counters.pop()
    deadlist.clear()

print("Ans:",len(counters))


