import numpy as np
import pandas as pd

# asos = pd.read_excel('ASOS_summer.xlsx',engine='openpyxl',
#                       usecols=[2,3,4,6,7])
# ## 원본을 numpy로
# msh = asos.to_numpy(dtype='float64')

# ## dataframe 생성
# column = np.array(['Year','Month','day','temp','ws'])
# hsb = pd.DataFrame(data=msh,columns=column)
# ## 엑셀 파일 만들기
# writer = pd.ExcelWriter('python_study.xlsx',engine='openpyxl')
# hsb.to_excel(writer,sheet_name='csb')

# writer.save()

## txt 파일 Dataframe
path = 'D:/Python study/210701/Tidal station/'
tide = pd.read_csv(path+'조위관측소(인천)_201907_KR.txt',header=3,
                   delimiter='\t',usecols=[0,1,2,3])

## 임의로 구
time1 = pd.DataFrame(columns=['YYMMDD','HHMMSS'])
# 이제 만들 열의 제목
time = pd.DataFrame(columns=['Year','Month','Day','Hour','Minute'])

time1['YYMMDD'] = tide.관측시간.str.split(' ').str[0]
time1['HHMMSS'] = tide.관측시간.str.split(' ').str[1]

time['Year'] = time1.YYMMDD.str.split('-').str[0]
time['Month'] = time1.YYMMDD.str.split('-').str[1]
time['Day'] = time1.YYMMDD.str.split('-').str[2]

time['Hour'] = time1.HHMMSS.str.split(':').str[0]
time['Minute'] = time1.HHMMSS.str.split(':').str[1]

timeR = time.to_numpy(dtype='float64')

path = 'D:/Python study/210701/Tidal station/'
tides = pd.read_csv(path+'조위관측소(인천)_201907_KR.txt',header=3,
                   delimiter='\t',usecols=[1,2,3])

tidesR = tides.to_numpy()

ttt = np.squeeze(np.array([tide]))

total = np.concatenate((timeR,tidesR),axis=1)


# variables.apply(pd.to_numeric, error='coerce').fillna(0)
# pandas - concatenate : pd.concat([A,B],axis=0)

#%% 시간별로 sorting 후 엑셀로 저장

hourly_index = np.array(['Year','Month','Day','Hour','Level','temp','salt'])
hourly_index = np.array(['Year','Month','Day','Hour','Minute','Level','temp','salt'])

#(1) - np.arange를 통한 60개씩 불러오기
hourly_total = np.array(total[np.arange(0,np.size(total,axis=0),60),:])

#(2) - np.where를 이용한 00시 데이터 sorting
id = np.where(total[:,4] == 0)
hourly_total = np.array(total[id,:])
hourly_total = np.squeeze(hourly_total)

hourly_total = np.array(hourly_total[:,[0,1,2,3,5,6,7]])
hourly_total = np.delete(hourly_total,4,axis=1)

hourly_data = pd.DataFrame(data = hourly_total,columns = hourly_index)
hourly_data2 = hourly_data.drop('Minute',axis=1)

writer = pd.ExcelWriter(path+'hourly_tide.xlsx',engine='openpyxl')

hourly_data.to_excel(writer,sheet_name='hourly_tide')

writer.save()







