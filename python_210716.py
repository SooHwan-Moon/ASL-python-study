import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from netCDF4 import Dataset

path = 'D:/Python study/210716/'

#%% SSW - ASCAT

nc1 = Dataset(path+'2018070100_2018070200_daily-ifremer-L3-MWF-GLO-20180703095911-01.0.nc')

# short wind_speed(time, depth, latitude, longitude)
# time: 1, depth: 1, latitude: 641, longitude: 1440

wlon = nc1.variables['longitude'][:]
wlat = nc1.variables['latitude'][:]
wind = np.squeeze(nc1.variables['wind_speed'][:,:,:,:])
windR = np.array(wind)
windR[windR < -999] = np.nan;

#%% Chl-a

nc2 = Dataset('A20181852018192.L3m_8D_CHL_chlor_a_9km.nc')

# float chlor_a(lat, lon)
clon = nc2.variables['lon'][:]
clat = nc2.variables['lat'][:]
chl = nc2.variables['chlor_a'][:,:]

#%% SST

nc3 = Dataset('AQUA_MODIS.20180701.L3m.DAY.SST.sst.9km.nc')

# short sst(lat, lon)
tlon = nc3.variables['lon'][:]
tlat = nc3.variables['lat'][:]
sst = nc3.variables['sst'][:,:]

#%% MLD

nc4 = Dataset('MLD_20190501.nc')

# float mixed_layer_thickness(time, lat, lon)
mlon = nc4.variables['lon'][:]
mlat = nc4.variables['lat'][:]
mld = np.squeeze(nc4.variables['mixed_layer_thickness'][:,:])

wsR = np.array(windR[440:481,1160:1241])
h1 = plt.pcolormesh(wsR,shading='gouraud')
plt.colorbar(h1)


plt.pcolormesh(wind,shading='gouraud')
plt.pcolormesh(chl,shading='gouraud')
plt.pcolormesh(sst,shading='gouraud')
plt.pcolormesh(mld,shading='gouraud')


#%% ROMS 5개 파일 불러옴
# Temp, Sal, Pressure = 0
# 단순상태방정식 구하기

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from netCDF4 import Dataset

# globals()['앞 이름{}'.format(루프변수)] 변수명을 loop를 통해 설정하고 싶을 때,
# ex) globals()['nc{}'.format(ist)] 
# --> nc1,nc2,nc3,nc4,nc5 순서대로의 변수 생성
#%% 단순히 nc파일 한개씩 불러오는 방법
nc1 = Dataset('landuse_ocean_d03_his_00001.nc')

temp1 = nc1.variables['temp'][:,19,:,:]
sal1 = nc1.variables['salt'][:,19,:,:]

nc2 = Dataset('landuse_ocean_d03_his_00002.nc')

temp2 = nc2.variables['temp'][:,19,:,:]
sal2 = nc2.variables['salt'][:,19,:,:]

nc3 = Dataset('landuse_ocean_d03_his_00003.nc')

temp3 = nc3.variables['temp'][:,19,:,:]
sal3 = nc3.variables['salt'][:,19,:,:]

nc4 = Dataset('landuse_ocean_d03_his_00004.nc')

temp4 = nc4.variables['temp'][:,19,:,:]
sal4 = nc4.variables['salt'][:,19,:,:]

nc5 = Dataset('landuse_ocean_d03_his_00005.nc')

temp5 = nc5.variables['temp'][:,19,:,:]
sal5 = nc5.variables['salt'][:,19,:,:]

temp = np.concatenate((temp1,temp2,temp3,temp4,temp5),axis=0)
sal = np.concatenate((sal1,sal2,sal3,sal4,sal5),axis=0)

rho = 1027 + ( (-0.15*(temp - 10)) + (0.78*(sal - 35)) + 0.0045*0 )

## 단점 : nc파일이 많을 경우, nc 파일 하나하나 타이핑해야 하므로, 코딩이 길어짐.

#%% 미리 배열을 생성한 후 알맞게 정렬하는 방법 - slicing을 위함.

temp = np.zeros([121,143,155])
sal = np.zeros([121,143,155])

for ist in np.arange(1,6,1):
    
    nc = Dataset('landuse_ocean_d03_his_000%2.2i' %(ist) + '.nc')
    
    if ist == 1:
        
        temp[0:25,:,:] = nc.variables['temp'][:,19,:,:]
        sal[0:25,:,:] = nc.variables['salt'][:,19,:,:]
        
    else:
        temp[24*(ist-1)+1:24*(ist-1)+25,:,:] = nc.variables['temp'][:,19,:,:]
        sal[24*(ist-1)+1:24*(ist-1)+25,:,:] = nc.variables['salt'][:,19,:,:]
        
rho = 1027 + ( (-0.15*(temp - 10)) + (0.78*(sal - 35)) + 0.0045*0 )

## 단점 : 시간의 규칙성이 없을 경우, 각각의 nc 파일마다 시간할당이 필요하며, 등차수열을 계산하여야 함.
## elif를 이용하여 nc파일의 시간에 대한 배열 갯수를 파악한 뒤 각각 알맞는 자리에 배치할 필요가 있음.


#%% concatenate를 통한 배열 통합

for ist in np.arange(1,6,1):
    nc = Dataset('landuse_ocean_d03_his_000%2.2i' %(ist) + '.nc')
    
    if ist == 1:
        
        temp = nc.variables['temp'][:,19,:,:]
        sal = nc.variables['salt'][:,19,:,:]
        
    else:
        
        temp_sub = nc.variables['temp'][:,19,:,:]
        sal_sub = nc.variables['salt'][:,19,:,:]
        
        temp = np.concatenate((temp,temp_sub))
        sal = np.concatenate((sal,sal_sub))
        
rho = 1027 + ( (-0.15*(temp - 10)) + (0.78*(sal - 35)) + 0.0045*0 )


#%% 리스트를 통한 배열 통합 (append | extend)
temp = []
sal = []

for ist in np.arange(1,6,1):
    
    nc = Dataset('landuse_ocean_d03_his_000%2.2i' %(ist) + '.nc')
    temp1 = nc.variables['temp'][:,19,:,:]
    sal1 = nc.variables['salt'][:,19,:,:]

    temp.append(temp1)
    sal.append(sal1)
    
tempR = np.concatenate(temp,axis=0)
salR = np.concatenate(sal,axis=0)
# -----------------------------------------------------------------------------
tempt = []
salt = []

for ist in np.arange(1,6,1):
    
    nc = Dataset('landuse_ocean_d03_his_000%2.2i' %(ist) + '.nc')
    temp1 = nc.variables['temp'][:,19,:,:]
    sal1 = nc.variables['salt'][:,19,:,:]

    tempt.extend(temp1)
    salt.extend(sal1)

tempRR = np.array(tempt)
salRR = np.array(salt)


rho = 1027 + ( (-0.15*(tempR - 10)) + (0.78*(salR - 35)) + 0.0045*0 )


    
    
    
    


       
       





