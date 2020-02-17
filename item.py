import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
import random
item = np.zeros((50,), dtype=int)
allTransaction = []
minSupport = 60
minConfident = 40


first = 800
n=0
while(n<800):
    numberOfItem = random.randint(2, 5)
    countInTransaction = 0
    transaction = []
    while(countInTransaction < numberOfItem):
        randNum = random.randint(0,100)
        if randNum < 50: transaction.append(0)
        elif randNum >= 50 and randNum < 80: transaction.append(1)
        else: 
            transaction.append(random.randint(0,49))
        countInTransaction +=1
    allTransaction.append(transaction)
    n+=1
n=0
while(n<200):
    numberOfItem = random.randint(6, 8)
    countInTransaction = 0
    transaction = []
    while(countInTransaction < numberOfItem):
        transaction.append(random.randint(0,49))
        countInTransaction +=1
    allTransaction.append(transaction)
    n+=1



print(allTransaction)


n=0
listItem=[]
while n<50:
    listItem.append(np.zeros((1000,), dtype=int))
    n+=1


n=0
while n<50:
    count=0
    while count<len(allTransaction):
        inTrans=0
        while inTrans<len(allTransaction[count]):

            if n == allTransaction[count][inTrans]:
                listItem[n][count] = 1
            inTrans+=1
        count+=1
    n+=1

n=0
item = np.zeros((50,), dtype=int)
while n<len(listItem):
    count=0
    while count<1000:
        if listItem[n][count]==1:
            
            item[n]+=1
        count+=1
    n+=1
    

print(item)

outerSup = []
n=0

while n<len(item):
    if item[n]<minSupport: outerSup.append(n)
    n+=1


listRemovedFirst = np.delete(np.arange(50), outerSup)
print(listRemovedFirst)

listItemTwo = []
listItemTwoTransaction = []


count1 = 0
for i in listRemovedFirst:
    count2 = count1 + 1
    while count2 < len(listRemovedFirst):
        listItemTwo.append([listRemovedFirst[count1], listRemovedFirst[count2]])
        count2 += 1
    count1 += 1

for i in range(len(listItemTwo)):
    listItemTwoTransaction.append(np.zeros((1000,), dtype=int))

for i in range(len(listItemTwo)):
    j = 0
    for j in range(len(allTransaction)):
        check = [0, 0]
        for k in range(len(allTransaction[j])):
            if allTransaction[j][k] == listItemTwo[i][0]: check[0] = 1
            if allTransaction[j][k] == listItemTwo[i][1]: check[1] = 1
        if check[0] == 1 and check[1] == 1:
            listItemTwoTransaction[i][j] = 1

countListItemTwoTransaction = np.zeros((len(listItemTwoTransaction),), dtype=int)
for i in range(len(countListItemTwoTransaction)):
        for j in range(len(listItemTwoTransaction[i])):
            if listItemTwoTransaction[i][j] == 1: countListItemTwoTransaction[i] = countListItemTwoTransaction[i] + 1
print(countListItemTwoTransaction)
listRemoveSecond = []
for i in range(len(countListItemTwoTransaction)):
    if countListItemTwoTransaction[i] >= minSupport: listRemoveSecond.append(i)
print(listRemoveSecond)
print("confident 0 => 1 = {}%".format(float(countListItemTwoTransaction[0])/(item[0])))
print("confident 1 => 0 = {}%".format(float(countListItemTwoTransaction[0])/(item[1])))