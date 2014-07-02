from random import random

t = 1000000

def elemlow(numlist):
	lowestpos = 0
	for i in range(len(numlist)):
		if numlist[i] < numlist[lowestpos]:
			lowestpos = i
	del numlist[lowestpos]

def elemhigh(numlist):
	highestpos = 0
	for i in range(len(numlist)):
		if numlist[i] > numlist[highestpos]:
			highestpos = i
	del numlist[highestpos]

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

def fivedsix():
	rolls = []
	for i in range(5):
		roll = random()
		roll = roll * 6
		roll = roll + 0.5
		roll = round(roll, 0)
		roll = int(roll)
		rolls.append(roll)
	elemhigh(rolls)
	elemlow(rolls)
	total = sum(rolls)
	return total

def sevendsix():
	rolls = []
	for i in range(7):
		roll = random()
		roll = roll * 6
		roll = roll + 0.5
		roll = round(roll, 0)
		roll = int(roll)
		rolls.append(roll)
	elemhigh(rolls)
	elemhigh(rolls)
	elemlow(rolls)
	elemlow(rolls)
	total = sum(rolls)
	return total

threed6 = {}
fived6 = {}
sevend6 = {}

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
	total = sevendsix()
	if total in sevend6:
		sevend6[total] = sevend6[total] + 1
	else:
		sevend6[total] = 1

per3 = {}
per5 = {}
per7 = {}

for i in range(2, 18):
	per3[i+1] = 0
	per5[i+1] = 0
	per7[i+1] = 0

for k, v in threed6.items():
	per3[k] = (v/t)

for k, v in fived6.items():
	per5[k] = (v/t)

for k, v in sevend6.items():
	per7[k] = (v/t)

print("3d6:",  per3)
print("5d6-low-high:",  per5)
print("7d6-2low-2high:",  per7)

f1 = open('d6differencetestv3.txt', 'w')
f1.write('Roll Type	3d6	5d6-low-high	7d6-2low-2high \n')
for i in range(2, 18):
	word = ''
	word = str(i+1) + '	' + str(per3[i+1]) + '	' + str(per5[i+1]) + '	' + str(per7[i+1]) + '\n'
	f1.write(word)
f1.close