#IPND STAGE 2 FINAL
#MADLIBS GENERATOR

#"credit for resource for sample: https://www.codeconquest.com/what-is-coding/how-does-coding-work/"
"""
steps to solving the problem
Step 1:
welcome, greet and introduce

Step 2:
Ask them to choose a question(game option) and fill in the blanks

Step 3:
ask a question and save the answer in a variable

Step 4:
i. check the answer.
ii. if the answer is right replace the blank space with the variable.

Step 5:
check if the answer is wrong repeat the question and repeat number 4.

step 6:
Move on to next question.

"""
blank_spaces = ["__1__","__2__", "__3__", "__4__", "__5__"]

easy ="So how does __1__ work, really? The short answer is that __2__ code __3__ the __4__ what to do, but it's not __5__ that simple."

medium = "So here's the longer answer. A __1__ can only understand two __2__ types of data: on and off. In fact, a computer is really just a __3__ of on/off switches (transistors). Anything that a computer can do is nothing more than a __4__ combination of some __5__ turned on and some transistors turned off."

hard ="Binary code is the __1__ of these combinations as 1s and 0s, where each __2__ represents one __3__. Binary code is grouped into bytes, groups of 8 digits representing 8 transistors. For example, 11101001. Modern __4__ contain millions or even billions of transistors, which means an __5__ large number of combinations."


game_level_options = {
						"easy" : easy,
						"medium" : medium,
						"hard" : hard
					}


easy_answers = ["coding", "writing", "tells", "computer", "quite"]
medium_answers =["computer", "distinct", "combination", "unique", "transistors"]
hard_answers = ["representation", "digit", "transistor", "computers", "unimaginably"]	

#auxilliary functions

def welcome_user():
	"""input : Empty

	Behaviour: Accepts input for the username and  asks again when n user name is given

	output: Print out a welcome statement for the user and tells user to select a level. 
	"""
	name = raw_input("What's your name?: ")
	if name == "":
		print "Kindly fill name in your name."
		welcome_user()
	else:
		print "Hello " + name+ "!, welcome to fill-in-the-blanks game."
		print "This is aimed at testing how well you understand how coding works.\nSelect a game level by choosing an option, which includes:\n\neasy, medium and hard.\n"
		


def ask_game_level():
	"""Input : Empty

	Behaviour : Prompts user to choose a game level(game option) and checks if the game level is right

	Output : Returns the level  chosen by user.
	"""
	game_option =raw_input("Choose an option: ").lower()
	print game_option, "why this?"
	if game_option in game_level_options:
		print "you have chosen the" + " "+ game_option + " option"
		print "You will get 5 guesses per problem.\nThe paragraph reads as such:"
		print "-"*80
		# print game_level_options[game_option]
		print game_option, "why is it none"
		return game_option
	# while game_option not in game_level_options:
	else:
		print game_option, "whats happening?"
		print "That's not an option!\nPlease select a game difficulty by choosing one!\n(easy, medium, and hard)."
		game_option = ask_game_level()
		print game_option, "let me check"
		return game_option






def question_answer(question):
	"""Input : question(str) or game option selected by the user

	Behaviour: checks the corresponding answer to the question

	Output: Returns corresponding answer for the question selected(game option)
	"""
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
	"""Input: response(str) obtained from user as user_input, blank(str), question(str)

	Behaviour: Checks the validity of an answer

	Output: Returns True if answer is valid or None if not valid
	"""
	position = blank_spaces.index(blank)
	answer = answer_to_question[position]
	if response == answer:
		return True
	return None

def begin_game(test_sample, blank):
	"""Input: test_sample(str)/game option chosen by user and a blank(str) from blank_spaces

	Behaviour: splits the test_sample into a list and checks if it is a blank.
	Accepts user_input and checks if it is right.
	Then replaces the blank in the test_sample with user input if right

	Output: Returns replaced(str) with a blank replaced."""    
	replaced = []
	statement = test_sample.split()
	
	for word in statement:
		if blank == word:
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
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	# print replaced,"\n", "take this out?"
	return replaced



def word_in_blankspace(blank_space,test_sample):
	"""Input: blank_space, test_sample

	Behaviour: A blank from blank_spaces is taken and the function begin_game called on it.

	Output : Return test_sample 
	"""
	for blank in blank_space:
		test_sample =begin_game(test_sample, blank)
		print test_sample
	return test_sample



 
#Plays the madlib game

welcome_user()
answer =ask_game_level()
print answer, "this is none******************"

print "-"*80
test_sample =game_level_options[answer]
print test_sample, "*******************"
answer_to_question =question_answer(test_sample)
word_in_blankspace(blank_spaces, test_sample) 
print "-"*80
print "Congratulations, you won"
