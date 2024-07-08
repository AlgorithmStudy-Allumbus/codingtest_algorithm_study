
#1. input 
n,k = input().split()
a = list(input().split())

# n,k = "5 2".split()
# a = list("10 20 22 12 11".split())
count = 0
for i in range(len(a)):
	if k in a[i]:
		count+=1

answer = int(n) - count
print(f"{answer}")


# print ("Hello Goorm! Your input is " + user_input)