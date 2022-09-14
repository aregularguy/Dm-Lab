# import pandas as pd

# import numpy as np

# dataframe = pd.DataFrame(np.random.randn(5,5) , column = ['2016' , '2017' , '2018' , '2019' , ' 2020' ] )


# # Print the the values of dataframe
# print(dataframe.head())
# # Display the box plot based on the dataframe values
# dataframe.boxplot(grid='false', color='blue',fontsize=10, rot=30 )



import random
# dataset = []
# for i in range(0,25):
#  n = random.randint(1,30)
#  dataset.append(n)
 
# # f = open('data.txt','r+')

# with open('data.txt' , 'w+' ) as f:
#      for items in dataset:
#          f.write('%d\n' %items)
#      print('File Written successfully')
     
# f.close()  

filedata = open("data.txt" , "r+")

l1 = []

for line in filedata.readlines():
    l1.append(int(line))
l1.sort()
print("data got ")
for i in range(25):
      print(l1[i])
filedata.close()         
print('max value from dataset is ' , max(l1))

print('min value from dataset is ' , min(l1))

mid  = len (l1) // 2

res = (l1[mid] + l1[~mid] ) / 2

print("Median of list is : " + str(res))

# print(dataset)