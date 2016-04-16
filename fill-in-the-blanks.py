# by Juil Yoon
""" Fill in The Blanks Quiz.

Asks the user for difficulty level and number of trys, and displays an approprate quiz. The quiz has numbered blanks, asks the user for their answers for each until the quiz is complete or they make the maximum number of mistakes.

Example:
    Run the following to test a compiled version provided by Udacity::

        $ python tests/fill-in-the-blanks.pyc
"""

quizes = {'easy': """Hello ___1___"""}
answers = {'easy': ['world']}

def takeQuiz():
    """ Shows the quiz and asks the user for answers."""
    print "Welcome to the quiz."
    print "What difficulty would you like?"
    difficulty = raw_input("Enter easy, medium, or hard:  ")
    quiz = quizes[difficulty]

    print "This quiz will be " + difficulty + "."
    print ""

    chances = raw_input("How many chances would you like per question?")
    print ""

    print "Let's get started:"
    print "=" * 20
    print quiz
    print "=" * 20 + '\n'

    for a in answers[difficulty]:
        c = chances

        guess = raw_input("What goes in ___1___: ")
        if guess == a:
            print "Correct!"
            print quiz.replace('___1___', a)
        else:
            print "That is incorrect. Be more prepared next time."

if __name__ == '__main__':
    ## Test functions
    # assert

    # main
    takeQuiz()
