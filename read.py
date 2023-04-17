# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:58:13 2023

@author: shiul
"""

data = []
count = 0 
with open('reviews.txt' , 'r') as f:
    for line in f:
        data.append(line)
        count += 1 
        if count % 1000 == 0 :
            print(len(data))
#print (data[0])      
#print ('-----------------------------')  
#print (data[0])  

#算平均留言長度
sum_len = 0 
for d in data:
        sum_len  += len(d)
print('平均長度' , sum_len/len(data))

#篩選留言長度小於100
new = [] 
for d in data:
        if len(d) < 100:
            new.append(d)
print('一共有' , len(new) , '筆留言長度小於100字')

#篩選有good留言
good = [] 
for d in data:
        if 'good' in d:
            good.append(d)
print('一共有' , len(good) , '筆留言有good')
print(good[0])