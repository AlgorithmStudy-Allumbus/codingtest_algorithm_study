while True:
    a = input()
    
    if a == '.':
        break
    stk = []
    ans = True

    for g in a:
        if g =='(' or g == '[':
            stk.append(g)
        elif g == ')':
            if len(stk) == 0:
                ans = False
                break
            if stk[-1] == '(':       
                stk.pop()
            else:
                ans=False
                break
        elif g ==']':
            if len(stk) == 0:
                ans = False
                break
            if stk[-1] == '[':
                stk.pop()
            else:
                ans = False
                break
    
    
    if ans and not stk:
        print("yes")
    else:
        print("no")
