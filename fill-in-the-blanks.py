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
"""The Theory of General ___1___ was proposed by ___2___ Einstein
in 1915. It provides a unified description of ___3___ as a property
of ___4___ and ___5___, also known as ___6___, and is the current
definition of ___3___ in modern physics.""",
        'hard':
"""Spirited ___1___ is the ___2___ Award winning film by ___3___ Miyazaki
and Studio ___4___. It won Best ___5___ ___6___ Film and the
Golden ___7___ at the 2002 ___8___ International Film Festival
(among many others). It was adapted by ___9___ for the English speaking
audience."""}
answers = {'easy': [['Washington, D.C.', 'Washington, DC', 'Washington DC'],
                    ['Barack Obama', 'Obama'],
                    ['African'],
                    ['Peace']],
            'medium': [['Relativity'],
                    ['Albert'],
                    ['gravity', 'gravitation'],
                    ['space'],
                    ['time'],
                    ['spacetime', 'space time']],
            'hard': [['Away'],
                    ['Academy', 'Oscar'],
                    ['Hayao'],
                    ['Ghibli'],
                    ['Animated'],
                    ['Feature'],
                    ['Bear'],
                    ['Berlin'],
                    ['Walt Disney Pictures', 'Disney']]}

def checkAnswer(possible, guess):
    """ Case insensitive check of answer.

    Args:
        possible (list): List of possible answers for question.
        guess (string): User's guess for question.

    Returns:
        bool: True if guess is in possible, False otherwise.
    """
    for a in possible:
        if guess.lower() == a.lower():
            return True
    return False

def takeQuiz():
    """ Shows the quiz and asks the user for answers.

    Returns:
        bool: True if the user completes the quiz, ``False`` if they use too many guesses
    """
    alive = True

    print '\n' + "* " * 10
    print "Welcome to the quiz.\n"
    print "What difficulty would you like?"
    difficulty = raw_input("Enter easy, medium, or hard:  ")
    while difficulty not in quizes:
        difficulty = raw_input("Please enter one of the options [easy, medium, hard]: ")
    quiz = quizes[difficulty]

    print "This quiz will be " + difficulty + " difficulty."
    print ""

    chances = raw_input("How many chances would you like per question:  ")
    while not chances.isdigit() or int(chances) < 1:
        chances = raw_input("Please enter a number that is greater than 0:  ")
    chances = int(chances)
    print ""

    print "Let's get started:"
    print "=" * 20
    print quiz
    print "=" * 20 + '\n'

    for i in xrange(len(answers[difficulty])):
        c = chances
        a = answers[difficulty][i]

        while c > 0:
            guess = raw_input("What goes in ___%s___: " % str(i+1))
            if checkAnswer(a, guess):
                print "Correct! \n"
                print '-' * 20
                quiz = quiz.replace('___%s___' % str(i+1), guess)
                print quiz
                print '-' * 20 + '\n'
                break
            elif c > 1:
                print "That is incorrect. Try again."
                c += -1
                print c, "chance(s) left. \n"
            else:
                alive = False
                break
        if not alive: break

    if alive:
        print "Great job completing the %s quiz!\n" % difficulty
    else:
        print "Too many wrong guesses. Game over.\n"

    return alive

if __name__ == '__main__':
    ## Test functions
    assert checkAnswer(answers['easy'][0], 'washington dc')

    # main
    takeQuiz()
