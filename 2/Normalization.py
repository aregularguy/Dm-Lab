import random
dataset = []
for i in range(0,25):
 n = random.randint(1,30)
 dataset.append(n)
 
 
 
 
 
# f = open('data.txt','r+')

with open('dataset.txt' , 'w+' ) as f:
     for items in dataset:
         f.write('%d\n' %items)
     print('File Written successfully')
     
f.close() 



 