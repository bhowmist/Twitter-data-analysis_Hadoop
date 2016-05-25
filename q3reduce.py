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
    (key,val) = line.split('\t',1)
    if key=='Ono_char_count':
       Ono_char_count = Ono_char_count + int(val)
    if key=='Ono_tweet_count':
       Ono_tweet_count = Ono_tweet_count + int(val)
    if key=='Else_char_count':
       Else_char_count = Else_char_count + float(val)
    if key=='Else_tweet_count':
       Else_tweet_count = Else_tweet_count + float(val)
  except:
    continue

Ono_average = (Ono_char_count*1.0)/Ono_tweet_count
Else_average = Else_char_count/Else_tweet_count
comparison= Ono_average/Else_average

print "%s\t%s" %("Ono_average:", Ono_average)
print "%s\t%s" %("Else_average:", Else_average)
print ("PrezOno's tweet length compared to the avg. of all others(ratio):",comparison)

