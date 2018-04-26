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
blank_spaces = ["__1__","__2__", "__3__"]

easy ="The __1__ model is often __2__ around the business world, evoking complicated and intimidating visual __3__ to those unfamiliar with them."

medium = "A hobby is a __1__ activity that is __2__ for enjoyment, typically __3__ one's leisure time."

hard ="Hobbies can __1__ collecting themed items and objects, engaging in __2__ and artistic pursuits, playing sports, or __3__ other amusements."


game_level_options = {
						"easy" : easy,
						"medium" : medium,
						"hard" : hard
					}


easy_answers = ["word", "tossed", "images"]
medium_answers = ["regular", "done", "during"],
hard_answers = ["include", "creative", "pursuing"]	


def welcome_user():
	name = raw_input("What's your name?: ")
	if name == "":
		print "Kindly fill name in your name."
		welcome_user()
	else:
		print "Hello " + name+ "!, welcome to fill-in-the-blanks game."
		print "This is aimed at testing how well you understand your business lessons.\nSelect a game level by choosing an option, which includes:\n\neasy, medium and hard.\n"
		


def ask_game_level():
	game_option =raw_input("Choose an option: ")
	game_option = game_option.lower()
	if game_option in game_level_options:
		print "you have chosen the" + " "+ game_option + " option"
		print "You will get 5 guesses per problem.\n The paragraph reads as such:"
		print "-"*80
		print game_level_options[game_option]
		return game_option
	while game_option not in game_level_options:
		print "That's not an option!\nPlease select a game difficulty by choosing one!\n(easy, medium, and hard)."
		ask_game_level()


def question_answer(question):
	if question == easy:
		answer = easy_answers
		return answer
	if question == medium:
		answer = medium_answers
		return answer
	if question == hard:
		answer = hard_answers
		return answer

# answer_to_question =question_answer(test_sample)
 
def check_answer(response, blank, question):
	
	position = blank_spaces.index(blank)
	# print str(position) + "This is it :"
	# print question
	# answers = question_answer(question)
	
	answer = answer_to_question[position]
	# print "answer answer ", answer
	if response == answer:
		return True
	return None

def begin_game(test_sample, blank):    
	replaced = []
	statement = test_sample.split()
	
	for word in statement:
		if blank == word:
			
		# replacement = word_in_blankspace(word, blank)
		# if replacement != None:
			user_input = raw_input("What should be substituted in for " + blank + "?: ").lower()
			response = check_answer(user_input, blank, test_sample)
			
			if response != None:
				print "Correct, you are right"
				word = word.replace(blank, user_input)
				replaced.append(word)
			while response == None:
				print "Wrong answer, try again"
				begin_game(test_sample, blank)
				break
				print response, "third response"
				# user_input = raw_input("What should be substituted in for " + blank + "?: ")
				
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	return replaced


def word_in_blankspace(blank_space,test_sample):
	for blank in blank_space:
		test_sample =begin_game(test_sample, blank)
		print test_sample
		# return result
        # if blank in word:
        #     return blank
    # return None


       
# Plays a full game of mad_libs. A player is prompted to replace words in ml_string, 
# which appear in parts_of_speech with their own words.  

    
 


# game_level_and_answers = {
# 	"easy":[first_sample,["word", "tossed", "images"]],
# 	"medium":[second_sample,["regular", "done", "during"]],
# 	"hard":[third_sample,["include", "creative", "pursuing"]]

# }

# def chosen_game(game):
# 	for key in enumerate(game_level_and_answers):
# 		if key == game_option:
# 			note =game_level_and_answers[key][0]
# 			print note
# 		if game_option not in game_level_and_answers:
# 			print "That's not an option"
# 			game_option =raw_input("Choose an option: ")

welcome_user()
answer =ask_game_level()

print "-"*80
test_sample =game_level_options[answer]
answer_to_question =question_answer(test_sample)
print word_in_blankspace(blank_spaces, test_sample) 
print "-"*80
print "Congratulations, you won"
# chosen_game(game_option)

# for blank in blank_spaces:
# 	if blank in first_sample:
# 		print blank


'''
SECOND SOLUTION

name = raw_input("What's your name?: ")
welcome= "Hello " + name+ "!, welcome to fill-in-the-blanks game."

instruction ="This is aimed at testing how well you understand your business lessons. Fill the 5 blank spaces with the correct word. Choose the number of turns to be repeated when you get an answer wrong."

turn = int(raw_input("number of turns(choose a number)?: "))

answers =["model", "financial modeling", "predicting", "meteorologist", "assumptions"]




sample ="The word " + '__1__'+ " is often tossed around the business world, evoking complicated and intimidating visual images to those unfamiliar with them. But instead of depending on your friend with an MBA to back you up, any business owner can and should know the basics of " +'__2__' + ". So what is a financial model exactly?A model is a means of " +'__3__' +" the future, and like a " +'__4__'+ " forecasting rain, a financial model is really just a volatile \"best guess\" that should be updated frequently.  Models take a set of " + '__5__'+ " (and sometimes your business's performance history) and forecast a future state. Even though they are predictions, models provide a good benchmark and can help run \"what-if\" scenarios so you are prepared for any situation."


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


#Helper functions
def ask_question(question):
	"""Takes in a question, outputs the question using the raw_input function and 
	returns the answer
	"""
	answer = raw_input(question)
	return answer


def check_answer(answer):
	"""Checks if an answer is correct by taking in a paramenter answer,
	checking in the list answers and returning True or False
	"""
	if answer in answers:
		return True
	return False


def replace_answer(note,question,answer):
	"""
	Replaces a word, question in the sentence or paragraph, note with the word answer
	and then outputs the rewritten sentence or paragraph
	"""
	note = note.replace(question,answer)
	return note

def wrong_answer(answer, question):
	"""
	checks if an answer is wrong, if wrong, repeats it till the answer is correct
	"""
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
	"""
	From list of questions, takes a question, accepts response, checks if the 
	response is correct. If correct, proceeds to other questions. If not correct,
	ask you number of times(turn) for right answer to be outputed.
	"""
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
print "credit for resource for quize: https://www.paro.io/blog/how-to-build-a-basic-financial-model"
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
# 	print 'What is your name?  It is {__1__}.'.format(a)


'''

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