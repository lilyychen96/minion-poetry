import os
import tweepy
import markovify
import string
import random
from time import sleep

from grammar import punctuation, prepositions
from mideng import mideng_lib
from minlib import minion_lib
from keys import key

consumer_key = key['consumer_key']
consumer_secret = key['consumer_secret']
access_token = key['access_token']
access_token_secret = key['access_token_secret']


class TweetBot:
    def __init__(self, corpus):
      self.load_corpus(corpus)

      # Authorize Twitter with Tweepy
      auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
      auth.set_access_token(access_token, access_token_secret)
      self.api = tweepy.API(auth)


    def load_corpus(self, corpus):
        with open(corpus) as corpus_file:
            corpus_lines = corpus_file.read()
        self.model = markovify.NewlineText(corpus_lines)


    def tweet(self):
        message = self.model.make_short_sentence(140)
        words = message.split()

        # get rid of pesky prepositions at the end of tweet
        while(words[-1] in prepositions):
            message = self.model.make_short_sentence(140)
            words = message.split()
            message = " ".join(words)

        message = translate(message)

        # check for or add punctuation
        for char in string.punctuation:
            while(message.endswith(char)):
                message = message[0:-1]

        message = message.strip() + punctuation[random.randint(0, 4)]

        try:
            print(message + "\n")
            self.api.update_status(message)
        except tweepy.TweepError as error:
            print(error.reason)


    def automate(self, delay):
        self.tweet()
        sleep(delay)


def translate(message):
    print(message)
    # translate from Middle English to Modern English, if applicable
    old = message.split()
    modern = list()
    for word in old:
      if(word in mideng_lib): modern.append(mideng_lib[word])
      else: modern.append(word)

    # Throw back into string in case a translation results in >1 separate words
    temp = " ".join(modern)

    # translate to Minionese
    modern = temp.split()
    new = list()
    for word in modern:
      if(word in minion_lib): new.append(minion_lib[word])
      else: new.append(word)

    # translation is now incoherent!
    return " ".join(new)


def main():
    while(True):
      bot = TweetBot("corpus.txt")
      bot.automate(2700)


if __name__ == "__main__":
    main()
