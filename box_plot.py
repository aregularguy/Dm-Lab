# import random
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
l2 = []
for i in range(6):
    l2.append(l1[i])
    
    
mid1 = len(l2) // 2
res1 =  (l2[mid1] + l2[~mid1])  / 2  
print('Lower  quartile is ', res1)

l3 = [ ]
for i in range(18):
  l3.append(l1[i])
mid2 = len(l3) //2  
res2 = (l3[mid2] + l3[~mid2]) /2
print('The Upper Quartile of data is ' , res2)


first_quartile = res1
third_quartile = res2
inter_quartile =   third_quartile - first_quartile

print('The Inter Quartile Range is ', inter_quartile)





# print(dataset)