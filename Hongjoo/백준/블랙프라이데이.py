import sys

N, target = map(int , sys.stdin.readline().split())
li = sorted(list(map(int, sys.stdin.readline().split())))


# 최대 3개
# 1개 
def check_fit():
  if target in li : 
    return 1
  else :  # 2개, 3개 , 안됨
    left= 0; right = N-1
    while left < right : 
      if target == sum([li[left],li[right]]) :
        return 1
      elif target > sum([li[left],li[right]]):
        diff = target - sum([li[left],li[right]])
        if diff in li and diff !=li[left] and diff != li[right]  : 
          return 1 
        else : 
          left += 1
      else : # target < sum
        right -= 1
    # 3개 조합
  return 0 

print(check_fit())