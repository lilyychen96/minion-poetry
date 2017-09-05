# minion-poetry

#### A bot that uses markovify and tweepy to compose and tweet poetry

An experiment in progress

## Requirements:
Built on Python 3.6.2, this bot uses the os, string, random, and time modules. markovify and tweepy can be installed by `pip install tweepy markovify` or with the requirements.txt file.

## Corpus:
The following texts were used to construct the corpus:
- Poems Every Child Should Know by Mary E. Burt: http://www.gutenberg.org/ebooks/16436
- The Waste Land by T.S. Eliot: http://www.gutenberg.org/ebooks/1321
- Prufrock and Other Observations by T. S. Eliot: http://www.gutenberg.org/ebooks/1459
- Songs of Innocence, and Songs of Experience by William Blake: http://www.gutenberg.org/ebooks/1934
- probably something else I'm forgetting, also from gutenberg.org

## Translation dictionaries:
The Minion translator library is derived from Bryce Dorn's minion translator dictionary: https://github.com/brycedorn/miniontranslator/blob/master/js/library.js
A Middle & Early Modern English to Modern English dictionary was also constructed due to the nature of many of the poems featured in the corpus to ease translation into Minionese.
