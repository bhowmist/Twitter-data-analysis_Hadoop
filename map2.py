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
      (key, val) = line.split('\t',1)
      if key=='Ono_char_count':
         Ono_char_count = Ono_char_count + int(val)
      if key=='Ono_tweet_count':
         Ono_tweet_count = Ono_tweet_count + int(val)
      if key=='Else_char_count':
         Else_char_count = Else_char_count + int(val)
      if key=='Else_tweet_count':
         Else_tweet_count = Else_tweet_count + int(val)


    except:
      continue

print '%s\t%s' %("Ono_char_count", Ono_char_count)
print '%s\t%s' %("Ono_tweet_count", Ono_tweet_count)
print '%s\t%s' %("Else_char_count", Else_char_count)
print '%s\t%s' %("Else_tweet_count", Else_tweet_count)
