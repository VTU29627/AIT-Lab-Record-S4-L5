A=[[1,2],[3,4]]
for i in A:
    for j in i:
        print(j,end=" ")
    print()

print()

g=[[0,0,0],
   [0,1,0],
   [0,0,0]]

for i in g:
    for j in i:
        print(j,end=" ")
    print()

print()

def traversal(g,i,j,list):
    if(i==len(g)-1 and j==len(g[0])-1):
        list.append((i,j))
        print(list)
        return
    
