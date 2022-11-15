def hashtable(keys,key):
    M=key
    Max=0
    a=[]
    l=0
    q=0
    y=0
    w=0
    z=0
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
                while (y<Max):
                    y=(j+q*q)%M
                    if a[y]==None:
                        a[y]=j
                        l=0
                        break
                    q=q+1
            else:
                while (w<k):
                    w=(z*z)
                    if a[w]==None:
                        a[w]=j
                        break
                    z=z+1
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
