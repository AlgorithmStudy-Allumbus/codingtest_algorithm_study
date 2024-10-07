"""
#dp : 1, 중복 , 최적 부분  -> memorize 
goal :최대 이익 
input : time , price , 0 

#1. 역순으로 N ~ 1 (퇴사일 N+1)
for i in range(N , 0 , -1)
#2-1 상담 가능 여부 (1)
if i + T_i <= N 이면 -> 가능
if not -> false (0) 

# 2-2 최대 효율
리스트 dp :  
dp[i] = 현재 price + 바로 담 상담 price VS 내일 상담 price
dp[i] = max(P[i] + dp[i+T_i] , P[i+1])
"""



import sys
n = int(sys.stdin.readline())
schedules = [[]]
for i in range(n) :
    t , p = map(int , sys.stdin.readline().split())
    schedules.append([t,p])

check = 0

dp = [0 for _ in range(n+2)]

for d in range(n ,0, -1 ) :
    t_i , p_i  = schedules[d]
    #1. 상담 가능여부
    if d + t_i  >  n+1 : # 상담 불가능
        dp[d] = dp[d+1]
    else : #상담 가능
        dp[d] = max(p_i + dp[d + t_i] , dp[d+1] ) 
        
print(dp[1])


def train_epoch_boosting(self, model, previous_model = None):
        '''
        부스팅을 적용한 학습 (1 에폭)
        '''
        model.train()
        total_loss = 0.0
        acc_cum = 0
        progress_bar = tqdm(self.train_loader, desc='Training with Boosting')
        print(len(self.models), 'Exists' if previous_model is not None else 'None') # 나중에 지울 부분
        for i,(images, targets) in enumerate(progress_bar):
            images, targets = images.to(self.device), targets.to(self.device)
            self.optimizer.zero_grad()
            
            # 현재 모델 예측
            print(f"Image.shape: {images.shape}")
            print(f"targets.shape: {targets.shape}")
            outputs = model(images)
            acc_cum += self.accuracy(outputs, targets)
            # 틀린 예측에 대한 가중치 적용wh
            if previous_model is not None: # 이전 모델이 존재하는 경우. 즉, Base 모델이 아닌 경우에 대해서만 Penalty 계산 후, 적용
                previous_model.eval()
                with torch.no_grad():
                    prev_outputs = previous_model(images)
                    print('이전 모델의 정확도:',self.accuracy(prev_outputs, targets))
                    print('현재 모델의 정확도:', self.accuracy(outputs, targets))
                # penalty_weights = self.boost_weights(prev_outputs, targets)
                loss = self.loss_fn(outputs, targets) # * penalty_weights.to(self.device)
                # loss = loss.mean()
            else:
                loss = self.loss_fn(outputs, targets)
                    
            
            loss.backward()
            self.optimizer.step()
            self.scheduler.step()
            total_loss += loss.item()
            progress_bar.set_postfix(loss=loss.item(), acc = acc_cum / (i+1))