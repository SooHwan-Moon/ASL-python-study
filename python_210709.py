import numpy as np

# for를 이용한 반복문 수행
# if 를 이용한 조건문 수행

# for 변수 in np.arange(처음, 끝, 중간):
    # 들여쓰기가 중요함!
    # 들여쓰기가 끝났을 때, 그 지점이 종료되는 구간.
    
#%% for 문을 이용한 시간 만들기
# 2019년 1월 1일 00시 부터 2019년 1월 31일 23시 까지의 시간
# 배열로서 만드는 작업을 수행하겠습니다.

Year = 2019
Month = 1
Day = np.arange(1,32,1)
Hour = np.arange(0,24,1)

# 배열의 공백을 미리 만들어놔야 해요.
time = np.ones([31*24,4])
sum = 0

# 단일루프

for iii in np.arange(1,100,1):
       
       for iiii in np.arange(1,100,1):
              sum = sum+1
              print(sum,'번째 입니다')


for ist in np.arange(1,32,1):
       
       time[24*ist-24:24*ist,0] = Year
       time[24*ist-24:24*ist,1] = Month
       time[24*ist-24:24*ist,2] = ist # Day[ist-1]
       time[24*ist-24:24*ist,3] = Hour
       # 등차수열 a1+(n-1)d 
       # 0,24,48,72....  --> 0 + (n-1)*24  --> 24*n-24
       # 24,48,72,.....  --> 24 + (n-1)*24 --> 24*n


## 2중 루프
for ist in np.arange(1,32,1):
    
    for istt in np.arange(0,24,1):
        
        time[sum,0] = Year
        time[sum,1] = Month
        time[sum,2] = ist
        time[sum,3] = istt
        sum = sum+1
        print(sum)
       
#%% UTC time을 KST로 만들기
ksttime = np.array(time)

for kst in np.arange(0,np.size(ksttime,axis=0),1):
       # 시간 열에 대하여 0~14 까지는 +9
       # 시간 열에 대하여 15~23 까지는 -15, Day 열에 +1
       # Day 열이 31일, Hour 열이 15~23, Hour 열은 -15, Month는 +1, Day = 1
       
       if time[kst,3] >= 0 and time[kst,3] <= 14:
              
              ksttime[kst,3] = time[kst,3] + 9
              
       elif time[kst,2] == 31 and time[kst,3] >= 15 and time[kst,3] <= 23:
              
              ksttime[kst,3] = time[kst,3] - 15
              ksttime[kst,2] = 1
              ksttime[kst,1] = time[kst,1] + 1
              
       elif time[kst,3] >= 15 and time[kst,3] <= 23:
       
              ksttime[kst,3] = time[kst,3] - 15
              ksttime[kst,2] = time[kst,2] + 1


ksttime = np.array(time)
ksttime[:,3] = ksttime[:,3]+9

for kstt in np.arange(0,744,1):
       
       if ksttime[kstt,3] >= 24:
              
              ksttime[kstt,3] = ksttime[kstt,3] - 24
              ksttime[kstt,2] = ksttime[kstt,2] + 1
              
ksttime[735:744,1] = 2; ksttime[735:744,2] = 1
              


#%% 2019년 2020년 달력
# 0번 열 : 연도
# 1번 열 : 월
# 2번 열 : 일
# 3번 열 : 요일
import numpy as np

c2019 = np.zeros([365,4])
c2020 = np.zeros([366,4])

year = np.array([2019,2020])
month = np.arange(1,13,1)
day1 = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
day2 = np.array([31,29,31,30,31,30,31,31,30,31,30,31])

sum = 0
summ = 0

for ist in np.arange(0,np.size(year,axis=0),1):
    
    if year[ist] == 2019:
        
        for iist in np.arange(0,np.size(month,axis=0),1):
            
            for iiist in np.arange(0,day1[iist],1):
                
                c2019[sum,0] = year[ist]
                c2019[sum,1] = month[iist]
                c2019[sum,2] = iiist+1
                sum = sum+1
    
    elif year[ist] == 2020:
        
        for iist in np.arange(0,np.size(month,axis=0),1):
            
            for iiist in np.arange(0,day2[iist],1):
                
                c2020[summ,0] = year[ist]
                c2020[summ,1] = month[iist]
                c2020[summ,2] = iiist+1
                summ = summ+1

 

cal = np.concatenate((c2019,c2020),axis=0)

call = np.array(cal,dtype='str')
date = np.array(['Tue','Wed','Thu','Fri','Sat','Sun','Mon'])
      
for msh in np.arange(1,105,1):
    
    call[7*msh-7:7*msh,3] = date
    
call[728:731,3] = date[0:3]

       
       
       
       
       
       
       
       
       
       
       
       
       
       
              

              
       

    
 

    
    
    
    
    
