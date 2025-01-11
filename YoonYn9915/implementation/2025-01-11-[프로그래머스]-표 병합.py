def solution(commands):
    answer = []
    graph = [[(i, j) for j in range(50)] for i in range(50)]
    value = [["EMPTY"] * 50 for _ in range(50)]
    for command in commands:
        command = command.split(' ')
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r,c,value = int(command[1])-1,int(command[2])-1,command[3]
                x,y = graph[r][c]
                value[x][y] = value
            elif len(command) == 3:
                value1, value2 = command[1], command[2]
                for i in range(50):
                    for j in range(50):
                        if value[i][j] == value1:
                            value[i][j] = value2
        elif command[0] == 'MERGE':
            r1,c1,r2,c2 = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1
            x1,y1 = graph[r1][c1]
            x2,y2 = graph[r2][c2]
            if value[x1][y1] == "EMPTY":
                value[x1][y1] = value[x2][y2]
            for i in range(50):
                for j in range(50):
                    if graph[i][j] == (x2,y2):
                        graph[i][j] = (x1,y1)
        elif command[0] == 'UNMERGE':
            r, c = int(command[1])-1,int(command[2])-1
            x, y = graph[r][c]
            tmp = value[x][y]
            for i in range(50):
                for j in range(50):
                    if graph[i][j] == (x,y):
                        graph[i][j] = (i,j)
                        value[i][j] = "EMPTY"
            value[r][c] = tmp
        elif command[0] == 'PRINT':
            r, c = int(command[1])-1, int(command[2])-1
            x, y = graph[r][c]
            answer.append(value[x][y])
    return answer