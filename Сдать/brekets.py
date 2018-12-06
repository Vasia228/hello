origin="????????????????????"
print(origin)

if len(origin)%2!=0 or origin[0]==")" or origin[-1]=="(":
    print("Не корректные входные данные")
    raise SystemExit

origin="("+origin[1:-1]+")"

buf=[""]
counters=[0]
remaining=len(origin)
deadlist=[]

for elem in origin:
    remaining-=1

    if elem == "(" or elem==")":
        data=-1
        if elem=="(":
            data=1
        for index in range(len(buf)):
            buf[index]+=(elem)
            counters[index]+=data
            if counters[index] < 0 or counters[index]>remaining:
                deadlist.append(index)
    else:
        for index in range(len(buf)):
            if (counters[index]-1)>=0:
                buf.append(buf[index]+")")
                counters.append(counters[index]-1)
            if counters[index]+1<=remaining:
                buf[index]+="("
                counters[index]+=1
            else:
                deadlist.append(index)
    for e in deadlist:
        buf[e]=buf.pop()
        counters[e]=counters.pop()
    deadlist.clear()
print(len(buf))


