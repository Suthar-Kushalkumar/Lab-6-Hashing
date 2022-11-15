def hashtable(keys,key,key2):
    M=key
    P=key2
    Max=0
    a=[]
    l=0
    y=0
    for key in keys:
        n=key%M
        if n>Max:
            Max=n
    for i in range(Max+1):
        a=a+[None]
    for j in keys:
        k=j%M
        k2=j%P
        if a[k]==None:
            a[k]=j
        else:
            for h in range(1,Max):
                z=k+(h+k2)
                if z>Max:
                    z=z%M
                if a[z]==None:
                    a[z]=j
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
K2=int(input("Enter second key: "))
print("Keys: ",ks)
print("Hash function(key): ",K)
print("Second Hash function(key): ",K2)
print("Hash table: ",hashtable(ks,K,K2))
S=hashtable(ks,K,K2)
e=int(input("Which element do you want to find: "))
search(S,e,K)
