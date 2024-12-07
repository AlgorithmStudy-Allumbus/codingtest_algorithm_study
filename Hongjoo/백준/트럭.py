'''
Condition 
1. 다리 - 최대 하중 L , 최대 개수 W , 길이 W 
-단위 시간 에 거리

'''
import sys
# 1. 입력 - 버스 개수 , 다리 길이 , 다리 최대 하중
N , W , L = map(int, sys.stdin.readline.splite()) 
buses = map(int, sys.stdin.readline.splite())
#2. 매 time 마다 bridge 최대 하중을 넘지 않은채 올리기 