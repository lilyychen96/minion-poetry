import os
import tweepy
import markovify
import string
import random
import grammar as g
from time import sleep

if(os.environ.get('IS_HEROKU', None)):
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
else:
    import settings
    consumer_key = settings.consumer_key
    consumer_secret = settings.consumer_secret
    access_token = settings.access_token
    access_token_secret = settings.access_token_secret

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

        words = list(message)
        while(words[-1] in g.prepositions):
            message = self.model.make_short_sentence(140)
            words = list(message)

        for char in string.punctuation:
            if(message.endswith(char)):
                message = message[0:-1] + g.punctuation[random.randint(0, 4)]
                break

        try:
             print(message)
             self.api.update_status(message)
        except tweepy.TweepError as error:
            print(error.reason)


    def automate(self, delay):
        self.tweet()
        # sleep(delay)


def main():
    bot = TweetBot("corpus.txt")
    bot.automate(300)

if __name__ == "__main__":
    main()
