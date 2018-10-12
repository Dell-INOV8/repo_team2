#python for forums
import sys 
#creation of file 
forums = []
forum = "forum.txt"
i = -1
#opens file
file = open(forum, "r")

#TODO: Function for parsing file 
#loops through file
for line in file:
	#cleans up line
	line = line.strip()
	#grabs whether it is a question or answer
	type = line[0]
	
	#if at a question 
	if type == 'Q': 
		#array for q's answers
		lines = []
		#add question to its list
		lines.append(line)
		#add question list to the main list
		forums.append(lines)
		i+=1
	#else it's an answer
	elif type == 'A':
		forums[i].append(line)
	
		
#TODO: make into function
#prints forum			
for thread in forums:
	for subthread in thread:
		print(subthread, end= '\n')
	
#TODO: Make action function and edit file 			
#Make a change?
takeAction = input("Would you like to make a change?(y/n):")
#Yes, make change
if takeAction == 'y':
	action =  input("What action would you like to do? 1 for Append or 2 for Delete:")
	
	#If you want to append 
	if action == "1":
		typeAction =  input("Would you like to add a questin or answer?(q/a): ")
		#if append question 
		if typeAction == "q":
			question = input("What's your question? Hit enter when done.: ")
			qList = []
			question = "Q" + str(len(forums)+1) + ": " + question
			qList.append(question)
			forums.append(qList)
		elif typeAction == "a":
			question = input("Which question would you like to change?Enter integer of question.(ex: Q1 would be 1): ")
			answer = input("Which answer would you like to change?Enter integer of answer.(ex: A1 would be 1): ")

			#TODO: Search function in question list
	#If you want to Delete 		
	elif action == "2":
		typeAction =  input("Would you like to delete a questin or answer?(q/a): ")
		#if delete question
		if typeAction == "q":
			print("Delete question!")
		#if delete answer
		if typeAction == "a":
			print("Deleted!")
	else:
		print("Not a valid action")
		exit(1)

for thread in forums:
	for subthread in thread:
		print(subthread, end= '\n')

file.close()
