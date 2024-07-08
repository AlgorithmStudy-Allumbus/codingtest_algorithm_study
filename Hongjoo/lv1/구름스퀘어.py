
# input
events =[] # [start , end]
# n = map(int, input())
# for i in range(n):
# 	s, e = map(int,input().split())
# 	events.append([s,e])

n = int(input())
for i in range(n):
	s,e = map(int, input().split())
	s= int(s); e= int(e)
	events.append([s,e])
#우선순위 greedy : 끝나는 시간 빠른 순 정렬 -> 시작시간 빠른 순
events.sort(key= lambda x: x[1])
schdule = []
end_time = -1
count= 0
for event in events : 
	if event[0] > end_time :
		schdule.append(event)
		count+= 1
		end_time = event[1]
	
# count = len(schdule)

# print(f'schedule {schdule}, ->  {count}')	
print(count)
