# Modified by Paul Winkler:
# removed a lot of redundant stuff,
# such as multiple identical function definitions;
# replaced most calls to input() with get_number();
# fixed a few typos;
# changed the format of scores from {('foo', 'bar'): 'baz'}
#  to {'foo': {'bar': 'baz'}} because it's flexible, at least as clear,
#  and takes many fewer keystrokes;
# in general, replaced a lot of cut-n-paste duplication with loops.
# There's still more that could be done, but I got sleepy.
# I think the script reads at least as well this way, and
# it's shorter by almost 25%.

print "A General Decision Analysis Program."
print
print "Have You Ever Had to Make Up Your Mind?"
print

import sys

def get_number(prompt, lower=sys.maxint * -1, upper=sys.maxint):
        """ get_number(prompt) -> float

This function prompts for a number.  If the user enters bad input, such as
'cat' or '3l', it will prompt again.
Now checks for upper and lower bounds.
"""
        res = None
        while res is None:
                try:
                        res = float(raw_input(prompt))
			try:
				assert lower <= res <= upper
			except AssertionError:
				print "Value must be between", lower, \
				      "and", upper
				res = None
                except ValueError: pass
		
	
        return res


def get_list(heading, prompt):

        print heading
        print
        print "(enter a blank line to end the list)"
        ret = []
        i = 1
        while 1:
                line = raw_input(prompt % i)
                if not line:
                        break
                ret.append(line)
                i=i+1
        print
        return ret

def get_user_rankings(criteria):
    # Next, get the user to rank his criteria.  I use a system where higher
    # is better, so that an undesirable characteristic can be given a negative
    # weight.
    #
    # {} is a dictionary, it can be indexed by (nearly) any expression,
    # and we will index it with the names of the criteria.

    rankings = {}
    print
    print "Enter relative importance of criteria (higher is more important)"
    print
    for c in criteria:
        rankings[c] = get_number("Criterion %s: " % c)
    return rankings

def get_user_scores(options, criteria):
    # Next, get the user to score each option on all the criteria.
    # Scores are stored as a two-dimensional dictionary, like so:
    # {'option1': {'criteria1': 100, 'criteria2': 10},
    #  'option2': {'criteria1': 50, 'criteria2': 10}
    # }
    scores = {}
    print
    print "Enter score for each option on each criterion"
    print
    for o in options:
        scores[o] = {}
        print
        print "Scores for option %s" % o
        print
        for c in criteria:
            scores[o][c] = get_number("Criterion %s: " % c)
    return scores

def calculate_results(options, scores, rankings):
    # Calculate the resulting score for each option.  This equation
    # is different from Rod Stephen's original program, because I
    # make more important criteria have higher rankings, and even let
    # bad criteria have negative rankings.

    # The "result" dictionary is indexed with the names of the options.
    result = {}
    # Criteria can be found automatically, doesn't need to be
    # passed as an argument.
    criteria = scores[options[0]].keys()
    for o in options:
        value = 0
        for c in criteria:
            # print o, c, rankings[c], scores[o][c]
            value = value + rankings[c] * scores[o][c]
            result[o] = value
    return result

def ranked_list(results):
    # Now, I want to take the dictionary result, and turn it into a ranked list

    results = results.items()        # A list of tuples (key, value)
    results.sort(lambda x, y: -cmp(x[1], y[1]))
                                # Sort the list using the reverse of the
                                # "value" of the entry, so that higher
                                # values come first
    return results


def generic_decision_analyzer(options, criteria):
    pass

