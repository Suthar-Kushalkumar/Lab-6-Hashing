def hashtable(keys,key,size):
    M=key
    a=[]
    l=0
    for i in range(size+1):
        a=a+[None]
    for j in keys:
        k=j%M
        if a[k]==None:
            a[k]=1

    return a
def search(hashtable1,hashtable2,number,key1,key2):
    r1=number%key1
    r2=number%key2
    if hashtable1[r1]==1 and hashtable2[r2]==1:
        print("Found")
    else:
        print("Not found")

print("#Hash table1 \n")
p=int(input("Size of your hashtable: "))
n=int(input("Enter number of elements you want to add in this hashtable: "))
ks=[]
for b in range(0,n):
    x=int(input("Enter element: "))
    ks=ks+[x]
K=int(input("Enter key: "))
print("Keys: ",ks)
print("Hash table: ",hashtable(ks,K,p))

print("\n#Hash table2 \n")
p2=int(input("Size of your hashtable: "))
n2=int(input("Enter number of elements you want to add in this hashtable: "))
ks2=[]
for c in range(0,n2):
    x2=int(input("Enter element: "))
    ks2=ks2+[x2]
K2=int(input("Enter key: "))
print("Keys: ",ks2)
print("Hash table: ",hashtable(ks2,K2,p2))
S=hashtable(ks,K,p)
S2=hashtable(ks2,K2,p2)
e=int(input("Which element do you want to find: "))
search(S,S2,e,K,K2)
search(S,S2,100,K,K2)
search(S,S2,133,K,K2)
search(S,S2,174,K,K2)
