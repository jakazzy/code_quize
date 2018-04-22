#IPND STAGE 2 FINAL
#MADLIBS GENERATOR
#sample='The word model is often tossed around the business world, evoking complicated and intimidating visual images to those unfamiliar with them. But instead of depending on your friend with an MBA to back you up, any business owner can and should know the basics of financial modeling.So what is a financial model exactly?A model is a means of predicting the future, and like a meteorologist forecasting rain, a financial model is really just a volatile "best guess" that should be updated frequently.  Models take a set of assumptions (and sometimes your business\'s performance history) and forecast a future state. Even though they are predictions, models provide a good benchmark and can help run "what-if" scenarios so you are prepared for any situation.
#"credit for resource: https://www.paro.io/blog/how-to-build-a-basic-financial-model"

"""
steps to solving the problem
Step 1:
welcome, greet and introduce(advance offer options)

Step 2:
Tell them the number of inputs to be filled and allow them to choose the number of times they can answer 
before game over

Step 3:
ask a question and save the question in a variable

Step 4:
i. check the answer.
ii. if the answer is right replace the blank space with the variable.

Step 5:
check if the answer is wrong repeat the question and repeat number 4.

step 6:
Move on to next question.

PSEUDOCODE
def ask_question:
	ask a question and save the question in a variable
	return question

def check_answer(answer):
	check the answer.
	return ...

if check_answer(answer):
	string.replace(word, answer)

if not check_answer(answer):
	check if the answer is wrong repeat the question and repeat number 4.



"""
name = raw_input("What's your name?: ")
welcome= "Hello " + name+ "!, welcome to fill-in-the-blanks game."

instruction ="This is aimed at testing how well you understand your business lessons. Fill the 5 blank spaces with the correct word. Choose the number of turns to be repeated when you get an answer wrong."

turn = int(raw_input("number of turns?: "))

answers =["model", "financial modeling", "predicting", "meteorologist", "assumptions"]




sample ="The word " + '__1__'+ " is often tossed around the business world, evoking complicated and intimidating visual images to those unfamiliar with them. But instead of depending on your friend with an MBA to back you up, any business owner can and should know the basics of " +'__2__' + ". So what is a financial model exactly?A model is a means of " +'__3__' +" the future, and like a " +'__4__'+ " forecasting rain, a financial model is really just a volatile \"best guess\" that should be updated frequently.  Models take a set of " + '__5__'+ " (and sometimes your business's performance history) and forecast a future state. Even though they are predictions, models provide a good benchmark and can help run \"what-if\" scenarios so you are prepared for any situation."
questions ={
	"question1":["__1__","model"],
	"question2":["__2__","financial modeling"],
	"question3":["__3__","predicting"],
	"question4":["__4__","meteorologist"],
	"question5":["__5__","assumptions"],

}

question1= "What should be substituted for __1__?: "
question2= "What should be substituted for __2__?: "
question3= "What should be substituted for __3__?: "
question4= "What should be substituted for __4__?: "
question5= "What should be substituted for __5__?: "

question_list = [question1, question2, question3, question4,question5]
blank_spaces = {
	"model": "__1__" ,
	"financial modeling":"__2__",
	"predicting": "__3__", 
	"meteorologist": "__4__" ,
	"assumptions": "__5__" ,

}

blank_space = ["__1__", "__2__","__3__","__4__","__5__"]
word1 = "__1__"
word2 = "__2__"
word3 = "__3__"
word4 = "__4__"
word5 = "__5__"


def ask_question(question):
	answer = raw_input(question)
	return answer

def check_answer(answer):
	if answer in answers:
		return True
	return False


def replace_answer(note,question,answer):
	note = note.replace(question,answer)
	return note

def wrong_answer(answer, question):
	if answer not in answers:
		print "sorry wrong answer"
		for i in range(turn):
			reply = raw_input(question)
			check =check_answer(reply)
			if check:
				print "well done"
				break
			else:
				print "Try again"
		if i + 1 == turn:
			print "sorry you have lost the game"

"--------------------------------------------------------------------------------------------------------"
print "-"*80
print welcome, "\n", instruction, "\n\n", sample

def ask_and_answer(list_questions):
	note = sample
	for question in list_questions:
		response = ask_question(question)
		output = check_answer(response)
		if output:
			print "correct"
			word =blank_spaces[response]
			note =replace_answer(note,word,response)
			print note
		elif not output:
			wrong_answer(response, question)
			break	
			


ask_and_answer(question_list)
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
# 	print 'What is your name?  It is {__1__}.'.format(a)

'''
SOLUTION 1
Title = "You have five guesses"
sample = 'The word ___1___ is often tossed around the business world, evoking complicated and intimidating visual images to those unfamiliar with them. But instead of depending on your friend with an MBA to back you up, any business owner can and should know the basics of ___2___. So what is a financial model exactly?A model is a means of __3__ the future, and like a __4__ forecasting rain, a financial model is really just a volatile "best guess" that should be updated frequently.  Models take a set of __5__ (and sometimes your business\'s performance history) and forecast a future state. Even though they are predictions, models provide a good benchmark and can help run "what-if" scenarios so you are prepared for any situation.'

print Title,'\n', sample, '\n'



answers =["model", "financial modeling", "predicting", "meteorologist", "assumptions"]

def check_result(answer):
	if answer in answers:
		print "correct answer"
	elif answer not in answers or  answer == "": 
		print "wrong answer! try again"
		for turn in range(3):
			answer=raw_input("Try another answer again: ")
			if answer in answers:
				print "Whew! you are right" 
				break
			else:
				print "No try again"
		if turn + 1 == 3:
			print "sorry you have lost the game"
			


question1= "What should be substituted for ___1___?: "
question2= "What should be substituted for ___2___?: "
question3= "What should be substituted for ___3___?: "
question4= "What should be substituted for ___4___?: "
question5= "What should be substituted for ___5___?: "

questions = [question1, question2, question3, question4,question5]

		
def lost_previous_question():
	for question in questions:
		question = raw_input(question)
		check_result(question)
		
		break
		if check_result != "sorry you have lost the game":
			print "You won"
	
lost_previous_question()
'''
"""elif answer not in answers or  answer == "": 
		print "wrong answer! try again"
		for turn in range(3):
			question=raw_input("Try another answer again: ")
			if question in answers:
				print "Whew! you are right"
				break
			else:
				print "No try again"
		if turn + 1 == 3:
			print "sorry you have lost the game"""