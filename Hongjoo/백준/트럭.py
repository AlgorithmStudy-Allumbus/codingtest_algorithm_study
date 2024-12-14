# 실패
import sys
n, w, l = map(int, sys.stdin.readline().split())
truck = list(map(int, sys.stdin.readline().split()))
time, bridge = 0, [0]*w #1. 시간변수와 다리의 길이를 입력받은 횟수만큼 리스트에 저장
while bridge: #2. 다리의 길이가 0이 아닐때까지 반복
    time += 1 #3 time +1
    bridge.pop(0) #4.다리의 첫번째 원소 제거
    if truck: #5.bridge리스트를 추가하는건 truck리스트가 남아있을때까지
        if sum(bridge) + truck[0] <= l: #6기존 다리의 원소의 합 + 가장 왼쪽의 트럭'이 다리의 최대하중과 같거나 작다면.
            bridge.append(truck.pop(0))
        else: #7. 다리에 트럭이 있지만 다리에 올리지 못할 경우 다리 공간 유지하기 위해 0을 삽입
            bridge.append(0) 
print(time)
