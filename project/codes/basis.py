import random,sys,os,math

for i  in range(5):
	print(random.randint(1,10))

print("hello world!")
# sys.exit();
# myName = input()
#print('it is good to meet you,' + str(myName))

def getsNumber(n):
	if n == 1:
		return 'one'
	elif n == 2:
		return 'two'
	elif n == 3:
		return "three"	
	elif n == 4:
		return "four" 
	elif n == 5:
		return "five"	

def getAnswer(answerNumber): 
	if answerNumber == 1:
		return 'It is certain' 
	elif answerNumber == 2:
		return 'It is decidedly so' 
	elif answerNumber == 3:
           return 'Yes'
   	# elif answerNumber == 4:
   	# 	return 'reply hazy try again'
   	# elif answerNumber == 5:
   	# 	return 'Ask again later'	
   	# elif answerNumber == 6:
   	# 	return 'Concentrate and ask again' 
   	# elif answerNumber == 7:
   	# 	return 'My reply is no'
   	# elif answerNumber == 8:
   	# 	return 'Outlook not so good'
   	# elif answerNumber == 9:
   	# 	return 'Very doubtful'

r =random.randint(1, 4)
fortune = getsNumber(r) 
print(fortune)

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

print('Hello', end='')
print("world")
print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep =',')