def decisionanalysis():
    # This code is placed in the public domain
    print
    print "This is a general decision program, and you can define your choices and criteria."
    print
    print "When prompted, please enter the options or choices that you need to decide amongst."
    print
    print "Then, when prompted, enter the criteria for making this decision."


    # First, ask the user to enter the lists
    options = get_list("Enter your options:", "Option %d: ")
    criteria = get_list("Now, enter your criteria:", "Criterion %d: ")

    print "A program to help you make decisions."
    rankings = get_user_rankings(criteria)
    scores = get_user_scores(options, criteria)
    results = ranked_list(calculate_results(options, scores, rankings))
    print
    print "Results, in order from highest to lowest score"
    print
    print "%5s\t%s" % ("Score", "Option")

    # Take the pairs out of results in order, and print them out
    for option, result in results:
            print "%5s\t%s" % (result, option)


   
# Here's the scores used by the language-choice functions.
language_scores = {"Python": {"ease of learning":100,
                              "ease of use":100,
                              "speed of program execution":10,
                              "quality of available tools":70,
                              "popularity":50,
                              "power & expressiveness":100,
                              "cross platform?":100,
                              "cost":100},
                   "Perl": {"ease of learning":50,
                            "ease of use":60,
                            "speed of program execution":20,
                            "quality of available tools":50,
                            "popularity":85,
                            "power & expressiveness":70,
                            "cross platform?":100,
                            "cost":100},
                   "Ruby": { "ease of learning":50,
                             "ease of use":100,
                             "speed of program execution":20,
                             "quality of available tools":20,
                             "popularity":10,
                             "power & expressiveness":100,
                             "cross platform?":80,
                             "cost":100},
                   "Tcl": {"ease of learning":100,
                           "ease of use":100,
                           "speed of program execution":10,
                           "quality of available tools":50,
                           "popularity":40,
                           "power & expressiveness":10,
                           "cross platform?":100,
                           "cost":100},
                   "JavaScript": {"ease of learning":70,
                                  "ease of use":75,
                                  "speed of program execution":10,
                                  "quality of available tools":50,
                                  "popularity":100,
                                  "power & expressiveness":40,
                                  "cross platform?":50,
                                  "cost":100},
                   "Visual Basic": {"ease of learning":50,
                                    "ease of use":100,
                                    "speed of program execution":20,
                                    "quality of available tools":100,
                                    "popularity":100,
                                    "power & expressiveness":50,
                                    "cross platform?":1,
                                    "cost":1},
                   "Java": {"ease of learning":15,
                            "ease of use":50,
                            "speed of program execution":50,
                            "quality of available tools":100,
                            "popularity":90,
                            "power & expressiveness":100,
                            "cross platform?":100,
                            "cost":100},
                   "C++": {"ease of learning":10,
                           "ease of use":25,
                           "speed of program execution":90,
                           "quality of available tools":90,
                           "popularity":80,
                           "power & expressiveness":100,
                           "cross platform?":90,
                           "cost":100},
                   "C": {"ease of learning":15,
                         "ease of use":20,
                         "speed of program execution":100,
                         "quality of available tools":80,
                         "popularity":80,
                         "power & expressiveness":80,
                         "cross platform?":110,
                         "cost":100},
                   "Lisp": {"ease of learning":40,
                            "ease of use":50,
                            "speed of program execution":80,
                            "quality of available tools":60,
                            "popularity":25,
                            "power & expressiveness":110,
                            "cross platform?":80,
                            "cost":90},
                   "Delphi": {"ease of learning":50,
                              "ease of use":110,
                              "speed of program execution":85,
                              "quality of available tools":100,
                              "popularity":30,
                              "power & expressiveness":100,
                              "cross platform?":80,
                              "cost":10}
                   }



def ProgramLanguageFinal():
    print "This is a program to help give you an idea which programming languages you should consider learning."
    print "While there are any number of languages you might consider, this program considers only 11 of the most popluar ones."
    print
    print "The program will ask you to input a ranking or weighting for a number of criteria that may be of importance"
    print "in choosing your next programming language."

    # First look up the criteria listed in the scores.
    # To do that, we need a language name, which can also
    # be looked up from the scores.
    languages = language_scores.keys()
    some_language = languages[0]
    criteria = language_scores[some_language].keys()
    rankings = get_user_rankings(criteria)
    results = ranked_list(calculate_results(languages, language_scores, rankings))
    # Take the pairs out of results in order, and print them out
    for option, result in results:
            print "%5s\t%s" % (result, option)


