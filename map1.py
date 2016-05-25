#!/usr/bin/env python
import sys
import json
import string

Ono_char_count = 0
Ono_tweet_count = 0
Else_char_count = 0
Else_tweet_count = 0

for line in sys.stdin:
    try:
        data = json.loads(line)
        if data['user']['id_str'] == "211178363":
          tweet= data['text']
          tweet2 = tweet.strip()
          for char in tweet2:
           Ono_char_count = Ono_char_count + 1
          Ono_tweet_count += 1
        if data['user']['id_str'] != "211178363":
          tweet3= data['text']
          tweet4 = tweet.strip()
          for char in tweet4:
           Else_char_count = Else_char_count + 1
          Else_tweet_count += 1
    except:
      continue

print '%s\t%s' %("Ono_char_count", Ono_char_count)
print '%s\t%s' %("Ono_tweet_count", Ono_tweet_count)
print '%s\t%s' %("Else_char_count", Else_char_count)
print '%s\t%s' %("Else_tweet_count", Else_tweet_count)
