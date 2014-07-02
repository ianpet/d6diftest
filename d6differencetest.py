from random import random

t = 1000000

def elemlow(numlist):
	lowestpos = 0
	for i in range(len(numlist)):
		if numlist[i] < numlist[lowestpos]:
			lowestpos = i
	del numlist[lowestpos]
def threedsix():
	rolls = []
	for i in range(3):
		roll = random()
		roll = roll * 6
		roll = roll + 0.5
		roll = round(roll, 0)
		roll = int(roll)
		rolls.append(roll)
	total = sum(rolls)
	return total
def fourdsix():
	rolls = []
	for i in range(4):
		roll = random()
		roll = roll * 6
		roll = roll + 0.5
		roll = round(roll, 0)
		roll = int(roll)
		rolls.append(roll)
	elemlow(rolls)
	total = sum(rolls)
	return total
def fivedsix():
	rolls = []
	for i in range(5):
		roll = random()
		roll = roll * 6
		roll = roll + 0.5
		roll = round(roll, 0)
		roll = int(roll)
		rolls.append(roll)
	elemlow(rolls)
	elemlow(rolls)
	total = sum(rolls)
	return total
def sixdsix():
	rolls = []
	for i in range(6):
		roll = random()
		roll = roll * 6
		roll = roll + 0.5
		roll = round(roll, 0)
		roll = int(roll)
		rolls.append(roll)
	elemlow(rolls)
	elemlow(rolls)
	elemlow(rolls)
	total = sum(rolls)
	return total

fourd6 = {}
threed6 = {}
fived6 = {}
sixd6 = {}
for i in range(t):
	total = fourdsix()
	if total in fourd6:
		fourd6[total] = fourd6[total] + 1
	else:
		fourd6[total] = 1

for i in range(t):
	total = threedsix()
	if total in threed6:
		threed6[total] = threed6[total] + 1
	else:
		threed6[total] = 1

for i in range(t):
	total = fivedsix()
	if total in fived6:
		fived6[total] = fived6[total] + 1
	else:
		fived6[total] = 1

for i in range(t):
	total = sixdsix()
	if total in sixd6:
		sixd6[total] = sixd6[total] + 1
	else:
		sixd6[total] = 1
per3 = {}
per4 = {}
per5 = {}
per6 = {}

for i in range(2, 18):
	per3[i+1] = 0
	per4[i+1] = 0
	per5[i+1] = 0
	per6[i+1] = 0
for key, value in threed6.items():
	per3[key] = (value/t)
for k, v in fourd6.items():
	per4[k] = (v/t)	
for k, v in fived6.items():
	per5[k] = (v/t)
for k, v in sixd6.items():
	per6[k] = (v/t)	
print('3d6:', per3)
print('4d6 minus lowest:', per4)
print('5d6 minus 2 lowest:', per5)
print('6d6 minus 3 lowest:', per6)
f1 = open('d6differencetest.txt', 'w')
f1.write('Roll Type	3d6	4d6-low	5d6-2low	6d6-3low \n')
for i in range(2, 18):
	word = ''
	word = str(i+1) + '	' + str(per3[i+1]) + '	' + str(per4[i+1]) + '	' + str(per5[i+1]) + '	' + str(per6[i+1]) + '\n'
	f1.write(word)
f1.close