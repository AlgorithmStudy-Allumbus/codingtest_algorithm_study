a = int(input())

for i in range(a):
    res = []
    b = str(input())
    for c in b:
        if c == '(':
            res.append(c)
        elif c == ')':
            if res:
                res.pop()
            else:
                print("NO")
                break
    else:        
        if len(res) == 0:
            print("YES")
        else:
            print("NO") 
