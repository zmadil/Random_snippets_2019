gettogether= {'Zain': {'Apples': 3, 'Banana':4,'Paper plates':5},
			   'Ali': {'Juice': 3, 'Banana':3,'Strawberry ':5},
			   'John': {'Mango':4, 'Paper Plates': 7},
			}

def totalthings(guests,things):
	count=0
	for i,j in guests.items():
		count= count+ j.get(things,0)
	return count

print(totalthings(gettogether,'Apples'))
