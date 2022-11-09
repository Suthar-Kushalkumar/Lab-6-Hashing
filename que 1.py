def hashtable(keys,key):
    M=key
    Max=0
    a=[]
    l=0
    for key in keys:
        n=key%M
        if n>Max:
            Max=n
    for i in range(Max+1):
        a=a+[None]
    for j in keys:
        k=j%M
        if a[k]==None:
            a[k]=j
        else:
            for h in range(k,Max):
                if a[h]==None:
                    l=l+1
            if l!=0:
                for g in range(k+1,Max):
                    if a[g]==None:
                        a[g]=j
                        l=0
                        break
            else:
                for t in range(0,k):
                    if a[t]==None:
                        a[t]=j
                        break
    return a
def search(hashtables,number,key):
    r=number%key
    l=len(hashtables)
    if r>l:
        print("Index is out of range./ Not found")
        return
    h=0
    for o in range(r,l):
        if hashtables[o]==number:
            print("Found")
            h=1
            return
    if h==0:
        for z in range(0,r):
            if hashtables[z]==number:
                print("Found")
                h=2
                return
    if h==0:
        print("Not found")
        return
p=int(input("How many elements do you want to add in your Keys: "))
ks=[]
for b in range(0,p):
    x=int(input("Enter element: "))
    ks=ks+[x]
K=int(input("Enter key: "))
print("Keys: ",ks)
print("Hash function(key): ",K)
print("Hash table: ",hashtable(ks,K))
S=hashtable(ks,K)
e=int(input("Which element do you want to find: "))
search(S,e,K)
