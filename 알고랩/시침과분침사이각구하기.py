t = int(input())
for i in range(t):
    h, m = map(int, input().split()) # 시간 입력받기 
    h_d = h*30 + m/2 # 시침의 각도/1시간에 30도씩 + 1분에 0.5도씩 움직임 
    m_d = m*6 # 분침의 각도/1분에 6도씩 움직임 
    if h_d >= m_d: # 시침의 각도가 분침의 각도보다 크거나 같을 때 
        angle_a = h_d - m_d # 사이각은 시침의 각도 - 분침의 각도
    else: # 시침의 각도가 분침의 각도보다 작을 때
        angle_a = m_d - h_d # 사이각은 분침의 각도 - 시침의 각도 

    if angle_a > 180: # 사이각이 180보다 클 때
        angle_a = 360 - angle_a # 사이각은 360 - 180
    
    print(int(angle_a)) # 정수로 출력 

# 1분에 6도씩 움직임
# 시침은 1분에 0.5도씩 움직임 