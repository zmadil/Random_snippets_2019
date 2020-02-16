import random, sys

def tech_func(num):
	
	for i in range(num):
		print('Enter names ')
		people= str(input())
		techs.append(people)

	if num==2:
		floors=['1st and BH', '2nd and 3rd']
	elif num==3:
		floors=['1st and BH', '2nd','3rd']
	elif num == 4:
		floors=['1st', '2nd', '3rd','BH']
	elif num==5:
		print('Select 4 techs. Then ' +random.choice(techs)+ ' can help with BH')
		sys.exit()

	random.shuffle(floors)
	for j in range(len(floors)):
		print ('The tech ' +techs[j]+ ' has the floor ' +floors[j])


techs=[]
floors=[]

print('How many techs are working today?')

x= int(input())
if x > 5:
	sys.exit()
elif x <2:
	sys.exit()

tech_func(x)

