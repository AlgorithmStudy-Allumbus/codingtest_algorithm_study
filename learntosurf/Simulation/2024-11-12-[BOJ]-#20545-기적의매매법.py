import sys 
input = sys.stdin.readline 

money = int(input())
machineduck = list(map(int, input().split())) 

# 준현 
j_stock = 0 
j_money = money 

for i in machineduck: 
    if j_money >= i: 
        j_stock += j_money // i 
        j_money %= i

# 성민 
s_stock = 0 
s_money = money 

for i in range(3, len(machineduck)): 
    if (machineduck[i-3] > machineduck[i-2]) and (machineduck[i-2] > machineduck[i-1]) and (machineduck[i-1] > machineduck[i]): 
        if s_money >= machineduck[i]:
            s_stock += s_money // machineduck[i] 
            s_money %= machineduck[i]
    
    elif (machineduck[i-3]<machineduck[i-2]) and (machineduck[i-2]<machineduck[i-1]) and (machineduck[i-1]<machineduck[i]): 
        if s_stock > 0: 
            s_money += s_stock * machineduck[i] 
            s_stock = 0

j_result = j_money + j_stock * machineduck[-1]
s_result = s_money + s_stock * machineduck[-1]

if j_result > s_result: 
    print("BNP")
elif j_result < s_result:
    print("TIMING")
else: 
    print("SAMESAME")