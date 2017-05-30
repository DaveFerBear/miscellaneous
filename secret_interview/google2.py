import operator

def answer(s):
    temp = ""
    for c in s:
        if (ord(c) <= 122 and ord(c) >= 97):
            temp += chr(-1*ord(c) + 219);
            print(ord(c))
        else:
        	temp += c
    return temp

def numMoves(x,y):
    x = abs(x)
    y = abs(y)
    if y > x:
        temp=y
        y=x
        x=temp  
    if (x==2 and y==2):
        return 4
    if (x==1 and y==0):
        return 3

    if(y == 0 or float(y) / float(x) <= 0.5):
        xClass = x % 4
        if (xClass == 0):
            initX = x/2
        elif(xClass == 1):
            initX = 1 + (x/2)
        elif(xClass == 2):
            initX = 1 + (x/2)
        else:
            initX = 1 + ((x+1)/2)

        if (xClass > 1):
            return initX - (y%2)
        else:
            return initX + (y%2)
    else:
        diagonal = x - ((x-y)/2)
        if((x-y)%2 == 0):
            if (diagonal % 3 == 0):
                return (diagonal/3)*2
            if (diagonal % 3 == 1):
                return ((diagonal/3)*2)+2
            else:
                return ((diagonal/3)*2)+2
        else:
            return ((diagonal/3)*2)+1

def compare(a,b):
    if (len(a) == 0 and len(b) != 0): return -1
    if (len(b) == 0 and len(a) != 0): return 1
    if (len(a) == 0 and len(b) == 0): return 0
    if (int(a[0]) > int(b[0])): return 1
    elif (int(a[0]) < int(b[0])): return -1
    return compare(a[1:], b[1:])

def concat(a):
    string = ""
    for x in a:
        string+=str(x)
        string+="."
    return string[:-1]

def answer2(l):
    l = [x.split(".") for x in l]
    l.sort(compare)
    l = [concat(x) for x in l]
    return l

def answer3(m):
    order = range(0,len(m))
    m = [[1 if sum(m[i]) is 0 and i==j else m[i][j] for j in range(0,len(m))] for i in range(0,len(m))] # Add missing ones to terminal rows
    m = [[(float(i)/sum(j)) for i in j] for j in m] # Normalize the Matrix Rows
    
    return m


M = [
[0,1,0,0,0,1],
[4,0,0,3,2,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]
]
A = answer3(M)
for row in A:
    print(row)

