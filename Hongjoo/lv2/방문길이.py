def goTo (start,d): 
# start : starting poing , d : 1 dirrection
# output : endpoint []
    if d == "U": # up
        end = [start[0], start[1]+1]
    elif d == "D" : # down
        end = [start[0], start[1]-1]
    elif d == "R" :# Right
        end = [start[0]+1, start[1]]
    elif d == "L": # Left
        end = [start[0]-1, start[1]]
    return  end

def solution(dirs):
    answer = 0
    start = [0,0]
    end =[0,0]
    allRoot=[[]]
    # record root about all dirs
    for d in dirs : 
        dupli = False
        end = goTo(start,d)
            # Find is it exit in map
        if -5>end[0] or end [0]>5 or -5>end[1] or end [1]>5:
            continue
        newroot = [start, end]
        print("d",d)
        # Search same root
        for i in range(len(allRoot)) :
            if allRoot[i] == [start,end] or allRoot[i] == [end,start] :
                dupli = True
                break
        # update root in allRoot
        if dupli == False:
            allRoot.append(newroot)   
        start= end

    del allRoot[0]
    answer = len(allRoot)
    return answer