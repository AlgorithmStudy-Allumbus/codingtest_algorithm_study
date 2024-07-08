
def func(f):
	# 1, ops (종류) , 위치 찾기
	f = list(f)
	answer =0
	ops = []
	nums =[]
	s = 0
	for i in range(len(f)):
		if f[i] in ["+","*","-"] :
			ops.append([i,f[i]]) # [idx, + ]
			if len(f[s:i]) >= 1 :
				num= "".join(f[s:i])
			nums.append(num)
			s=i+1
	nums.append("".join(f[ops[-1][0]+1:]))
	nums= list(map(int, nums))
	# 연산자 우선순위
	
	answer = nums[0]
	for j in range(len(ops)):
			if ops[j][1] == "*":
				answer *= nums[j+1]
			elif ops[j][1]  == "-":
				answer -= nums[j+1]
			elif ops[j][1]  == "+":
				answer += nums[j+1]
	return answer 
	

a,b = input().split()
out=max(func(a),func(b))
# print ("Hello Goorm! Your input is " + user_input)
print(out)