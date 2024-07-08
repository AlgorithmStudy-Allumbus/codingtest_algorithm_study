# n ,k = int(input().split()) # 개수, 특정 정수 위치
# array = list(map(int,input().split()))
def binary(num):
	tmp = ""
	while num	!=0 : 
		if num % 2 == 0 : 
			tmp= "0"+tmp
			num = num // 2
		else :
			tmp = "1" + tmp
			num = num // 2
	return tmp
	
	
n ,k = map(int,input().split()) # 개수, 특정 정수 위치
array = list(map(int,input().split()))

bcount_o = []
for o in array : 
	l=binary(o).count("1")
	bcount_o.append([l,o])

# 내림차순 정렬
bcount_o.sort(reverse= True)
print(bcount_o[k-1][1])

