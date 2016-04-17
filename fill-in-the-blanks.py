# by Juil Yoon
""" Fill in The Blanks Quiz.

Asks the user for difficulty level and number of trys, and displays an approprate quiz. The quiz has numbered blanks, asks the user for their answers for each until the quiz is complete or they make the maximum number of mistakes.

Example:
    Run the following to test a compiled version provided by Udacity::

        $ python tests/fill-in-the-blanks.pyc
"""

quizes = {'easy':
"""The capital city of the United States of America
is ___1___. The current president of the USA is ___2___.
___2___ is best known for being the first ___3___-American
president of the USA. He has also received the
Nobel ___4___ Prize.""",
        'medium':
"""The Theory of General ___1___ was proposed by ___2___ Einstein"""}
answers = {'easy': [['Washington, D.C.', 'Washington, DC', 'Washington DC'],
                    ['Barack Obama', 'Obama'],
                    ['African'],
                    ['Peace']]}

def checkAnswer(list, guess):
    """ Case insensitive check of answer."""

    for a in guess:
        if guess.lower() == a.lower():
            return True
    return False

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
        i, c = 1, chances

        guess = raw_input("What goes in ___%s___: " % i)
        if checkAnswer(a, guess):
            print "Correct! \n"
            print '-' * 20
            print quiz.replace('___1___', guess)
            print '-' * 20
        else:
            print "That is incorrect. Be more prepared next time."

if __name__ == '__main__':
    ## Test functions
    # assert

    # main
    takeQuiz()