def ProgramLanguageScript():
    print
    print "This is a program to help you choose a scripting language."
    print
    print "You will be asked to rank some important criteria as to their relative importance to you."
    print "These criteria are 'ease of learning', 'ease of use', 'speed of program execution'"
    "'quality of available tools', 'popularity', and 'power & expressiveness'"
    print
    print "Please rank each of the criteria with a number from 1 to 100 when prompted."
    print
    print "100 means of highest relative importance, 1 means of least importance."

    # This time we want a subset of languages, so I'm going to specify them.
    options = ["Python", "Perl", "Ruby", "Tcl", "JavaScript", "Visual Basic"]
    criteria = language_scores[options[0]].keys()
    rankings = get_user_rankings(criteria)
    results = ranked_list(calculate_results(options, language_scores, rankings))
    # Take the pairs out of results in order, and print them out
    for option, result in results:
            print "%5s %s" % (result, option)


def Basketball():
    print "This is a program to help you decide which team will win a basketball game"
    print
    print "When prompted, enter a number ranking each team on the prompted team skill"
    print "on a scale from 1 to 100, with 1 being terrible and 100 being the best imaginable"
    print
    team_one = raw_input ("What is the name of team one: ")
    team_two = raw_input ("What is the name of team two: ")
    teams = (team_one, team_two)

    rankings = {"speed":100, "size":66, "jumping_ability":50, "defense":60, "shooting":75, "ballhandling":50, "rebounding":50}
    criteria = rankings.keys()
    scores = {team_one: {},
              team_two: {}}
    for c in criteria:
        for team in (team_one, team_two):
            scores[team][c] = get_number("rank the team %s of %s on a scale of 1 to 100: " % (c, team), 1, 100)

    results = calculate_results(teams, scores, rankings)
    for team in teams:
        print "%s has a power ranking of %d" % (team, results[team])
    # Now, who won?
    ranked_results = ranked_list(results)
    # Compare the scores.
    if ranked_results[0][1] == ranked_results[1][1]:
        print "the two teams are a toss-up!!!"
    else:
        print "%s wins!!" % ranked_results[0][0]

                
def YesNo():                
    print "Program to help you make a Yes or No decision."
    options = ["Yes", "No"]
    criteria = get_list("Enter your criteria ...", "Criterion %d: ")

    rankings = get_user_rankings(criteria)
    scores = get_user_scores(options, criteria )
    print `scores`
    results = ranked_list(calculate_results(options, scores, rankings))
    print
    print "The results are"
    print
    print "%5s %s" % ("Score", "Option")

    for option, result in results:
            print "%5s %s" % (result, option)

    if results[0] > results[1]:
            print "You should decide Yes!!!"

    else:
            print
            print "You should decide No!!!"
            print


###### MAIN LOOP ############
            
while 1:    # loop forever

    print "Please enter the number for the type of decision you wish to analayze:" 
    print "1. General Decision Analysis, you choose the options, criteria, etc."
    print "2. Help in Choosing Programming Language amongst 11 popular languages"
    print  "3. Help in choosing scripting programming language amongst 6 scripting languages"
    print  "4. Which Basketball Team will win the Game???"
    print  "5. Questions with Yes or No type answers"
    choice = get_number("Please type in the number of the type of decision-program you wish to run from above and hit enter:", 1, 5)

    if choice ==1:
        decisionanalysis()
    elif choice ==2: 
        ProgramLanguageFinal()
    elif choice ==3:
        ProgramLanguageScript()
    elif choice ==4:
        Basketball()
    elif choice ==5:
        YesNo()
    elif choice =="quit":
        break    # exit from infinite loop
    else:
        print "Invalid operation"










