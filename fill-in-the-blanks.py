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
    """ Shows the quiz and asks the user for answers.

    Returns ``True`` if the user completes the quiz, ``False`` if they
    use too many guesses"""

    alive = True

    print "Welcome to the quiz."
    print "What difficulty would you like?"
    difficulty = raw_input("Enter easy, medium, or hard:  ")
    while difficulty not in quizes:
        difficulty = raw_input("Please enter one of the options [easy, medium, hard]: ")
    quiz = quizes[difficulty]

    print "This quiz will be " + difficulty + "."
    print ""

    chances = raw_input("How many chances would you like per question:  ")
    while not chances.isdigit(): or int(chances) < 1
        chances = raw_input("Please enter a number that is greater than 0:  ")
    print ""

    print "Let's get started:"
    print "=" * 20
    print quiz
    print "=" * 20 + '\n'

    for a in answers[difficulty]:
        i, c = 1, chances

        while c > 0:
            guess = raw_input("What goes in ___%s___: " % i)
            if checkAnswer(a, guess):
                print "Correct! \n"
                print '-' * 20
                print quiz.replace('___%s___' % i, a[0])
                print '-' * 20 + '\n'

                i += 1 #Next question
                break
            elif c > 1:
                print "That is incorrect. Try again.\n"
                c += -1
            else:
                alive = False
                break

    if alive:
        print "Great job completing the %s quiz!" % difficulty
    else:
        print "Too many wrong guesses. Game over."

    return alive

if __name__ == '__main__':
    ## Test functions
    assert checkAnswer(a['easy'][0], 'washington dc') == True

    # main
    takeQuiz()
