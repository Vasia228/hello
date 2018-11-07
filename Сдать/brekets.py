example = "(????)"
COUNTER=0

if len(example)%2!=0:
    print("No variants")
    raise SystemExit

code={"(":1,")":-1,"?":0}
arr=[]
for e in example:
    arr.append(code.get(e))

def shrink(arr):
    global COUNTER
    print(arr)
    if len(arr)==0:
        COUNTER+=1
        return 0
    if arr[0]==-1 or arr[-1]==1:
        return 0
    else:
        arr[0],arr[-1]=1,-1
    for i in range(len(arr)-1):
        if arr[i]==1 and arr[i+1]==-1:
            if len(arr)==2:
                COUNTER+=1
                return 0
            arr=arr[:i]+arr[i+2:]
    for i in range(len(arr)):
        if arr[i]==0:
            #if i > 0 and arr[i-1]==1:
                #shrink(arr[:i-1]+arr[i+1:])
            if i < (len(arr)-1) and arr[i+1]==-1: 
                shrink(arr[:i]+arr[i+2:])
            if i < (len(arr)-1) and arr[i+1]==0:
                shrink(arr[:i]+arr[i+2:])
shrink(arr)
print(COUNTER)
