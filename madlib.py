# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string.

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# # Built-in function word.replace(original, replacement) already exists
# def replace(pos, string, word):
#     p = string.find(pos)
#     return string[0:p] + word + string[p+len(pos):]

def play_game(ml_string, parts_of_speech):
    replaced = []
    # your code here
    for word in ml_string.split():
        pos = word_in_pos(word, parts_of_speech)
        if not pos:
            replaced.append(word)
        else:
            userInput = raw_input("Give me a " + pos + ":")
            replaced.append(word.replace(pos, userInput))

    return " ".join(replaced)

if __name__ == '__main__':
    import random

    parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN",
                        "NOUN", "VERB", "ADJECTIVE"]

    mad_libs = ["Straight outta PLACE, crazy NOUN named PERSON,                from the gang called PLURALNOUN Wit Attitude",
                "VERB when you can, VERB when you have to, be who you must, that's a part of the NOUN.",
                "I want PERSON to lead me, take me somewhere... Don't want to VERB in a PLACE one more day.",
                "It makes me ADJECTIVE to know my NOUN will be represented by the PLACE we're in now."]

    print play_game(mad_libs[random.randint(0, len(mad_libs)-1)], parts_of_speech)
