import grammar as g
import markovify
import string
import random

def markov():

    with open("corpus.txt") as f:
        content = f.read()

    tweet = " "
    a = list(tweet)
    happy = False

    while(not happy):
        if (len(a) > 4 or a[-1] in g.prepositions):
            happy = True
        else:
            model = markovify.NewlineText(content)
            tweet = model.make_short_sentence(140)
            a = list(tweet)


    for char in string.punctuation:
        if(tweet.endswith(char)):
            tweet = tweet[0:-1] + g.punctuation[random.randint(0, 4)]
            break

    return tweet
