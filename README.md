# Twitter-data-analysis_Hadoop
I have analyzed he twitter data of an user named @PrezOno. The relevant information was extracted and analyzed very fast from more 900gb of data using hadoop-map reduce.
Two map functions were used. The first map function transferred the data that I am using into a smaller dataset. The second map function was used as an additional combiner. The reduce code was used to get the final output of @PrezOno’s average amount of tweets and everyone else’s average amount of tweets.The average length of @PrezOno’s tweets  and the average length of the rest of tweets was also found. At the end the ratio of average tweet length of @PrezOno’s tweets to the average tweet length of others was found.

Example output:
Ono_average:106.025698755 
Else_average:107.039539671
("PrezOno's tweet length compared to the avg. of all others(ratio):",1.009562218)
